"""
ObjectivePlayerTeleportCar - Teleport player into a vehicle objective.
"""

from typing import Literal
from pydantic import Field
from .base import ObjectiveBase


class ObjectivePlayerTeleportCar(ObjectiveBase):
    """
    Player Teleport Car objective - Teleport player into a vehicle.

    Spawns a vehicle and teleports the player into it at a specific seat.
    Can configure vehicle properties, colors, health, and immunity flags.
    Supports driveby mode flag.

    Default text: "" (no text, instant teleport)
    """

    # Objective type
    objective_type: Literal[9] = Field(9, description="Objective type (9 = Player Teleport Car)")

    # Vehicle properties
    car_id: int = Field(405, description="Vehicle model ID", ge=0)
    color_primary: int = Field(0, description="Primary color ID (0-126, -1=random)", ge=-1, le=126)
    color_secondary: int = Field(36, description="Secondary color ID (0-126, -1=random)", ge=-1, le=126)
    health: int = Field(1000, description="Vehicle health (0-1000)", ge=0, le=1000)

    # Seat position
    seat: int = Field(
        0,
        description="Vehicle seat to place player in (0=Driver, 1=Passenger, 2=Rear left, 3=Rear right)",
        ge=0,
        le=3
    )

    # Radar marker
    radar_marker: int = Field(
        -1,
        description="Radar marker color ID (-1=None, 0=Red, 1=Green, 2=Blue, 3=White, 4=Yellow, or custom RGB encoded as int)"
    )

    # Behavior flags
    flags: int = Field(
        0,
        description=(
            "Behavior and immunity flags bitfield from CarFlags - combine values using bitwise OR. "
            "Available flags: "
            "IMMUNE_BULLET=2, IMMUNE_EXPLOSION=4, IMMUNE_TYRES=8, IMMUNE_COLLISION=16, "
            "LOCKED=32, HANDBRAKED=64, MUST_DESTROY=256, DRIVEBY=512. "
            "Example: 512=driveby mode enabled"
        ),
        ge=0
    )

    # Unused fields
    unused_1: int = Field(0, description="Unused field")
    unused_2: int = Field(0, description="Unused field")
    unused_3: int = Field(0, description="Unused field")

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
                "objective_type": 9,
                "car_id": 405,
                "color_primary": 1,
                "color_secondary": 36,
                "health": 1000,
                "seat": 0,
                "radar_marker": -1,
                "flags": 0,
                "unused_1": 0,
                "unused_2": 0,
                "unused_3": 0,
                "text": ""
            }
        }
