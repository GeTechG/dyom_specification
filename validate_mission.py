import json
import sys
from pathlib import Path
from typing import Dict, List, Set, Tuple
from pydantic import ValidationError

from models import Mission, AnyObjective


class ValidationResult:
    """Holds validation results with errors and warnings."""

    def __init__(self):
        self.errors: List[str] = []
        self.warnings: List[str] = []
        self.info: List[str] = []

    def add_error(self, message: str):
        """Add an error message."""
        self.errors.append(f"ERROR: {message}")

    def add_warning(self, message: str):
        """Add a warning message."""
        self.warnings.append(f"WARNING: {message}")

    def add_info(self, message: str):
        """Add an info message."""
        self.info.append(f"INFO: {message}")

    def is_valid(self) -> bool:
        """Check if validation passed (no errors)."""
        return len(self.errors) == 0

    def print_results(self):
        """Print all validation results."""
        for msg in self.info:
            print(f"  {msg}")
        for msg in self.warnings:
            print(f"  {msg}")
        for msg in self.errors:
            print(f"  {msg}")


def validate_entity_limits(mission: Mission, result: ValidationResult):
    """Check that entity counts don't exceed limits."""

    limits = {
        "objectives": (mission.objectives, 100),
        "actors": (mission.actors, 100),
        "cars": (mission.cars, 50),
        "pickups": (mission.pickups, 50),
        "objects": (mission.objects, 100),
    }

    for entity_type, (entities, max_count) in limits.items():
        count = len(entities)
        if count > max_count:
            result.add_error(f"Too many {entity_type}: {count} (max: {max_count})")
        elif count > max_count * 0.9:  # Warn at 90%
            result.add_warning(f"Approaching limit for {entity_type}: {count}/{max_count}")

        if count > 0:
            result.add_info(f"{entity_type.capitalize()}: {count}/{max_count}")


def validate_route_points(mission: Mission, result: ValidationResult):
    """Check total route points across all route types."""

    total_points = 0

    for route in mission.paths.routes:
        total_points += len(route.points)

    for movement in mission.paths.movements:
        total_points += len(movement.points)

    for displacement in mission.paths.displacements:
        total_points += len(displacement.points)

    max_points = 399
    if total_points > max_points:
        result.add_error(f"Too many total route points: {total_points} (max: {max_points})")
    elif total_points > max_points * 0.9:
        result.add_warning(f"Approaching route point limit: {total_points}/{max_points}")

    if total_points > 0:
        result.add_info(f"Total route points: {total_points}/{max_points}")


def validate_references(mission: Mission, result: ValidationResult):
    """Validate that entity references are valid."""

    # Build sets of valid IDs
    actor_ids = {i for i in range(len(mission.actors))}
    car_ids = {i for i in range(len(mission.cars))}
    object_ids = {i for i in range(len(mission.objects))}
    pickup_ids = {i for i in range(len(mission.pickups))}
    route_ids = {r.id for r in mission.paths.routes}
    movement_ids = {r.id for r in mission.paths.movements}
    displacement_ids = {r.id for r in mission.paths.displacements}

    # Check actor references
    for idx, actor in enumerate(mission.actors):
        if actor.animation_info.route is not None:
            if actor.animation_info.route >= 0 and (actor.animation_info.route not in route_ids and actor.animation_info.route not in car_ids):
                result.add_error(f"Actor {idx}: Invalid route {actor.animation_info.route}")

    # Check object references
    for idx, obj in enumerate(mission.objects):
        if obj.route_id is not None:
            if obj.behaviour == 1 and obj.route_id >= 0 and obj.route_id not in displacement_ids:
                result.add_error(f"Object {idx}: Invalid displacement_id {obj.route_id}")
            elif obj.behaviour > 1 and obj.route_id >= 0 and obj.route_id not in movement_ids:
                result.add_error(f"Object {idx}: Invalid movement_id {obj.route_id}")

    # Check objective references
    for idx, objective in enumerate(mission.objectives):
        obj_dict = objective.model_dump()
        obj_type = obj_dict.get('objective_type')

        # Actor objectives
        if obj_type in [1, 2, 3]:  # KILL_ACTOR, KILL_ACTOR_CONDITIONAL, KILL_ACTOR_ANY
            actor_id = obj_dict.get('actor_id', -1)
            if actor_id >= 0 and actor_id not in actor_ids:
                result.add_error(f"Objective {idx}: Invalid actor_id {actor_id}")

        # Car objectives
        elif obj_type in [4, 5, 6, 7]:  # DESTROY_CAR, ENTER_CAR, STEAL_CAR, FLIP_CAR
            car_id = obj_dict.get('car_id', -1)
            if car_id >= 0 and car_id not in car_ids:
                result.add_error(f"Objective {idx}: Invalid car_id {car_id}")

        # Pickup objectives
        elif obj_type == 10:  # PICKUP
            pickup_id = obj_dict.get('pickup_id', -1)
            if pickup_id >= 0 and pickup_id not in pickup_ids:
                result.add_error(f"Objective {idx}: Invalid pickup_id {pickup_id}")

        # Object objectives
        elif obj_type == 24:  # OBJECT
            object_id = obj_dict.get('object_id', -1)
            if object_id >= 0 and object_id not in object_ids:
                result.add_error(f"Objective {idx}: Invalid object_id {object_id}")

        # Cutscene objectives
        elif obj_type == 11:  # CUTSCENE
            movement_id = obj_dict.get('movement_id', -1)
            if movement_id >= 0 and movement_id not in movement_ids:
                result.add_error(f"Objective {idx}: Invalid movement_id {movement_id}")


def validate_mission_file(file_path: Path) -> ValidationResult:
    """
    Validate a DYOM mission JSON file.

    Args:
        file_path: Path to the JSON file to validate

    Returns:
        ValidationResult object with errors, warnings, and info
    """
    result = ValidationResult()

    # Check file exists
    if not file_path.exists():
        result.add_error(f"File not found: {file_path}")
        return result

    # Load JSON
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        result.add_error(f"Invalid JSON: {e}")
        return result
    except Exception as e:
        result.add_error(f"Failed to read file: {e}")
        return result

    # Validate against Pydantic model
    try:
        mission = Mission.model_validate(data)
    except ValidationError as e:
        result.add_error("Schema validation failed:")
        for error in e.errors():
            loc = " -> ".join(str(x) for x in error['loc'])
            msg = error['msg']
            result.add_error(f"  {loc}: {msg}")
        return result

    # Additional validation checks
    validate_entity_limits(mission, result)
    validate_route_points(mission, result)
    validate_references(mission, result)

    return result


def main():
    """Main entry point for the validator."""

    if len(sys.argv) < 2:
        print("Usage: python validate_mission.py <mission.json>")
        print("\nValidates a DYOM mission JSON file against the specification.")
        sys.exit(1)

    file_path = Path(sys.argv[1])

    print(f"Validating: {file_path}")
    print("-" * 60)

    result = validate_mission_file(file_path)
    result.print_results()

    print("-" * 60)
    if result.is_valid():
        print("[PASS] Validation passed!")
        sys.exit(0)
    else:
        print(f"[FAIL] Validation failed with {len(result.errors)} error(s)")
        sys.exit(1)


if __name__ == "__main__":
    main()
