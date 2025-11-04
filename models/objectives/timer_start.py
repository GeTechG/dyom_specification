"""
ObjectiveTimerStart - Start mission timer objective.
"""

from typing import Literal
from pydantic import Field
from .base import ObjectiveBase


class ObjectiveTimerStart(ObjectiveBase):
    """
    Timer Start objective - Begin mission time measurement.

    Starts recording mission completion time. Used for speedrun tracking.
    Completes immediately.

    Note: This objective does not use interior ID or position fields meaningfully.

    Default text: "" (no text, instant start)
    """

    # Objective type
    objective_type: Literal[16] = Field(16, description="Objective type (16 = Start Timer)")

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
    unused_11: int = Field(0, description="Unused field")
    unused_12: str = Field("", description="Unused field (string)")

    class Config:
        use_enum_values = True
        json_schema_extra = {
            "example": {
                "position_x": 0.0,
                "position_y": 0.0,
                "position_z": 0.0,
                "direction": 0.0,
                "interior": 0,
                "objective_type": 16,
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
                "unused_11": 0,
                "unused_12": ""
            }
        }
