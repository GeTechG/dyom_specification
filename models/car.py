"""
Car model for DYOM missions.

Represents vehicles in a DYOM mission, including their model, colors, health,
and behavior settings.
"""

from enum import IntEnum
from typing import Annotated

from pydantic import BaseModel, Field, RootModel

CarModelType = Annotated[int, Field(ge=400, le=611)]

class CarModel(RootModel[CarModelType]):
    root: CarModelType

    model_config = {
        'json_schema_extra': {
            'type': 'integer',
            'description': """Vehicle model ID (400-611)

            - 400 = Landstal
            - 401 = Bravura
            - 402 = Buffalo
            - 403 = Linerun
            - 404 = Perennial
            - 405 = Sentinel
            - 406 = Dumper
            - 407 = Firetruck
            - 408 = Trash
            - 409 = Stretch
            - 410 = Manana
            - 411 = Infernus
            - 412 = Voodoo
            - 413 = Pony
            - 414 = Mule
            - 415 = Cheetah
            - 416 = Ambulance
            - 417 = Leviathn
            - 418 = Moonbeam
            - 419 = Esperanto
            - 420 = Taxi
            - 421 = Washington
            - 422 = Bobcat
            - 423 = Mr Whoopy
            - 424 = Bf Injection
            - 425 = Hunter
            - 426 = Premier
            - 427 = Enforcer
            - 428 = Securicar
            - 429 = Banshee
            - 430 = Predator
            - 431 = Bus
            - 432 = Rhino
            - 433 = Barracks
            - 434 = Hotknife
            - 435 = Artict1
            - 436 = Previon
            - 437 = Coach
            - 438 = Cabbie
            - 439 = Stallion
            - 440 = Rumpo
            - 441 = RC Bandit
            - 442 = Romero
            - 443 = Packer
            - 444 = Monster
            - 445 = Admiral
            - 446 = Squalo
            - 447 = Seaspar
            - 448 = Pizzaboy
            - 449 = Tram
            - 450 = Artict2
            - 451 = Turismo
            - 452 = Speeder
            - 453 = Reefer
            - 454 = Tropic
            - 455 = Flatbed
            - 456 = Yankee
            - 457 = Caddy
            - 458 = Solair
            - 459 = Topfun
            - 460 = Skimmer
            - 461 = - PCJ=600
            - 462 = Faggio
            - 463 = Freeway
            - 464 = RC Baron
            - 465 = RC Raider
            - 466 = Glendale
            - 467 = Oceanic
            - 468 = Sanchez
            - 469 = Sparrow
            - 470 = Patriot
            - 471 = Quad
            - 472 = Coastg
            - 473 = Dinghy
            - 474 = Hermes
            - 475 = Sabre
            - 476 = Rustler
            - 477 = ZR 350
            - 478 = Walton
            - 479 = Regina
            - 480 = Comet
            - 481 = BMX
            - 482 = Burrito
            - 483 = Camper
            - 484 = Marquis
            - 485 = Baggage
            - 486 = Dozer
            - 487 = Maverick
            - 488 = Maverick News
            - 489 = Rancher
            - 490 = FBI Rancher
            - 491 = Virgo
            - 492 = Greenwood
            - 493 = Jetmax
            - 494 = Hotring
            - 495 = Sandking
            - 496 = Blista Compact
            - 497 = Maverick Police
            - 498 = Boxville
            - 499 = Benson
            - 500 = Mesa
            - 501 = RC Goblin
            - 502 = Hotring A
            - 503 = Hotring B
            - 504 = Bloodring Banger
            - 505 = Rancher Lure
            - 506 = Super GT
            - 507 = Elegant
            - 508 = Journey
            - 509 = Bike
            - 510 = Mountain Bike
            - 511 = Beagle
            - 512 = Cropduster
            - 513 = Stunt
            - 514 = Petro
            - 515 = Roadtrain
            - 516 = Nebula
            - 517 = Majestic
            - 518 = Buccanee
            - 519 = Shamal
            - 520 = Hydra
            - 521 = - FCR=900
            - 522 = - NRG=500
            - 523 = Police Bike
            - 524 = Cement
            - 525 = Towtruck
            - 526 = Fortune
            - 527 = Cadrona
            - 528 = FBI Truck
            - 529 = Willard
            - 530 = Forklift
            - 531 = Tractor
            - 532 = Combine
            - 533 = Feltzer
            - 534 = Remington
            - 535 = Slamvan
            - 536 = Blade
            - 537 = Freight
            - 538 = Streak
            - 539 = Vortex
            - 540 = Vincent
            - 541 = Bullet
            - 542 = Clover
            - 543 = Sadler
            - 544 = Firetruck LA
            - 545 = Hustler
            - 546 = Intruder
            - 547 = Primo
            - 548 = Cargobob
            - 549 = Tampa
            - 550 = Sunrise
            - 551 = Merit
            - 552 = Utility
            - 553 = Nevada
            - 554 = Yosemite
            - 555 = Windsor
            - 556 = Monster A
            - 557 = Monster B
            - 558 = Uranus
            - 559 = Jester
            - 560 = Sultan
            - 561 = Stratum
            - 562 = Elegy
            - 563 = Raindanc
            - 564 = RC Tiger
            - 565 = Flash
            - 566 = Tahoma
            - 567 = Savanna
            - 568 = Bandito
            - 569 = Freiflat
            - 570 = Streakc
            - 571 = Kart
            - 572 = Mower
            - 573 = Duneride
            - 574 = Sweeper
            - 575 = Broadway
            - 576 = Tornado
            - 577 = - AT=400
            - 578 = - DFT=30
            - 579 = Huntley
            - 580 = Stafford
            - 581 = - BF=400
            - 582 = News Van
            - 583 = Tug
            - 584 = Petrotr
            - 585 = Emperor
            - 586 = Wayfarer
            - 587 = Euros
            - 588 = Hotdog
            - 589 = Club
            - 590 = Freibox
            - 591 = Artict3
            - 592 = Androm
            - 593 = Dodo
            - 594 = RC Cam
            - 595 = Launch
            - 596 = Police LA
            - 597 = Police SF
            - 598 = Police LV
            - 599 = Police Ranger
            - 600 = Picador
            - 601 = Police SWAT
            - 602 = Alpha
            - 603 = Phoenix
            - 604 = Glenshit
            - 605 = Sadlshit
            - 606 = Bagbox A
            - 607 = Bagbox B
            - 608 = Tugstair
            - 609 = Boxville Mission
            - 610 = Farm Trailer
            - 611 = Utility trailer
            """
        }
    }

