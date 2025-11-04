"""
ObjectiveWantedLevel - Set wanted level objective.
"""

from typing import Literal
from pydantic import Field
from .base import ObjectiveBase


class ObjectiveWantedLevel(ObjectiveBase):
    """
    Wanted Level objective - Set player's wanted level range.

    Sets the player's current wanted level and defines min/max constraints.
    Completes immediately.

    Note: This objective does not use interior ID or position fields meaningfully.

    Default text: "" (no text, instant change)
    """

    # Objective type
    objective_type: Literal[14] = Field(14, description="Objective type (14 = Wanted Level)")

    # Wanted level configuration
    level_current: int = Field(
        0,
        description="Current wanted level to set (0-6 stars)",
        ge=0,
        le=6
    )
    level_min: int = Field(
        0,
        description="Minimum wanted level allowed (0-6 stars)",
        ge=0,
        le=6
    )
    level_max: int = Field(
        6,
        description="Maximum wanted level allowed (0-6 stars)",
        ge=0,
        le=6
    )

    # Unused fields
    unused_1: float = Field(0.0, description="Unused field (float)")
    unused_2: float = Field(0.0, description="Unused field (float)")
    unused_3: int = Field(0, description="Unused field")
    unused_4: int = Field(0, description="Unused field")
    unused_5: int = Field(0, description="Unused field")
    unused_6: int = Field(0, description="Unused field")
    unused_7: int = Field(0, description="Unused field")
    unused_8: int = Field(0, description="Unused field")
    unused_9: str = Field("", description="Unused field (string)")

    class Config:
        use_enum_values = True
        json_schema_extra = {
            "example": {
                "position_x": 0.0,
                "position_y": 0.0,
                "position_z": 0.0,
                "direction": 0.0,
                "interior": 0,
                "objective_type": 14,
                "level_current": 0,
                "level_min": 0,
                "level_max": 6,
                "unused_1": 0.0,
                "unused_2": 0.0,
                "unused_3": 0,
                "unused_4": 0,
                "unused_5": 0,
                "unused_6": 0,
                "unused_7": 0,
                "unused_8": 0,
                "unused_9": ""
            }
        }
