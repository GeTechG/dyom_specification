"""
ObjectivePlayerTeleportCar - Teleport player into a vehicle objective.
"""

from typing import Literal
from pydantic import Field
from .base import ObjectiveBase
from ..car import CarModel
from ..constants import RadarMarker


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
    car_id: CarModel = Field(..., description="Vehicle model ID (400-611)")
    color_primary: int = Field(...,
                               description="Primary color ID (0-126, see https://gta.fandom.com/wiki/Carcols.dat/GTASA)",
                               ge=0, le=126)
    color_secondary: int = Field(...,
                                 description="Secondary color ID (0-126, see https://gta.fandom.com/wiki/Carcols.dat/GTASA)",
                                 ge=0, le=126)
    health: int = Field(1000, description="Vehicle health (0-1000)")

    # Seat position
    seat: int = Field(
        0,
        description="Vehicle seat to place player in (0=Driver, 1=Passenger, 2=Rear left, 3=Rear right)",
        ge=0,
        le=3
    )

    # Radar marker
    radar_marker: RadarMarker = Field(RadarMarker.NONE, description="Radar marker color")

    immune_bullet: bool = Field(False, description="Vehicle is immune to bullets")
    immune_explosion: bool = Field(False, description="Vehicle is immune to explosions")
    immune_tyres: bool = Field(False, description="Vehicle tyres cannot be popped")
    immune_collision: bool = Field(False, description="Vehicle is immune to collision damage")
    locked: bool = Field(False, description="Vehicle doors are locked")
    handbraked: bool = Field(False, description="Vehicle handbrake is engaged")
    must_destroy: bool = Field(False, description="Vehicle must be destroyed (mission requirement)")
    driveby: bool = Field(False, description="Enable driveby mode for the vehicle")

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
                "immune_bullet": False,
                "immune_explosion": False,
                "immune_tyres": False,
                "immune_collision": False,
                "locked": False,
                "handbraked": False,
                "must_destroy": False,
                "driveby": False,
                "unused_1": 0,
                "unused_2": 0,
                "unused_3": 0,
                "text": ""
            }
        }
