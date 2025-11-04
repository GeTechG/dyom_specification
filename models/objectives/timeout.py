"""
ObjectiveTimeout - Wait with optional timer display objective.
"""

from typing import Literal
from pydantic import Field
from .base import ObjectiveBase


class ObjectiveTimeout(ObjectiveBase):
    """
    Timeout objective - Wait for a duration with optional timer display.

    Similar to Countdown but completes automatically after the duration.
    Can optionally display the timer on screen.

    Note: This objective does not use interior ID.

    Default text: "" (timer may be displayed on screen)
    """

    # Objective type
    objective_type: Literal[10] = Field(10, description="Objective type (10 = Timeout)")

    # Timer configuration
    duration: int = Field(
        3000,
        description="Wait duration in milliseconds (e.g., 3000 = 3 seconds)",
        ge=0
    )
    show_timer: int = Field(
        0,
        description="Display timer on screen (0 = hidden, 1 = visible)",
        ge=0,
        le=1
    )

    # Unused fields
    unused_1: float = Field(0.0, description="Unused field (float)")
    unused_2: int = Field(0, description="Unused field")
    unused_3: int = Field(0, description="Unused field")
    unused_4: int = Field(0, description="Unused field")
    unused_5: int = Field(0, description="Unused field")
    unused_6: int = Field(0, description="Unused field")
    unused_7: int = Field(0, description="Unused field")
    unused_8: int = Field(0, description="Unused field")
    unused_9: float = Field(0.0, description="Unused field (float)")

    # Objective text
    text: str = Field("", description="Objective description text shown to player")

    class Config:
        use_enum_values = True
        json_schema_extra = {
            "example": {
                "position_x": 0.0,
                "position_y": 0.0,
                "position_z": 0.0,
                "direction": 0.0,
                "interior": 0,
                "objective_type": 10,
                "duration": 5000,
                "show_timer": 1,
                "unused_1": 0.0,
                "unused_2": 0,
                "unused_3": 0,
                "unused_4": 0,
                "unused_5": 0,
                "unused_6": 0,
                "unused_7": 0,
                "unused_8": 0,
                "unused_9": 0.0,
                "text": "Wait for backup..."
            }
        }
