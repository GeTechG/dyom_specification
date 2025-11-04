"""
ObjectiveActor - Kill an enemy actor objective.
"""

from typing import Literal
from pydantic import Field
from .base import ObjectiveBase


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
    skin: int = Field(102, description="Skin/character model ID", ge=0)

    # Combat stats
    weapon: int = Field(0, description="Weapon ID (0 = unarmed)", ge=0)
    ammo: int = Field(0, description="Ammunition count", ge=0)
    health: int = Field(100, description="Health percentage (0-200)", ge=0, le=200)
    accuracy: int = Field(50, description="Shooting accuracy percentage (0-100)", ge=0, le=100)

    # Radar marker
    radar_marker: int = Field(
        0,
        description="Radar marker color ID (-1=None, 0=Red, 1=Green, 2=Blue, 3=White, 4=Yellow, or custom RGB encoded as int)"
    )

    # Behavior flags
    flags: int = Field(
        0,
        description=(
            "Behavior flags bitfield from ActorFlags - combine values using bitwise OR. "
            "Available flags: "
            "HOLD_POSITION=2, ATTACK_DIRECT=4, FOLLOW=8, HEADSHOT_IMMUNE=16, "
            "KILL_WHOLE_GANG=32, HEALTH_BAR=64, ENEMY_2=128. "
            "Example: 36=kill whole gang+headshot immune (32+4)"
        ),
        ge=0
    )

    # Animation
    animation: int = Field(-1, description="Animation type (see Animation enum, -12 to 129)")
    animation_argument: int = Field(0, description="Animation argument (route ID, seat, etc.)")

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
                "radar_marker": 0,  # RadarMarker.RED
                "flags": 0,
                "animation": -1,  # Animation.NONE
                "animation_argument": 0,
                "unused_1": 0,
                "text": "Kill the gang member!"
            }
        }
