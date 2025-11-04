"""
ObjectiveCountdown - Display countdown timer objective.
"""

from typing import Literal
from pydantic import Field
from .base import ObjectiveBase


class ObjectiveCountdown(ObjectiveBase):
    """
    Countdown objective - Display a countdown timer.

    Shows a countdown timer on screen for the specified duration. The objective completes
    when the timer reaches zero. Typically used to create time pressure or delays.

    Note: This objective does not use interior ID.

    Default text: "" (timer is displayed on screen)
    """

    # Objective type
    objective_type: Literal[8] = Field(8, description="Objective type (8 = Countdown)")

    # Timer duration
    duration: int = Field(
        3000,
        description="Countdown duration in milliseconds (e.g., 3000 = 3 seconds)",
        ge=0
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
    unused_9: int = Field(0, description="Unused field")
    unused_10: int = Field(0, description="Unused field")

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
                "objective_type": 8,
                "duration": 5000,
                "unused_1": 0.0,
                "unused_2": 0,
                "unused_3": 0,
                "unused_4": 0,
                "unused_5": 0,
                "unused_6": 0,
                "unused_7": 0,
                "unused_8": 0,
                "unused_9": 0,
                "unused_10": 0,
                "text": "Wait for the signal..."
            }
        }
