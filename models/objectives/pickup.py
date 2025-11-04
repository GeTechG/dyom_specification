"""
ObjectivePickup - Collect a pickup objective.
"""

from typing import Literal
from enum import IntEnum
from pydantic import Field
from .base import ObjectiveBase


class PickupObjectiveFlags(IntEnum):
    """Flags for pickup objectives.
        COLLECT_ALL = 2
        COUNTER = 4
    """
    COLLECT_ALL = 2
    COUNTER = 4


class ObjectivePickup(ObjectiveBase):
    """
    Pickup objective - Collect a pickup item.

    The player must collect a specific pickup item (weapon, health, armor, etc.).
    Can be configured to require collecting all pickups with the same object ID,
    or display a counter showing collection progress.
    Default text: "Get the pickup."
    """

    # Objective type
    objective_type: Literal[3] = Field(3, description="Objective type (3 = Pickup)")

    # Pickup properties
    object_id: int = Field(
        1210,
        description="Pickup object ID (1240=Health, 1241=Drugs, 1242=Armor, 1247=Police bribe, 370=Jetpack, 100=Weapon, 101=Custom object)",
        ge=0
    )
    ammo: int = Field(0, description="Ammunition count for weapon pickups", ge=0)

    # Radar marker
    radar_marker: int = Field(
        1,
        description="Radar marker color ID (-1=None, 0=Red, 1=Green, 2=Blue, 3=White, 4=Yellow, or custom RGB encoded as int)"
    )

    # Behavior flags
    flags: int = Field(
        0,
        description=(
            "Pickup objective flags bitfield - combine values using bitwise OR. "
            "Available flags: "
            "COLLECT_ALL=2 (player must collect all pickups with this object_id), "
            "COUNTER=4 (show collection counter on screen). "
            "Example: 6=collect all with counter (2+4)"
        ),
        ge=0
    )

    # Unused fields (note: unused_1 is a float in the file structure)
    unused_1: float = Field(0.0, description="Unused field (float)")
    unused_2: int = Field(0, description="Unused field")
    unused_3: int = Field(0, description="Unused field")
    unused_4: int = Field(0, description="Unused field")
    unused_5: int = Field(0, description="Unused field")
    unused_6: int = Field(0, description="Unused field")
    unused_7: float = Field(0.0, description="Unused field (float)")

    # Objective text
    text: str = Field("", description="Objective description text shown to player")

    class Config:
        use_enum_values = True
        json_schema_extra = {
            "example": {
                "position_x": 2495.0,
                "position_y": -1688.0,
                "position_z": 13.3,
                "direction": 0.0,
                "interior": 0,
                "objective_type": 3,
                "object_id": 1240,
                "ammo": 0,
                "radar_marker": 1,  # RadarMarker.GREEN
                "flags": 0,
                "unused_1": 0.0,
                "unused_2": 0,
                "unused_3": 0,
                "unused_4": 0,
                "unused_5": 0,
                "unused_6": 0,
                "unused_7": 0.0,
                "text": "Collect the health pickup!"
            }
        }
