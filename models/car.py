"""
Car model for DYOM missions.

Represents vehicles in a DYOM mission, including their model, colors, health,
and behavior settings.
"""

from enum import IntEnum
from pydantic import BaseModel, Field


class CarFlags(IntEnum):
    """
    Behavior and immunity flags for vehicles (bitfield).

    Multiple flags can be combined using bitwise OR.
    Example: IMMUNE_BULLET | LOCKED = 2 | 32 = 34
    """
    IMMUNE_BULLET = 2       # Bit 1: Vehicle immune to bullet damage
    IMMUNE_EXPLOSION = 4    # Bit 2: Vehicle immune to explosions
    IMMUNE_TYRES = 8        # Bit 3: Tyres cannot be popped
    IMMUNE_COLLISION = 16   # Bit 4: Vehicle immune to collision damage
    LOCKED = 32             # Bit 5: Vehicle doors locked
    HANDBRAKED = 64         # Bit 6: Handbrake engaged
    MUST_DESTROY = 256      # Bit 8: Objective requires destroying this vehicle
    DRIVEBY = 512           # Bit 9: Enable drive-by shooting


class Car(BaseModel):
    """
    A vehicle in a DYOM mission.

    Vehicles can be cars, bikes, boats, planes, helicopters, and other vehicle types.
    Maximum 50 vehicles per mission.
    """

    # Vehicle model and appearance
    car_id: int = Field(..., description="Vehicle model ID (400-611, see vehicle list)", ge=400, le=611)
    color_primary: int = Field(..., description="Primary color ID (0-126)", ge=0, le=126)
    color_secondary: int = Field(..., description="Secondary color ID (0-126)", ge=0, le=126)

    # Position and orientation
    position_x: float = Field(..., description="X coordinate in game world")
    position_y: float = Field(..., description="Y coordinate in game world")
    position_z: float = Field(..., description="Z coordinate in game world (height)")
    direction: float = Field(0.0, description="Facing direction in degrees (0-360)", ge=0, le=360)
    interior: int = Field(0, description="Interior ID (0 = outdoor)", ge=0)

    # Vehicle state
    health: int = Field(1000, description="Vehicle health (0-1000+)", ge=0)
    flags: int = Field(
        0,
        description=(
            "Behavior and immunity flags bitfield - combine values using bitwise OR. "
            "Available flags: "
            "IMMUNE_BULLET=2, IMMUNE_EXPLOSION=4, IMMUNE_TYRES=8, IMMUNE_COLLISION=16, "
            "LOCKED=32, HANDBRAKED=64, MUST_DESTROY=256, DRIVEBY=512. "
            "Example combinations: 0=none, 34=bullet immune+locked (2+32), "
            "30=all immunities (2+4+8+16)"
        ),
        ge=0
    )

    # Lifetime control
    spawn: int = Field(0, description="Objective number when vehicle spawns (0 = mission start)", ge=0)
    despawn: int = Field(1000, description="Objective number when vehicle despawns (1000 = never)", ge=0, le=1000)
    must_survive: int = Field(0, description="If 1, mission fails if vehicle is destroyed", ge=0, le=1)

    class Config:
        use_enum_values = True
        json_schema_extra = {
            "example": {
                "car_id": 560,
                "color_primary": 6,
                "color_secondary": 1,
                "position_x": 2495.0,
                "position_y": -1688.0,
                "position_z": 13.3,
                "direction": 90.0,
                "interior": 0,
                "health": 1000,
                "flags": 0,
                "spawn": 0,
                "despawn": 1000,
                "must_survive": 0
            }
        }
