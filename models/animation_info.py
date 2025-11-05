"""
Animation info model for DYOM actors.

Represents additional animation parameters that depend on the animation type,
such as route references for movement animations or vehicle seat assignments.
"""

from __future__ import annotations
from typing import Optional
from enum import IntEnum
from pydantic import BaseModel, Field


class VehicleSeat(IntEnum):
    """Vehicle seat positions for actors entering/sitting in vehicles."""
    DRIVER = 0
    PASSENGER = 1
    REAR_LEFT = 2
    REAR_RIGHT = 3


class DriverBehaviour(IntEnum):
    """Driving behavior modes for actors in driver seat."""
    NONE = 0           # Do nothing
    ROUTE_SLOW = 1     # Drive route - slow
    ROUTE_NORMAL = 2   # Drive route - normal
    ROUTE_FAST = 3     # Drive route - aggressive
    ATTACK_PLAYER = 4  # Attack player
    FOLLOW_PLAYER = 5  # Follow player


class AnimationInfo(BaseModel):
    """
    Additional animation parameters for actor animations.

    These fields are only populated based on the animation type:
    - Route: Used for movement animations (walk, run, sprint, crouch walk, multiple locations)
    - VehicleSeat: Used for vehicle animations (enter, sit, exit)
    - DriverBehaviour: Used when VehicleSeat is DRIVER

    Note: Fields are serialized with PascalCase names to match the C# implementation.
    """

    route: int = Field(
        None,
        description=(
            "Route ID for movement animations. "
            "Used with animations: Walk (-2), Crouch walk (-10), Run (-3), Sprint (-9), Multiple locations (-11)"
        ),
        ge=0
    )

    vehicle_seat: Optional[VehicleSeat] = Field(
        None,
        description=(
            "Vehicle seat position. "
            "Used with animations: Enter vehicle (-4), Sit in vehicle (-6), Exit vehicle (-5)"
        )
    )

    driver_behaviour: Optional[DriverBehaviour] = Field(
        None,
        description=(
            "Driving behavior when VehicleSeat is DRIVER. "
            "Specifies how the actor should behave while driving"
        )
    )

    class Config:
        use_enum_values = True