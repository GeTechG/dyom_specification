"""
ObjectiveObject - Interact with an object objective.
"""

from typing import Literal
from enum import IntEnum
from pydantic import Field
from .base import ObjectiveBase


class ObjectObjectiveType(IntEnum):
    """Object interaction types.
        TOUCH = 0
        DAMAGE = 1
        PHOTOGRAPH = 2
        SHOOT = 3
    """
    TOUCH = 0
    DAMAGE = 1
    PHOTOGRAPH = 2
    SHOOT = 3


class ObjectiveObject(ObjectiveBase):
    """
    Object objective - Interact with a 3D object.

    Player must interact with a specific object in various ways: touch it, damage it,
    photograph it, or shoot it. Object has position and full 3D rotation.

    Default text: varies by objective type
    """

    # Objective type
    objective_type: Literal[19] = Field(19, description="Objective type (19 = Object)")

    # Object properties
    object_id: int = Field(1221, description="Object model ID from GTA San Andreas", ge=0)

    # Object rotation (note: rotation_z is in the position normally used for direction)
    rotation_x: float = Field(0.0, description="X-axis rotation in degrees", ge=0, le=360)
    rotation_y: float = Field(0.0, description="Y-axis rotation in degrees", ge=0, le=360)
    rotation_z: float = Field(0.0, description="Z-axis rotation in degrees", ge=0, le=360)

    # Interaction type
    objective: ObjectObjectiveType = Field(
        ObjectObjectiveType.TOUCH,
        description="Interaction type (0=Touch, 1=Damage, 2=Photograph, 3=Shoot)"
    )

    # Radar marker
    radar_marker: int = Field(
        2,
        description="Radar marker color ID (-1=None, 0=Red, 1=Green, 2=Blue, 3=White, 4=Yellow, or custom RGB encoded as int)"
    )

    # Unused fields
    unused_1: int = Field(0, description="Unused field")
    unused_2: int = Field(0, description="Unused field")
    unused_3: int = Field(0, description="Unused field")
    unused_4: int = Field(0, description="Unused field")
    unused_5: float = Field(0.0, description="Unused field (float)")

    # Objective text
    text: str = Field("", description="Objective description text shown to player")

    class Config:
        use_enum_values = True
        json_schema_extra = {
            "example": {
                "position_x": 2495.0,
                "position_y": -1688.0,
                "position_z": 13.3,
                "rotation_z": 0.0,
                "interior": 0,
                "objective_type": 19,
                "object_id": 1221,
                "rotation_x": 0.0,
                "rotation_y": 0.0,
                "objective": 0,  # ObjectObjectiveType.TOUCH
                "radar_marker": 2,
                "unused_1": 0,
                "unused_2": 0,
                "unused_3": 0,
                "unused_4": 0,
                "unused_5": 0.0,
                "text": "Touch the crate!"
            }
        }
