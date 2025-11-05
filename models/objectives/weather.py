"""
ObjectiveWeather - Change weather objective.
"""

from typing import Literal
from pydantic import Field
from .base import ObjectiveBase
from .. import Weather


class ObjectiveWeather(ObjectiveBase):
    """
    Weather objective - Change the game weather.

    Instantly changes the weather conditions. Completes immediately.

    Note: This objective does not use interior ID or position fields meaningfully.

    Default text: "" (no text, instant change)
    """

    # Objective type
    objective_type: Literal[11] = Field(11, description="Objective type (11 = Weather)")

    # Weather configuration
    weather: Weather = Field(Weather.SUNNY_HEAT_CLEAR, description="Weather type. See Weather enum for all available options.")

    # Unused fields
    unused_1: float = Field(0.0, description="Unused field (float)")
    unused_2: int = Field(0, description="Unused field")
    unused_3: int = Field(0, description="Unused field")
    unused_4: int = Field(0, description="Unused field")
    unused_5: int = Field(0, description="Unused field")
    unused_6: int = Field(0, description="Unused field")
    unused_7: int = Field(0, description="Unused field")
    unused_8: int = Field(0, description="Unused field")
    unused_9: int = Field(0, description="Unused field")
    unused_10: int = Field(0, description="Unused field")
    unused_11: str = Field("", description="Unused field (string)")

    class Config:
        use_enum_values = True
        json_schema_extra = {
            "example": {
                "position_x": 0.0,
                "position_y": 0.0,
                "position_z": 0.0,
                "direction": 0.0,
                "interior": 0,
                "objective_type": 11,
                "weather_id": 9,
                "unused_1": 0.0,
                "unused_2": 0,
                "unused_3": 0,
                "unused_4": 0,
                "unused_5": 0,
                "unused_6": 0,
                "unused_7": 0,
                "unused_8": 0,
                "unused_9": 0,
                "unused_10": 0,
                "unused_11": ""
            }
        }
