"""
Object model for DYOM missions.

Represents static or dynamic objects in a DYOM mission.
Objects can be placed in the world, animated, or moved along paths.
"""

from enum import IntEnum
from typing import Annotated
from pydantic import BaseModel, Field, RootModel


ObjectModelType = Annotated[int, Field(ge=-467)]


class ObjectModel(RootModel[ObjectModelType]):
    root: ObjectModelType

    model_config = {
        'json_schema_extra': {
            'type': 'integer',
            'description': """Object model ID from GTA San Andreas (standard objects >= 0, effects < 0)

            Effect Objects (negative IDs):
            - -15 = Explosion Old Style
            - -16 = Fire
            - -388 = blood_heli
            - -389 = camflash
            - -390 = coke_puff
            - -391 = explosion_crate
            - -392 = explosion_door
            - -393 = exhale
            - -394 = gunflash
            - -395 = gunsmoke
            - -396 = puke
            - -397 = riot_smoke
            - -398 = shootlight
            - -399 = tank_fire
            - -400 = tree_hit_fir
            - -401 = tree_hit_palm
            - -402 = water_hydrant
            - -403 = water_splash
            - -404 = water_splash_big
            - -405 = water_splsh_sml
            - -406 = water_swim
            - -407 = wallbust
            - -408 = boat_prop
            - -409 = carwashspray
            - -410 = cement
            - -411 = cloudfast
            - -412 = coke_trail
            - -413 = cigarette_smoke
            - -414 = extinguisher
            - -415 = flame
            - -416 = fire
            - -417 = fire_med
            - -418 = fire_large
            - -419 = flamethrower
            - -420 = fire_bike
            - -421 = fire_car
            - -422 = insects
            - -423 = heli_dust
            - -424 = jetpack
            - -425 = jetthrust
            - -426 = nitro
            - -427 = molotov_flame
            - -428 = overheat_car
            - -429 = prt_boatsplash
            - -430 = prt_gunshell
            - -431 = prt_sand
            - -432 = prt_sand2
            - -433 = prt_smoke_huge
            - -434 = prt_spark
            - -435 = prt_spark_2
            - -436 = prt_splash
            - -437 = prt_watersplash
            - -438 = prt_wheeldirt
            - -439 = petrolcan
            - -440 = spraycan
            - -441 = smoke30lit
            - -442 = smoke30m
            - -443 = smoke50lit
            - -444 = smoke_flare
            - -445 = teargas
            - -446 = teargasAD
            - -447 = vent
            - -448 = vent2
            - -449 = water_ripples
            - -450 = water_speed
            - -451 = waterfall_end
            - -452 = water_fnt_tme
            - -453 = water_fountain
            - -454 = WS_factorysmoke
            - -455 = Explosion 0
            - -456 = Explosion 1
            - -457 = Explosion 2
            - -458 = Explosion 3
            - -459 = Explosion 4
            - -460 = Explosion 5
            - -461 = Explosion 6
            - -462 = Explosion 7
            - -463 = Explosion 8
            - -464 = Explosion 9
            - -465 = Explosion 10
            - -466 = Explosion 11
            - -467 = Explosion 12

            Standard objects use positive IDs (0 and above).
            See GTA San Andreas object database for standard object IDs.
            """
        }
    }


class Object(BaseModel):
    """
    A static or dynamic object in a DYOM mission.

    Objects are 3D models placed in the game world. They can be static decorations,
    or they can have behaviors like moving along paths or displacing when approached.
    Maximum 100 objects per mission.
    """

    # Object model
    object_id: ObjectModel = Field(..., description="Object model ID from GTA San Andreas (standard objects >= 0, effects < 0)")

    # Position and rotation
    position_x: float = Field(..., description="X coordinate in game world")
    position_y: float = Field(..., description="Y coordinate in game world")
    position_z: float = Field(..., description="Z coordinate in game world (height)")
    rotation_x: float = Field(0.0, description="X-axis rotation in degrees")
    rotation_y: float = Field(0.0, description="Y-axis rotation in degrees")
    rotation_z: float = Field(0.0, description="Z-axis rotation in degrees")

    interior: int = Field(0, description="Interior ID (0-7, 0 = outdoor)", ge=0, le=7)
    behaviour: int | None = Field(
        None,
        description=(
            "Object behavior type: "
            "0 or None = None (static object), "
            "1 = Displace when approached, "
            "2 = Move along path - slow, "
            "3 = Move along path - medium, "
            "4 = Move along path - fast"
        ),
        ge=0,
        le=4
    )
    route_id: int | None = Field(
        None,
        description="Route ID for objects with behavior 1-4 (displacement or movement along path)",
        ge=1
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
                "behaviour": None,
                "route_id": None,
                "spawn": 0,
                "despawn": 1000
            }
        }
