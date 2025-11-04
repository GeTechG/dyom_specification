"""
Base classes and enums for DYOM objectives.

This module contains the base objective class and common enumerations
used across different objective types.
"""

from enum import IntEnum
from pydantic import BaseModel, Field


class ObjectiveType(IntEnum):
    """Types of objectives available in DYOM missions.
        CAR = 1
        CHECKPOINT = 2
        PICKUP = 3
        UNUSED = 4
        ACTOR = 5
        CUTSCENE = 6
        PLAYER_TELEPORT = 7
        COUNTDOWN = 8
        PLAYER_TELEPORT_CAR = 9
        TIMEOUT = 10
        WEATHER = 11
        DAYTIME = 12
        CITIZEN_BEHAVIOUR = 13
        WANTED_LEVEL = 14
        TIMELIMIT = 15
        START_TIMER = 16
        PLAYER_DISARM = 17
        PHONE_CALL = 18
        OBJECT = 19
        MONEY_ADD = 20
        MONEY_SUB = 21
        PLAYER_ANIMATION = 22
    """
    CAR = 1
    CHECKPOINT = 2
    PICKUP = 3
    UNUSED = 4
    ACTOR = 5
    CUTSCENE = 6
    PLAYER_TELEPORT = 7
    COUNTDOWN = 8
    PLAYER_TELEPORT_CAR = 9
    TIMEOUT = 10
    WEATHER = 11
    DAYTIME = 12
    CITIZEN_BEHAVIOUR = 13
    WANTED_LEVEL = 14
    TIMELIMIT = 15
    START_TIMER = 16
    PLAYER_DISARM = 17
    PHONE_CALL = 18
    OBJECT = 19
    MONEY_ADD = 20
    MONEY_SUB = 21
    PLAYER_ANIMATION = 22


class RadarMarker(IntEnum):
    """Radar marker colors for objectives.
        NONE = -1
        RED = 0
        GREEN = 1
        BLUE = 2
        WHITE = 3
        YELLOW = 4
    """
    NONE = -1
    RED = 0
    GREEN = 1
    BLUE = 2
    WHITE = 3
    YELLOW = 4


class ObjectiveBase(BaseModel):
    """Base fields shared by all objective types."""

    # Position and orientation
    position_x: float = Field(..., description="X coordinate in game world")
    position_y: float = Field(..., description="Y coordinate in game world")
    position_z: float = Field(..., description="Z coordinate in game world (height)")
    direction: float = Field(0.0, description="Facing direction in degrees (0-360)", ge=0, le=360)
    interior: int = Field(0, description="Interior ID (0 = outdoor)", ge=0)

    # Objective identification
    objective_type: int = Field(..., description="Objective type identifier from ObjectiveType enum")

    class Config:
        use_enum_values = True
