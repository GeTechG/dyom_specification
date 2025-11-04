"""
Route models for DYOM missions.

Routes define paths for actors, vehicles, objects, and camera movements.
They consist of multiple points that entities follow in sequence.
"""

from typing import List
from enum import Enum
from pydantic import BaseModel, Field


class RouteType(str, Enum):
    """
    Type of route/path in the mission.

    - ROUTE: Movement path for actors and vehicles to follow
    - MOVEMENT: Camera movement path for cutscenes
    - DISPLACEMENT: Object displacement - moves object from initial position to new position when triggered
    - INVALID: Invalid or uninitialized route type
    """
    ROUTE = "route"
    MOVEMENT = "movement"
    DISPLACEMENT = "displacement"
    INVALID = "invalid"


class RoutePoint(BaseModel):
    """
    A single point in a route path.

    Contains position and optional rotation information.
    """
    position_x: float = Field(0.0, description="X coordinate of the point")
    position_y: float = Field(0.0, description="Y coordinate of the point")
    position_z: float = Field(0.0, description="Z coordinate of the point")

    rotation_x: float = Field(0.0, description="X-axis rotation in degrees (used for camera movements)")
    rotation_y: float = Field(0.0, description="Y-axis rotation in degrees (used for camera movements)")
    rotation_z: float = Field(0.0, description="Z-axis rotation in degrees (used for camera movements)")

    class Config:
        json_schema_extra = {
            "example": {
                "position_x": 2495.0,
                "position_y": -1688.0,
                "position_z": 13.3,
                "rotation_x": 0.0,
                "rotation_y": 0.0,
                "rotation_z": 90.0
            }
        }


class RouteEntry(BaseModel):
    """
    Low-level route entry stored in mission file.

    This is the raw format used in DYOM files. Route entries are stored
    as a flat array with index references. Maximum 400 route entries per mission.

    Note: This is primarily for file I/O. Use Route model for working with paths.
    """
    next_index: int = Field(0, description="Index of next route entry, or -1 for end, -2 for slow loop, -3 for normal loop", ge=-3)
    argument_1: float = Field(0.0, description="First argument (typically X position or rotation)")
    argument_2: float = Field(0.0, description="Second argument (typically Y position or rotation)")
    argument_3: float = Field(0.0, description="Third argument (typically Z position or rotation)")

    class Config:
        json_schema_extra = {
            "example": {
                "next_index": 1,
                "argument_1": 2495.0,
                "argument_2": -1688.0,
                "argument_3": 13.3
            }
        }


class Route(BaseModel):
    """
    A complete route/path in the mission.

    Routes define movement paths for actors, vehicles, objects, or camera.
    Each route consists of multiple points that define the path.

    Route types:
    - Routes: Actor/vehicle movement paths - entities follow waypoints in sequence
    - Movements: Camera paths for cutscenes - camera follows path during cutscene
    - Displacements: Object displacement - object moves from initial position to new position when triggered (duration specifies animation time)
    """
    id: int = Field(..., description="Unique route ID used to reference this route", ge=0)
    type: RouteType = Field(..., description="Type of route (route/movement/displacement)")
    points: List[RoutePoint] = Field(default_factory=list, description="List of points defining the path")
    loop: bool = Field(False, description="Whether the route loops back to the start (for routes and movements)")
    duration: float = Field(
        1.0,
        description="Duration in seconds for displacement animation (only used for displacement type, not for routes or movements)",
        ge=0
    )
    trigger_diameter: float = Field(1.0, description="Trigger radius for reaching waypoints (in game units)", ge=0)

    class Config:
        use_enum_values = True
        json_schema_extra = {
            "example": {
                "id": 0,
                "type": "route",
                "points": [
                    {
                        "position_x": 2495.0,
                        "position_y": -1688.0,
                        "position_z": 13.3,
                        "rotation_x": 0.0,
                        "rotation_y": 0.0,
                        "rotation_z": 0.0
                    },
                    {
                        "position_x": 2500.0,
                        "position_y": -1690.0,
                        "position_z": 13.3,
                        "rotation_x": 0.0,
                        "rotation_y": 0.0,
                        "rotation_z": 0.0
                    }
                ],
                "loop": False,
                "duration": 1.0,
                "trigger_diameter": 1.0
            }
        }
