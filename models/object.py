"""
Object model for DYOM missions.

Represents static or dynamic objects in a DYOM mission.
Objects can be placed in the world, animated, or moved along paths.
"""

from enum import IntEnum
from pydantic import BaseModel, Field


class ObjectBehaviour(IntEnum):
    """Behavior types for objects.
        NONE = 0
        MOVE_APPROACHED = 1  # Displace when approached
        ANIMATE_SLOW = 2  # Move along path - slow
        ANIMATE_NORMAL = 3  # Move along path - medium
        ANIMATE_FAST = 4  # Move along path - fast
    """
    NONE = 0
    MOVE_APPROACHED = 1  # Displace when approached
    ANIMATE_SLOW = 2  # Move along path - slow
    ANIMATE_NORMAL = 3  # Move along path - medium
    ANIMATE_FAST = 4  # Move along path - fast


class Object(BaseModel):
    """
    A static or dynamic object in a DYOM mission.

    Objects are 3D models placed in the game world. They can be static decorations,
    or they can have behaviors like moving along paths or displacing when approached.
    Maximum 100 objects per mission.

    Note: The 'interior' field is a composite value that encodes both the interior ID
    and the behavior type using bit packing.
    """

    # Object model
    object_id: int = Field(..., description="Object model ID from GTA San Andreas", ge=0)

    # Position and rotation
    position_x: float = Field(..., description="X coordinate in game world")
    position_y: float = Field(..., description="Y coordinate in game world")
    position_z: float = Field(..., description="Z coordinate in game world (height)")
    rotation_x: float = Field(0.0, description="X-axis rotation in degrees", ge=0, le=360)
    rotation_y: float = Field(0.0, description="Y-axis rotation in degrees", ge=0, le=360)
    rotation_z: float = Field(0.0, description="Z-axis rotation in degrees", ge=0, le=360)

    # Interior and behavior (composite field)
    interior: int = Field(
        0,
        description=(
            "Composite bitfield combining interior ID and behavior: "
            "bits 0-2 encode interior ID (0-7), "
            "bits 6-8 encode behavior type from ObjectBehaviour enum "
            "(NONE=0, MOVE_APPROACHED=1, ANIMATE_SLOW=2, ANIMATE_NORMAL=3, ANIMATE_FAST=4). "
            "Formula: value = interior_id + (behaviour_id << 6). "
            "Example: interior_id=2, behavior=ANIMATE_NORMAL(3) → value = 2 + (3 << 6) = 2 + 192 = 194"
        ),
        ge=0
    )

    # Lifetime control
    spawn: int = Field(0, description="Objective number when object spawns (0 = mission start)", ge=0)
    despawn: int = Field(1000, description="Objective number when object despawns (1000 = never)", ge=0, le=1000)

    class Config:
        use_enum_values = True
        json_schema_extra = {
            "example": {
                "object_id": 1221,
                "position_x": 2495.0,
                "position_y": -1688.0,
                "position_z": 13.3,
                "rotation_x": 0.0,
                "rotation_y": 0.0,
                "rotation_z": 90.0,
                "interior": 0,
                "spawn": 0,
                "despawn": 1000
            }
        }
