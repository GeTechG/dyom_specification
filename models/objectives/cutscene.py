"""
ObjectiveCutscene - Camera cutscene objective.
"""

from typing import Literal
from enum import IntEnum
from pydantic import Field
from .base import ObjectiveBase


class CutsceneBehaviour(IntEnum):
    """Cutscene camera behavior modes."""
    STATIC = 0
    LINEAR = 1
    SMOOTH = 2
    ACTOR_FOLLOW = 3
    ACTOR_1ST_PERSON = 4
    ACTOR_3RD_PERSON = 5
    PLAYER_FOLLOW = 6
    PLAYER_1ST_PERSON = 7
    PLAYER_3RD_PERSON = 8
    MASK = 255
    SLOW_MOTION = 256
    CAMERA_SHAKING = 512
    SKIP_FADING = 1024
    SKIP_WIDESCREEN = 2048


class ObjectiveCutscene(ObjectiveBase):
    """
    Cutscene objective - Play a camera cutscene.

    Displays a cinematic camera sequence with various behaviors (static, moving, following actors/player).
    The camera can move from the position to the target position, or follow entities.

    The behaviour field is a composite bitfield:
    - Bits 0-7 (masked by 255): Camera behavior type (0-8)
    - Bit 8 (256): Slow motion effect
    - Bit 9 (512): Camera shaking effect
    - Bit 10 (1024): Skip fade in/out
    - Bit 11 (2048): Skip widescreen cinematic bars

    Default text: "" (no text displayed during cutscenes)
    """

    # Objective type
    objective_type: Literal[6] = Field(6, description="Objective type (6 = Cutscene)")

    # Camera position (start point)
    position_icon_z: float = Field(
        ...,
        description="Z coordinate for icon placement (usually same as position_z)"
    )

    # Camera target position (look-at point)
    target_position_x: float = Field(..., description="Target X coordinate in game world")
    target_position_y: float = Field(..., description="Target Y coordinate in game world")
    target_position_z: float = Field(..., description="Target Z coordinate in game world (height)")

    # Cutscene properties
    duration: int = Field(
        3000,
        description="Cutscene duration in milliseconds (e.g., 3000 = 3 seconds)",
        ge=0
    )

    # Behavior (composite bitfield)
    behaviour: int = Field(
        0,
        description=(
            "Cutscene behavior composite bitfield. "
            "Bits 0-7 (value & 255): Camera mode - "
            "0=Static, 1=Linear, 2=Smooth, 3=Actor follow, 4=Actor 1st person, 5=Actor 3rd person, "
            "6=Player follow, 7=Player 1st person, 8=Player 3rd person. "
            "Bit 8 (256): Slow motion. "
            "Bit 9 (512): Camera shaking. "
            "Bit 10 (1024): Skip fade in/out. "
            "Bit 11 (2048): Skip widescreen bars. "
            "Example: 258=Linear+Slow motion (1+256), 3=Actor follow"
        ),
        ge=0
    )

    # Actor reference (for actor-related behaviors)
    actor_idx: int = Field(
        0,
        description="Actor index (0-99) to follow/view when using actor-related behaviors (3, 4, 5)",
        ge=0,
        le=99
    )

    # Unused fields
    unused_1: int = Field(0, description="Unused field")
    unused_2: int = Field(0, description="Unused field")
    unused_3: int = Field(0, description="Unused field")
    unused_4: int = Field(0, description="Unused field")

    # Objective text
    text: str = Field("", description="Objective description text (typically empty for cutscenes)")

    class Config:
        use_enum_values = True
        json_schema_extra = {
            "example": {
                "position_x": 2495.0,
                "position_y": -1688.0,
                "position_z": 20.0,
                "position_icon_z": 20.0,
                "direction": 0.0,
                "interior": 0,
                "objective_type": 6,
                "target_position_x": 2500.0,
                "target_position_y": -1690.0,
                "target_position_z": 15.0,
                "duration": 3000,
                "behaviour": 2,  # CutsceneBehaviour.SMOOTH
                "actor_idx": 0,
                "unused_1": 0,
                "unused_2": 0,
                "unused_3": 0,
                "unused_4": 0,
                "text": ""
            }
        }
