"""
ObjectiveActor - Kill an enemy actor objective.
"""

from typing import Literal, Optional
from pydantic import Field
from .base import ObjectiveBase
from .. import Skin, Animation, AnimationInfo, RadarMarker


class ObjectiveActor(ObjectiveBase):
    """
    Actor objective - Kill an enemy actor.

    The player must eliminate a specific enemy character. Can be configured for direct attack,
    gang elimination, health bars, and various combat parameters.
    Default text: "Kill the person."
    """

    # Objective type
    objective_type: Literal[5] = Field(5, description="Objective type (5 = Actor)")

    # Actor appearance
    skin: Skin = Field(..., description="Skin/character model ID (see skin list)")

    # Combat stats
    weapon: int = Field(0, description="Weapon ID (0 = unarmed)", ge=0)
    ammo: int = Field(0, description="Ammunition count", ge=0)
    health: int = Field(100, description="Health percentage (0-200)", ge=0, le=200)
    accuracy: int = Field(50, description="Shooting accuracy percentage (0-100)", ge=0, le=100)

    # Radar marker
    radar_marker: RadarMarker = Field(RadarMarker.RED, description="Radar marker color")

    hold_position: bool = Field(False, description="Hold position when attack")
    attack_direct: bool = Field(False, description="Immediate attack")
    follow: bool = Field(False, description="If gang - Friend, follow player")
    headshot_immune: bool = Field(False, description="Headshot Immune")
    kill_whole_gang: bool = Field(False, description="Objective requires killing all gang members")
    health_bar: bool = Field(False, description="Show health bar")
    enemy2: bool = Field(False, description="Is Enemy2 gang")

    # Animation
    animation: Animation = Field(-1, description="Animation type for this actor")
    animation_info: Optional[AnimationInfo] = Field(
        None,
        description=(
            "Additional animation parameters (route, vehicle seat, driver behavior). "
            "Only populated for animations that require additional context"
        )
    )

    # Unused field
    unused_1: int = Field(0, description="Unused field")

    # Objective text
    text: str = Field("", description="Objective description text shown to player")

    class Config:
        use_enum_values = True
        json_schema_extra = {
            "example": {
                "position_x": 2495.0,
                "position_y": -1688.0,
                "position_z": 13.3,
                "direction": 90.0,
                "interior": 0,
                "objective_type": 5,
                "skin": 102,
                "weapon": 30,
                "ammo": 500,
                "health": 100,
                "accuracy": 75,
                "radar_marker": 0,
                "hold_position": False,
                "attack_direct": False,
                "follow": False,
                "headshot_immune": False,
                "kill_whole_gang": False,
                "health_bar": False,
                "enemy2": False,
                "animation": -1,
                "animation_info": None,
                "unused_1": 0,
                "text": "Kill the gang member!"
            }
        }
