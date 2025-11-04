"""
ObjectivePhoneCall - Display phone call message objective.
"""

from typing import Literal
from pydantic import Field
from .base import ObjectiveBase


class ObjectivePhoneCall(ObjectiveBase):
    """
    Phone Call objective - Display a phone call message.

    Shows a phone call interface with the objective text for the specified duration.
    Used for story dialogue and mission briefings.

    Note: This objective does not use interior ID or position fields meaningfully.

    Default text: "" (text displayed in phone interface)
    """

    # Objective type
    objective_type: Literal[18] = Field(18, description="Objective type (18 = Phone Call)")

    # Phone call duration
    duration: int = Field(
        4000,
        description="Phone call display duration in milliseconds (e.g., 4000 = 4 seconds)",
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
    unused_10: float = Field(0.0, description="Unused field (float)")

    # Objective text
    text: str = Field("", description="Message text displayed during phone call")

    class Config:
        use_enum_values = True
        json_schema_extra = {
            "example": {
                "position_x": 0.0,
                "position_y": 0.0,
                "position_z": 0.0,
                "direction": 0.0,
                "interior": 0,
                "objective_type": 18,
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
                "unused_10": 0.0,
                "text": "Meet me at the docks, we have business to discuss."
            }
        }
