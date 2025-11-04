"""
ObjectivePlayerTeleport - Teleport player to a location objective.
"""

from typing import Literal
from pydantic import Field
from .base import ObjectiveBase


class ObjectivePlayerTeleport(ObjectiveBase):
    """
    Player Teleport objective - Teleport player to a new location.

    Instantly moves the player to a specified position and optionally changes their skin,
    weapon, health, and facing direction. Happens automatically without player interaction.

    Default text: "" (no text, instant teleport)
    """

    # Objective type
    objective_type: Literal[7] = Field(7, description="Objective type (7 = Player Teleport)")

    # Player state changes
    skin: int = Field(
        0,
        description="Player skin/character model ID to change to (0 = keep current skin)",
        ge=0
    )
    weapon: int = Field(
        0,
        description="Weapon ID to give player (0 = no weapon change)",
        ge=0
    )
    ammo: int = Field(
        1,
        description="Ammunition count for the weapon (1 = default ammo for weapon type)",
        ge=0
    )
    health: int = Field(
        100,
        description="Player health to set (0-200, 100 = full health)",
        ge=0,
        le=200
    )

    # Unused fields
    unused_1: int = Field(0, description="Unused field")
    unused_2: int = Field(0, description="Unused field")
    unused_3: int = Field(0, description="Unused field")
    unused_4: int = Field(0, description="Unused field")
    unused_5: int = Field(0, description="Unused field")
    unused_6: int = Field(0, description="Unused field")
    unused_7: str = Field("", description="Unused field (string)")

    class Config:
        use_enum_values = True
        json_schema_extra = {
            "example": {
                "position_x": 2495.0,
                "position_y": -1688.0,
                "position_z": 13.3,
                "direction": 90.0,
                "interior": 0,
                "objective_type": 7,
                "skin": 0,
                "weapon": 30,
                "ammo": 500,
                "health": 100,
                "unused_1": 0,
                "unused_2": 0,
                "unused_3": 0,
                "unused_4": 0,
                "unused_5": 0,
                "unused_6": 0,
                "unused_7": ""
            }
        }
