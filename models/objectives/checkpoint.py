"""
ObjectiveCheckpoint - Reach a location marker objective.
"""

from typing import Literal
from enum import IntEnum
from pydantic import Field
from .base import ObjectiveBase


class CheckpointShape(IntEnum):
    """Checkpoint visual shapes.
        CAMPFIRE = 0
        BEACON_ARROW = 1
        BEACON_FINISH = 2
        BEACON = 3
        RING = 4
        INVISIBLE = 5
    """
    CAMPFIRE = 0
    BEACON_ARROW = 1
    BEACON_FINISH = 2
    BEACON = 3
    RING = 4
    INVISIBLE = 5


class ObjectiveCheckpoint(ObjectiveBase):
    """
    Checkpoint objective - Reach a location marker.

    The player must reach a specific location marked by various visual indicators.
    Can be configured with different shapes (beacon, ring, invisible, etc.) and sizes.
    Default text: "Go to the next checkpoint."

    Note: The radius field is stored in the position that would normally be 'direction' in other objectives.
    The actual direction field is at the end (for arrow/ring rotation).
    """

    # Objective type
    objective_type: Literal[2] = Field(2, description="Objective type (2 = Checkpoint)")

    # Checkpoint properties (note: radius replaces direction in the base position)
    radius: float = Field(2.0, description="Checkpoint radius in meters (diameter = radius * 2, range: 0.2-6000.0)", ge=0.2, le=6000.0)

    # Visual appearance
    shape: CheckpointShape = Field(
        CheckpointShape.CAMPFIRE,
        description="Visual shape of the checkpoint (0=Campfire, 1=Beacon with arrow, 2=Beacon with finish flag, 3=Beacon, 4=Ring, 5=Invisible)"
    )

    # Radar marker
    radar_marker: int = Field(
        4,
        description="Radar marker color ID (-1=None, 0=Red, 1=Green, 2=Blue, 3=White, 4=Yellow, or custom RGB encoded as int)"
    )

    # Direction (for arrow/ring orientation)
    direction: float = Field(0.0, description="Rotation for arrow/ring shapes in degrees (0-360, stored as negative value internally)", ge=0, le=360)

    # Unknown/unused fields
    unknown_1: int = Field(0, description="Unknown field")
    unused_1: int = Field(0, description="Unused field")
    unused_2: int = Field(0, description="Unused field")
    unused_3: int = Field(0, description="Unused field")
    unused_4: int = Field(0, description="Unused field")
    unused_5: int = Field(0, description="Unused field")
    unused_6: int = Field(0, description="Unused field")

    # Objective text
    text: str = Field("", description="Objective description text shown to player")

    class Config:
        use_enum_values = True
        json_schema_extra = {
            "example": {
                "position_x": 2495.0,
                "position_y": -1688.0,
                "position_z": 13.3,
                "radius": 2.0,
                "interior": 0,
                "objective_type": 2,
                "shape": 3,  # CheckpointShape.BEACON
                "unknown_1": 0,
                "radar_marker": 4,  # RadarMarker.YELLOW
                "direction": 0.0,
                "unused_1": 0,
                "unused_2": 0,
                "unused_3": 0,
                "unused_4": 0,
                "unused_5": 0,
                "unused_6": 0,
                "text": "Go to the marker!"
            }
        }
