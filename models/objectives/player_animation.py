"""
ObjectivePlayerAnimation - Play player animation objective.
"""

from typing import Literal, Optional
from pydantic import Field
from .base import ObjectiveBase
from .. import Animation, AnimationInfo


class ObjectivePlayerAnimation(ObjectiveBase):
    """
    Player Animation objective - Make player perform an animation.

    Forces the player to play a specific animation (standing, sitting, etc.).
    Can use animation routes for movement animations.

    Note: This objective does not use interior ID or position fields meaningfully.

    Default text: "" (no text, instant animation)
    """

    # Objective type
    objective_type: Literal[22] = Field(22, description="Objective type (22 = Player Animation)")

    # Animation configuration
    animation: Animation = Field(-1, description="Animation type for this actor")
    animation_info: Optional[AnimationInfo] = Field(
        None,
        description=(
            "Additional animation parameters (route, vehicle seat, driver behavior). "
            "Only populated for animations that require additional context"
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
    unused_10: str = Field("", description="Unused field (string)")

    class Config:
        use_enum_values = True
        json_schema_extra = {
            "example": {
                "position_x": 0.0,
                "position_y": 0.0,
                "position_z": 0.0,
                "direction": 0.0,
                "interior": 0,
                "objective_type": 22,
                "animation": -2,  # Animation.WALK
                "animation_info": {
                    "route": 399,
                    "vehicle_seat": None,
                    "driver_behaviour": None
                },
                "unused_1": 0.0,
                "unused_2": 0,
                "unused_3": 0,
                "unused_4": 0,
                "unused_5": 0,
                "unused_6": 0,
                "unused_7": 0,
                "unused_8": 0,
                "unused_9": 0,
                "unused_10": ""
            }
        }
