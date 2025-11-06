"""
ObjectiveCar - Drive or destroy a vehicle objective.
"""

from typing import Literal
from pydantic import Field
from .base import ObjectiveBase
from ..car import CarModel
from ..constants import RadarMarker


class ObjectiveCar(ObjectiveBase):
    """
    Car objective - Drive or destroy a vehicle.

    The player must either enter and drive a specific vehicle, or destroy it.
    The objective type is determined by the must_destroy field.
    Default text: "Go to the car and enter it."
    """

    # Objective type
    objective_type: Literal[1] = Field(1, description="Objective type (1 = Car)")

    # Vehicle properties
    car_id: CarModel = Field(526, description="Vehicle model ID (400-611)")
    color_primary: int = Field(0, description="Primary color ID (0-126, -1=random, see https://gta.fandom.com/wiki/Carcols.dat/GTASA)", ge=-1, le=126)
    color_secondary: int = Field(36, description="Secondary color ID (0-126, -1=random, see https://gta.fandom.com/wiki/Carcols.dat/GTASA)", ge=-1, le=126)
    health: int = Field(1000, description="Vehicle health (0-1000)", ge=0, le=1000)

    # Radar marker
    radar_marker: RadarMarker = Field(RadarMarker.BLUE, description="Radar marker color")

    immune_bullet: bool = Field(False, description="Vehicle immune to bullet damage")
    immune_explosion: bool = Field(False, description="Vehicle immune to explosions")
    immune_tyres: bool = Field(False, description="Tyres cannot be popped")
    immune_collision: bool = Field(False, description="Vehicle immune to collision damage")
    locked: bool = Field(False, description="Vehicle doors locked")
    handbraked: bool = Field(False, description="Handbrake engaged")
    must_destroy: bool = Field(False, description="Objective requires destroying this vehicle")

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
                "radar_marker": 2,
                "immune_bullet": False,
                "immune_explosion": False,
                "immune_tyres": False,
                "immune_collision": False,
                "locked": False,
                "handbraked": False,
                "must_destroy": False,
                "unused_1": 0,
                "unused_2": 0,
                "unused_3": 0,
                "unused_4": 0,
                "text": "Get into the car!"
            }
        }
