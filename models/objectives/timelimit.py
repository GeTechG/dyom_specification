"""
ObjectiveTimelimit - Set or adjust mission time limit objective.
"""

from typing import Literal
from pydantic import Field
from .base import ObjectiveBase


class ObjectiveTimelimit(ObjectiveBase):
    """
    Timelimit objective - Set or adjust mission time limit.

    Can set a new time limit, add time to existing limit, or disable the limit entirely.
    Behavior depends on the duration value:
    - Positive value: Set absolute time limit (replace existing)
    - Negative value: Add time to existing limit (adjust mode)
    - Value of -1: Disable time limit

    Note: This objective does not use interior ID or position fields meaningfully.

    Default text: "" (no text, instant change)
    """

    # Objective type
    objective_type: Literal[15] = Field(15, description="Objective type (15 = Timelimit)")

    # Time limit configuration
    duration: int = Field(
        30000,
        description=(
            "Time limit in milliseconds. "
            "Positive = set absolute limit, "
            "Negative = add to existing limit (adjust), "
            "-1 = disable limit. "
            "Example: 30000 = 30 seconds, -5000 = add 5 seconds, -1 = remove limit"
        )
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
    unused_10: float = Field(0.0, description="Unused field (float)")
    unused_11: str = Field("", description="Unused field (string)")

    class Config:
        use_enum_values = True
        json_schema_extra = {
            "example": {
                "position_x": 0.0,
                "position_y": 0.0,
                "position_z": 0.0,
                "direction": 0.0,
                "interior": 0,
                "objective_type": 15,
                "duration": 60000,
                "unused_1": 0.0,
                "unused_2": 0,
                "unused_3": 0,
                "unused_4": 0,
                "unused_5": 0,
                "unused_6": 0,
                "unused_7": 0,
                "unused_8": 0,
                "unused_9": 0,
                "unused_10": 0.0,
                "unused_11": ""
            }
        }
