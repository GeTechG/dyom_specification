"""
DYOM Mission File Specification Models

This package contains Pydantic models for DYOM (Design Your Own Mission) files.
"""

from .actor import Actor, Animation, Gang, ActorFlags
from .animation_info import AnimationInfo, VehicleSeat, DriverBehaviour
from .car import Car
from .constants import Weather, Weapon, Skin
from .object import Object, ObjectModel
from .pickup import Pickup, PickupBehaviour
from .route import Route, RouteType, RoutePoint, RouteEntry
from .mission import (
    Mission,
    MissionInfo,
    MissionFlags,
    PlayerInitial,
    InitialSettings,
    PathsCollection,
    AnyObjective,
)
from .objectives import (
    ObjectiveType,
    RadarMarker,
    ObjectiveActor,
    ObjectiveCar,
    ObjectiveCheckpoint,
    ObjectivePickup,
    ObjectiveCutscene,
    ObjectivePlayerTeleport,
    ObjectiveCountdown,
    ObjectivePlayerTeleportCar,
    ObjectiveTimeout,
    ObjectiveWeather,
    ObjectiveDayTime,
    ObjectiveCitizenBehaviour,
    ObjectiveWantedLevel,
    ObjectiveTimelimit,
    ObjectiveTimerStart,
    ObjectivePlayerDisarm,
    ObjectivePhoneCall,
    ObjectiveObject,
    ObjectiveMoneyAdd,
    ObjectiveMoneySub,
    ObjectivePlayerAnimation,
    CheckpointShape,
    CitizenBehaviourMode,
    ObjectObjectiveType,
)

__all__ = [
    # Constants
    "Weather",
    "Weapon",
    "Skin",
    "VehicleSeat",
    "DriverBehaviour",

    # Actor models
    "Actor",
    "Animation",
    "Gang",
    "ActorFlags",
    "AnimationInfo",

    # Car models
    "Car",

    # Object models
    "Object",
    "ObjectModel",

    # Pickup models
    "Pickup",
    "PickupBehaviour",

    # Route models
    "Route",
    "RouteType",
    "RoutePoint",
    "RouteEntry",

    # Mission models
    "Mission",
    "MissionInfo",
    "MissionFlags",
    "PlayerInitial",
    "InitialSettings",
    "PathsCollection",
    "AnyObjective",

    # Objective models
    "ObjectiveType",
    "RadarMarker",
    "ObjectiveActor",
    "ObjectiveCar",
    "ObjectiveCheckpoint",
    "ObjectivePickup",
    "ObjectiveCutscene",
    "ObjectivePlayerTeleport",
    "ObjectiveCountdown",
    "ObjectivePlayerTeleportCar",
    "ObjectiveTimeout",
    "ObjectiveWeather",
    "ObjectiveDayTime",
    "ObjectiveCitizenBehaviour",
    "ObjectiveWantedLevel",
    "ObjectiveTimelimit",
    "ObjectiveTimerStart",
    "ObjectivePlayerDisarm",
    "ObjectivePhoneCall",
    "ObjectiveObject",
    "ObjectiveMoneyAdd",
    "ObjectiveMoneySub",
    "ObjectivePlayerAnimation",
    "CheckpointShape",
    "CitizenBehaviourMode",
    "ObjectObjectiveType",
]
