"""
Pickup model for DYOM missions.

Represents collectible items in a DYOM mission including weapons, health, armor, and more.
"""

from enum import IntEnum
from pydantic import BaseModel, Field

from .object import ObjectModel


class PickupBehaviour(IntEnum):
    """Behavior types for pickups.
        UNPICKABLE = 1
        RESPAWN = 2  # 30 second respawn
        ONCE = 3  # Pickup once
        MINE = 10  # Mine, foot & vehicle 90m, 10s delay
        MINE_VEHICLE = 12  # Mine, vehicle only 90m, 10s delay
        VEHICLE = 14  # Vehicle only pickup
        RESPAWN_SLOW = 15  # 6 minute respawn
        MONEY = 19  # Money pickup
    """
    UNPICKABLE = 1
    RESPAWN = 2  # 30 second respawn
    ONCE = 3  # Pickup once
    MINE = 10  # Mine, foot & vehicle 90m, 10s delay
    MINE_VEHICLE = 12  # Mine, vehicle only 90m, 10s delay
    VEHICLE = 14  # Vehicle only pickup
    RESPAWN_SLOW = 15  # 6 minute respawn
    MONEY = 19  # Money pickup


class Pickup(BaseModel):
    """
    A pickup/collectible item in a DYOM mission.

    Pickups are items the player can collect, including weapons, health, armor,
    money, and other power-ups. They can have different behaviors like respawning
    or acting as mines.
    Maximum 50 pickups per mission.
    """

    # Pickup type
    object_id: ObjectModel = Field(...,description="Pickup object ID")

    # Weapon-specific
    ammo: int = Field(0, description="Ammunition count for weapon pickups (0 = default)", ge=0)

    # Behavior
    behaviour: PickupBehaviour = Field(
        PickupBehaviour.ONCE,
        description="Pickup behavior type (respawn, mine, etc.)"
    )

    # Position
    position_x: float = Field(..., description="X coordinate in game world")
    position_y: float = Field(..., description="Y coordinate in game world")
    position_z: float = Field(..., description="Z coordinate in game world (height)")

    # Lifetime control
    spawn: int = Field(0, description="Objective number when pickup spawns (0 = mission start)", ge=0)
    despawn: int = Field(1000, description="Objective number when pickup despawns (1000 = never)", ge=0, le=1000)

    class Config:
        use_enum_values = True
        json_schema_extra = {
            "example": {
                "object_id": 1240,
                "ammo": 0,
                "behaviour": 3,  # PickupBehaviour.ONCE
                "position_x": 2495.0,
                "position_y": -1688.0,
                "position_z": 13.3,
                "spawn": 0,
                "despawn": 1000
            }
        }
