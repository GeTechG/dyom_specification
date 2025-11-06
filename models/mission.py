"""
Mission model for DYOM missions.

This is the root structure that contains all mission data including metadata,
initial settings, entities (actors, cars, objects, pickups), objectives, and routes.
"""

from typing import List, Union
from enum import IntEnum
from pydantic import BaseModel, Field

from .constants import Weather, Weapon, Skin
from .actor import Actor
from .car import Car
from .object import Object
from .pickup import Pickup
from .route import Route
from .objectives import (
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
)


class MissionInfo(BaseModel):
    """
    Basic mission metadata and information.

    Contains the mission name, author, intro text, and audio settings.
    """
    name: str = Field(..., description="Mission name (max 50 characters)", max_length=50)
    author: str = Field(..., description="Author name (max 50 characters)", max_length=50)
    intro_text_1: str = Field("", description="First line of intro text", max_length=100)
    intro_text_2: str = Field("", description="Second line of intro text", max_length=100)
    intro_text_3: str = Field("", description="Third line of intro text", max_length=100)
    sound_filename: str = Field("", description="Custom audio filename path (format: SD/XXXXX/xx.mp3)")
    published: bool = Field(False, description="Whether mission is read-only/published")


class PlayerInitial(BaseModel):
    """
    Initial player state at mission start.

    Defines player spawn location, appearance, and equipment.
    """
    interior: int = Field(0, description="Interior ID (0 = outdoor)", ge=0)
    position_x: float = Field(2488.56, description="X coordinate in game world")
    position_y: float = Field(-1666.84, description="Y coordinate in game world")
    position_z: float = Field(12.38, description="Z coordinate in game world (height)")
    direction: float = Field(0.0, description="Facing direction in degrees (0-360)", ge=0, le=360)
    skin: Skin = Field(0, description="Player skin/character model ID")
    health: int = Field(100, description="Player health percentage (0-200)", ge=0)
    weapon: Weapon = Field(0, description="Player starting weapon ID", ge=0)
    ammo: int = Field(1000000, description="Starting ammunition count", ge=0)


class InitialSettings(BaseModel):
    """
    Initial mission settings and environment.

    Defines time, weather, wanted level, and global mission parameters.
    """
    timelimit: int = Field(0, description="Overall mission time limit in milliseconds (0 = no limit)", ge=0)
    day_time: int = Field(8, description="Starting hour of day (0-23)", ge=0, le=23)
    weather: Weather = Field(Weather.SUNNY_HEAT_CLEAR, description="Weather type. See Weather enum for all available options.")
    wanted_level_min: int = Field(0, description="Minimum wanted level (0-6)", ge=0, le=6)
    wanted_level_max: int = Field(6, description="Maximum wanted level (0-6)", ge=0, le=6)

    riot: bool = Field(False, description="Enable riot mode in Los Santos")
    timed: bool = Field(False, description="Enable mission timer display")

    player: PlayerInitial = Field(default_factory=PlayerInitial, description="Player initial state")


class PathsCollection(BaseModel):
    """
    Collection of all path/route types in the mission.

    Routes are paths that actors or vehicles follow sequentially.
    Movements are object movement paths.
    Displacements are object movement animations from initial position to new position when triggered.
    """
    routes: List[Route] = Field(default_factory=list, description="Actor/vehicle movement paths - entities follow waypoints")
    movements: List[Route] = Field(default_factory=list, description="Object movement paths")
    displacements: List[Route] = Field(default_factory=list, description="Object displacement paths - objects move to new position when triggered (uses duration field)")


# Union type for all objective types - discriminated by objective_type field
AnyObjective = Union[
    ObjectiveCar,
    ObjectiveCheckpoint,
    ObjectivePickup,
    ObjectiveActor,
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
]


class Mission(BaseModel):
    """
    Complete DYOM mission structure.

    This is the root object that contains all mission data:
    - Mission metadata (name, author, intro text)
    - Initial settings (time, weather, player state)
    - All entities (actors, cars, objects, pickups)
    - All objectives that define mission progression
    - All routes/paths for movement and cutscenes

    Maximum limits:
    - Objectives: 100
    - Actors: 100
    - Cars: 50
    - Pickups: 50
    - Objects: 50
    - Route points: 399
    """

    mission: MissionInfo = Field(..., description="Mission metadata and information")
    initial: InitialSettings = Field(default_factory=InitialSettings, description="Initial mission settings")

    # Entity lists
    objectives: List[AnyObjective] = Field(default_factory=list, description="Mission objectives - tasks player must complete (max 100)")
    actors: List[Actor] = Field(default_factory=list, description="NPCs/pedestrians (max 100)")
    cars: List[Car] = Field(default_factory=list, description="Vehicles (max 50)")
    pickups: List[Pickup] = Field(default_factory=list, description="Pickups/collectibles (max 50)")
    objects: List[Object] = Field(default_factory=list, description="Static objects (max 100)")

    # Paths
    paths: PathsCollection = Field(default_factory=PathsCollection, description="All routes and paths")

    class Config:
        json_schema_extra = {
            "example": {
                "mission": {
                    "name": "My Mission",
                    "author": "Mission Creator",
                    "intro_text_1": "Welcome to my mission",
                    "intro_text_2": "Get ready for action",
                    "intro_text_3": "",
                    "sound_filename": "",
                    "published": False
                },
                "initial": {
                    "timelimit": 0,
                    "day_time": 12,
                    "weather": 0,
                    "wanted_level_min": 0,
                    "wanted_level_max": 6,
                    "riot": False,
                    "timed": False,
                    "player": {
                        "interior": 0,
                        "position_x": 2488.56,
                        "position_y": -1666.84,
                        "position_z": 12.38,
                        "direction": 0.0,
                        "skin": 0,
                        "health": 100,
                        "weapon": 0,
                        "ammo": 1000000
                    }
                },
                "objectives": [],
                "actors": [],
                "cars": [],
                "pickups": [],
                "objects": [],
                "paths": {
                    "routes": [],
                    "movements": [],
                    "displacements": []
                }
            }
        }