class Car(BaseModel):
    """
    A vehicle in a DYOM mission.

    Vehicles can be cars, bikes, boats, planes, helicopters, and other vehicle types.
    Maximum 50 vehicles per mission.
    """

    # Vehicle model and appearance
    car_id: CarModel = Field(..., description="Vehicle model ID (400-611)")
    color_primary: int = Field(..., description="Primary color ID (0-126, see https://gta.fandom.com/wiki/Carcols.dat/GTASA)", ge=0, le=126)
    color_secondary: int = Field(..., description="Secondary color ID (0-126, see https://gta.fandom.com/wiki/Carcols.dat/GTASA)", ge=0, le=126)

    # Position and orientation
    position_x: float = Field(..., description="X coordinate in game world")
    position_y: float = Field(..., description="Y coordinate in game world")
    position_z: float = Field(..., description="Z coordinate in game world (height)")
    direction: float = Field(0.0, description="Facing direction in degrees (0-360)", ge=0, le=360)
    interior: int = Field(0, description="Interior ID (0 = outdoor)", ge=0)

    # Vehicle state
    health: int = Field(1000, description="Vehicle health (0-1000+)", ge=0)
    immune_bullet: bool = Field(False, description="Vehicle immune to bullet damage")
    immune_explosion: bool = Field(False, description="Vehicle immune to explosions")
    immune_tyres: bool = Field(False, description="Tyres cannot be popped")
    immune_collision: bool = Field(False, description="Vehicle immune to collision damage")
    locked: bool = Field(False, description="Vehicle doors locked")
    handbraked: bool = Field(False, description="Handbrake engaged")
    must_destroy: bool = Field(False, description="Objective requires destroying this vehicle")
    driveby: bool = Field(False, description="Enable drive-by shooting")

    # Lifetime control
    spawn: int = Field(0, description="Objective number when vehicle spawns (0 = mission start)", ge=0)
    despawn: int = Field(1000, description="Objective number when vehicle despawns (1000 = never)", ge=0, le=1000)
    must_survive: int = Field(0, description="If 1, mission fails if vehicle is destroyed", ge=0, le=1)

    class Config:
        use_enum_values = True
        json_schema_extra = {
            "example": {
                "car_id": 560,
                "color_primary": 6,
                "color_secondary": 1,
                "position_x": 2495.0,
                "position_y": -1688.0,
                "position_z": 13.3,
                "direction": 90.0,
                "interior": 0,
                "health": 1000,
                "immune_bullet": False,
                "immune_explosion": False,
                "immune_tyres": False,
                "immune_collision": False,
                "locked": False,
                "handbraked": False,
                "must_destroy": False,
                "driveby": False,
                "spawn": 0,
                "despawn": 1000,
                "must_survive": 0
            }
        }
