"""
ObjectiveCitizenBehaviour - Control traffic and pedestrian behavior objective.
"""

from typing import Literal
from enum import IntEnum
from pydantic import Field
from .base import ObjectiveBase


class CitizenBehaviourMode(IntEnum):
    """Citizen behavior modes.
        NORMAL = 0
        RIOT = 1
        NO_CAR = 2
        NO_PED = 3
        NO_CAR_PED = 4
    """
    NORMAL = 0
    RIOT = 1
    NO_CAR = 2
    NO_PED = 3
    NO_CAR_PED = 4


class ObjectiveCitizenBehaviour(ObjectiveBase):
    """
    Citizen Behaviour objective - Control traffic and pedestrian spawning.

    Changes whether traffic cars and pedestrians spawn in the world, and whether
    they are in riot mode. Completes immediately.

    Mode values:
    - 0 (NORMAL): Normal traffic and pedestrians
    - 1 (RIOT): Riot mode with traffic and pedestrians (chaos)
    - 2 (NO_CAR): Pedestrians only, no traffic
    - 3 (NO_PED): Traffic only, no pedestrians
    - 4 (NO_CAR_PED): Empty streets, no traffic or pedestrians

    Note: This objective does not use interior ID or position fields meaningfully.

    Default text: "" (no text, instant change)
    """

    # Objective type
    objective_type: Literal[13] = Field(13, description="Objective type (13 = Citizen Behaviour)")

    # Behavior mode
    mode: CitizenBehaviourMode = Field(
        CitizenBehaviourMode.NORMAL,
        description="Citizen behavior mode (0=Normal, 1=Riot, 2=No cars, 3=No peds, 4=Empty)"
    )

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
                "objective_type": 13,
                "mode": 4,  # CitizenBehaviourMode.NO_CAR_PED
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
