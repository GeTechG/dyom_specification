"""
ObjectiveCar - Drive or destroy a vehicle objective.
"""

from typing import Literal
from pydantic import Field
from .base import ObjectiveBase


class ObjectiveCar(ObjectiveBase):
    """
    Car objective - Drive or destroy a vehicle.

    The player must either enter and drive a specific vehicle, or destroy it.
    The objective type is determined by the MUST_DESTROY flag.
    Default text: "Go to the car and enter it."
    """

    # Objective type
    objective_type: Literal[1] = Field(1, description="Objective type (1 = Car)")

    # Vehicle properties
    car_id: int = Field(526, description="Vehicle model ID", ge=0)
    color_primary: int = Field(0, description="Primary color ID (0-126, -1=random)", ge=-1, le=126)
    color_secondary: int = Field(36, description="Secondary color ID (0-126, -1=random)", ge=-1, le=126)
    health: int = Field(1000, description="Vehicle health (0-1000)", ge=0, le=1000)

    # Radar marker
    radar_marker: int = Field(
        2,
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
            "Example: 256=destroy objective, 290=destroy+bullet immune+locked (256+2+32)"
        ),
        ge=0
    )

    # Unused fields
    unused_1: int = Field(0, description="Unused field")
    unused_2: int = Field(0, description="Unused field")
    unused_3: int = Field(0, description="Unused field")
    unused_4: int = Field(0, description="Unused field")

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
                "objective_type": 1,
                "car_id": 526,
                "color_primary": 1,
                "color_secondary": 36,
                "health": 1000,
                "radar_marker": 2,  # RadarMarker.BLUE
                "flags": 0,
                "unused_1": 0,
                "unused_2": 0,
                "unused_3": 0,
                "unused_4": 0,
                "text": "Get into the car!"
            }
        }
