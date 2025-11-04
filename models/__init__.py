"""
DYOM Mission File Specification Models

This package contains Pydantic models for DYOM (Design Your Own Mission) files.
"""

from .actor import Actor, Animation, VehicleSeat, DriverBehaviour, Gang, ActorFlags
from .car import Car, CarFlags
from .object import Object, ObjectBehaviour
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
    PickupObjectiveFlags,
    CutsceneBehaviour,
    CitizenBehaviourMode,
    ObjectObjectiveType,
)

__all__ = [
    # Actor models
    "Actor",
    "Animation",
    "VehicleSeat",
    "DriverBehaviour",
    "Gang",
    "ActorFlags",

    # Car models
    "Car",
    "CarFlags",

    # Object models
    "Object",
    "ObjectBehaviour",

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
    "PickupObjectiveFlags",
    "CutsceneBehaviour",
    "CitizenBehaviourMode",
    "ObjectObjectiveType",
]
