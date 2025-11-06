"""
ObjectivePickup - Collect a pickup objective.
"""

from typing import Literal
from pydantic import Field
from .base import ObjectiveBase
from ..object import ObjectModel
from ..constants import RadarMarker


class ObjectivePickup(ObjectiveBase):
    """
    Pickup objective - Collect a pickup item.

    The player must collect a specific pickup item (weapon, health, armor, etc.).
    Can be configured to require collecting all pickups with the same object ID,
    or display a counter showing collection progress.
    Default text: "Get the pickup."
    """

    # Objective type
    objective_type: Literal[3] = Field(3, description="Objective type (3 = Pickup)")

    # Pickup properties
    object_id: ObjectModel = Field(
        1210,
        description="Pickup object ID from GTA San Andreas"
    )
    ammo: int = Field(0, description="Ammunition count for weapon pickups", ge=0)

    # Radar marker
    radar_marker: RadarMarker = Field(RadarMarker.GREEN, description="Radar marker color")

    collect_all: bool = Field(False, description="Player must collect all pickups with this object_id")
    counter: bool = Field(False, description="Show collection counter on screen")

    # Unused fields (note: unused_1 is a float in the file structure)
    unused_1: float = Field(0.0, description="Unused field (float)")
    unused_2: int = Field(0, description="Unused field")
    unused_3: int = Field(0, description="Unused field")
    unused_4: int = Field(0, description="Unused field")
    unused_5: int = Field(0, description="Unused field")
    unused_6: int = Field(0, description="Unused field")
    unused_7: float = Field(0.0, description="Unused field (float)")

    # Objective text
    text: str = Field("", description="Objective description text shown to player")

    class Config:
        use_enum_values = True
        json_schema_extra = {
            "example": {
                "position_x": 2495.0,
                "position_y": -1688.0,
                "position_z": 13.3,
                "direction": 0.0,
                "interior": 0,
                "objective_type": 3,
                "object_id": 1240,
                "ammo": 0,
                "radar_marker": 1,
                "collect_all": False,
                "counter": False,
                "unused_1": 0.0,
                "unused_2": 0,
                "unused_3": 0,
                "unused_4": 0,
                "unused_5": 0,
                "unused_6": 0,
                "unused_7": 0.0,
                "text": "Collect the health pickup!"
            }
        }
