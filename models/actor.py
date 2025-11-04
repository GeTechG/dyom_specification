"""
Actor model for DYOM missions.

Represents NPCs/pedestrians in a DYOM mission, including their appearance, behavior,
weapons, animations, and AI settings.
"""

from typing import Optional
from enum import IntEnum
from pydantic import BaseModel, Field


class Animation(IntEnum):
    """Actor animation types. Special animations (negative values) and custom animations (0-129).

    Special animations:
        -12 = Aiming current gun
        -11 = Multiple locations
        -10 = Crouch walk
        -9 = Sprint
        -8 = Jump forward
        -7 = Die
        -6 = Be in nearest vehicle
        -5 = Leave nearest vehicle
        -4 = Enter nearest vehicle
        -3 = Run
        -2 = Walk
        -1 = No animation

    Custom animations (0-129):
        0 = Holding long gun
        1 = Talking with hand gestures
        2 = Rise hand "Watch what are you doing!"
        3 = Leaning front against counter, works with hands
        4 = Crouching on one knee
        5 = Sitting still, hands together
        6 = Talking explaining himself, handing something
        7 = Thai Chi
        8 = Hand pointing right, hitchhiking
        9 = Scratching crouch nervously
        10 = Forearm jerk gesture
        11 = Hand wave hello
        12 = Working on small thing on table/wall
        13 = Dancing / warming up 1
        14 = Dancing
        15 = Working/sweeping counter
        16 = Hand wave "Come closer"
        17 = Talking with hands irritated/resigned
        18 = Hand wave cheering "helicopter"
        19 = Hand wave cheering "air punch"
        20 = Shouting / cheering
        21 = Slapping in front
        22 = Aiming gangsta gun
        23 = Slapping beside
        24 = Hands up
        25 = Looking around, searching
        26 = Looking up, searching
        27 = Looking up shouting, searching
        28 = Hand pointing front / explaining
        29 = Hand pointing up-front / theatrical gesture
        30 = Looking up shouting, pointing
        31 = Shouting / cheering 2
        32 = Hand wave cheering "pumping up", shouting
        33 = Shouting / crying / holding nose
        34 = Leaning, knocking against door, complaining
        35 = Drinking
        36 = Hand fighting / box practicing
        37 = Talking, both hands up and down
        38 = Talking with hand gestures 2
        39 = Hand greeting and hug
        40 = Hand greeting and hug 2
        41 = Dancing 2
        42 = Dancing waves
        43 = Dancing 3
        44 = Dancing 4
        45 = Dancing twist
        46 = Dancing energetic
        47 = Sitting on floor / chilling
        48 = Lying on side
        49 = Lying on back
        50 = Hitting floor with bat/tool
        51 = Kneeling down to push something, standing up
        52 = Kneeling down to punch ground
        53 = Stomping on something aggressively
        54 = Fighting pose boxing
        55 = Spanking on knees
        56 = Fighting pose martial arts
        57 = Drunk, pushing someone
        58 = Drunk, pushing with both hands
        59 = Kicking
        60 = Talking / hand slap
        61 = Talking with hand gestures 3
        62 = Talking with hand gestures calm
        63 = Talking with hand gestures 4
        64 = Talking with hand gestures 5
        65 = Talking with hand gestures 6
        66 = Talking with hand gestures 7
        67 = Talking with hand gestures calm 2
        68 = Talking with hand gestures 8
        69 = Talking pointing forward
        70 = Dancing with hips
        71 = Dancing presenting thigh
        72 = Kneeling dancing
        73 = Dancing erotic 1
        74 = Dancing erotic 2
        75 = Hand wave "get over here"
        76 = Cheering / "everybody come closer"
        77 = Cheering / "get lost"
        78 = Lying on side, pain convulsions
        79 = Lying on belly crawling
        80 = Lying against wall, hand on chest
        81 = Peeking around corner
        82 = Peeking around corner 2
        83 = Storming place with gun 1
        84 = Storming place with gun 2
        85 = Storming place with gun 3
        86 = Cheering / "go go go"
        87 = Standing, hands crossed
        88 = Standing, looking at watch
        89 = Talking, not believing
        90 = Listening carefully / thinking
        91 = Standing relaxed, moving hands / talking
        92 = Dancing / warming up 2
        93 = Talking / rapping
        94 = Standing with hand in pocket, touching face
        95 = Standing / waiting 1
        96 = Standing, adjusting belt
        97 = Standing, stretching back
        98 = Standing / waiting 3
        99 = Listening crossing hands
        100 = Hitting floor with chainsaw
        101 = Lying side sleeping 1
        102 = Lying side sleeping 2
        103 = Listening agreeing
        104 = Listening denying
        105 = Crying
        106 = Leaning against wall
        107 = Cheering / working
        108 = Hand wave "drive around"
        109 = Hand wave "stop"
        110 = Kicking door
        111 = Sitting on stairs/ledge chilling
        112 = Sitting talking
        113 = Standing hand writing
        114 = Standing / waiting 2
        115 = Handing money from wallet
        116 = Kneeling working on something
        117 = Standing face-palming
        118 = Aiming long gun
        119 = Holding short gun
        120 = Jump and roll
        121 = Thrown back on floor
        122 = Standing face expr. mad
        123 = Standing face expr. chewing
        124 = Standing face expr. jaw drop
        125 = Standing face expr. eyebrows raised
        126 = Talking still
        127 = Standing face expr. one eyebrow raised
        128 = Sitting, reading, punching table
        129 = Sitting working on computer
    """
    NONE = -1
    WALK = -2
    RUN = -3
    VEHICLE_ENTER = -4
    VEHICLE_EXIT = -5
    VEHICLE_SIT = -6
    DIE = -7
    JUMP = -8
    SPRINT = -9
    WALK_CROUCH = -10
    MULTIPLE_LOCATIONS = -11
    AIM = -12


class VehicleSeat(IntEnum):
    """Vehicle seat positions.
        DRIVER = 0
        PASSENGER = 1
        REAR_LEFT = 2
        REAR_RIGHT = 3
    """
    DRIVER = 0
    PASSENGER = 1
    REAR_LEFT = 2
    REAR_RIGHT = 3


class DriverBehaviour(IntEnum):
    """AI behavior for actors driving vehicles.
        NONE = 0
        ROUTE_SLOW = 1
        ROUTE_NORMAL = 2
        ROUTE_FAST = 3
        ATTACK_PLAYER = 4
        FOLLOW_PLAYER = 5
    """
    NONE = 0
    ROUTE_SLOW = 1
    ROUTE_NORMAL = 2
    ROUTE_FAST = 3
    ATTACK_PLAYER = 4
    FOLLOW_PLAYER = 5


class Gang(IntEnum):
    """Gang/faction affiliations for actors.
        NEUTRAL_MALE = 4
        NEUTRAL_FEMALE = 5
        POLICE = 6
        BALLA = 7
        GROVE = 8
        VAGO = 9
        RIFA = 10
        NANG = 11
        MAFIA = 12
        TRIAD = 13
        AZTECA = 14
        DEALER = 17
        MEDIC = 18
        FIREMAN = 19
        CRIMINAL = 20
        BUM = 21
        SPECIAL = 22
        PROSTITUTE = 23
        ENEMY_1 = 24
        FRIEND = 25
        ENEMY_2 = 26
    """
    NEUTRAL_MALE = 4
    NEUTRAL_FEMALE = 5
    POLICE = 6
    BALLA = 7
    GROVE = 8
    VAGO = 9
    RIFA = 10
    NANG = 11
    MAFIA = 12
    TRIAD = 13
    AZTECA = 14
    DEALER = 17
    MEDIC = 18
    FIREMAN = 19
    CRIMINAL = 20
    BUM = 21
    SPECIAL = 22
    PROSTITUTE = 23
    ENEMY_1 = 24
    FRIEND = 25
    ENEMY_2 = 26


class ActorFlags(IntEnum):
    """Behavior flags for actors (bitfield)."""
    HOLD_POSITION = 2      # Bit 1: Actor stays at current position
    ATTACK_DIRECT = 4      # Bit 2: Attack player directly (360° engagement)
    FOLLOW = 8             # Bit 3: Follow player
    HEADSHOT_IMMUNE = 16   # Bit 4: Immune to headshot kills
    KILL_WHOLE_GANG = 32   # Bit 5: Objective requires killing all gang members
    HEALTH_BAR = 64        # Bit 6: Show health bar for this actor
    ENEMY_2 = 128          # Bit 7: Mark as secondary enemy type


class Actor(BaseModel):
    """
    An actor (NPC/pedestrian) in a DYOM mission.

    Actors are non-player characters that can have various behaviors, weapons, and animations.
    They can be enemies, friends, or neutral characters. Maximum 100 actors per mission.
    """

    # Appearance
    skin: int = Field(..., description="Skin/character model ID (see skin list)", ge=0)

    # Position and orientation
    position_x: float = Field(..., description="X coordinate in game world")
    position_y: float = Field(..., description="Y coordinate in game world")
    position_z: float = Field(..., description="Z coordinate in game world (height)")
    direction: float = Field(0.0, description="Facing direction in degrees (0-360)", ge=0, le=360)
    interior: int = Field(0, description="Interior ID (0 = outdoor)", ge=0)

    # Faction and behavior
    gang: Gang = Field(Gang.NEUTRAL_MALE, description="Gang/faction affiliation determining AI behavior")
    flags: int = Field(
        0,
        description=(
            "Behavior flags bitfield - combine values using bitwise OR. "
            "Available flags: "
            "HOLD_POSITION=2, ATTACK_DIRECT=4, FOLLOW=8, HEADSHOT_IMMUNE=16, "
            "KILL_WHOLE_GANG=32, HEALTH_BAR=64, ENEMY_2=128. "
            "Example combinations: 0=none, 2=hold position, 18=hold+headshot immune (2+16), "
            "22=hold+attack+headshot (2+4+16)"
        ),
        ge=0
    )

    # Combat stats
    weapon: int = Field(0, description="Weapon ID (0 = unarmed)", ge=0)
    ammo: int = Field(1000000, description="Ammunition count", ge=0)
    accuracy: int = Field(50, description="Shooting accuracy percentage (0-100)", ge=0, le=100)
    health: int = Field(100, description="Health percentage (0-200, 100 = normal)", ge=0, le=200)

    # Lifetime control
    spawn: int = Field(0, description="Objective number when actor spawns (0 = mission start)", ge=0)
    despawn: int = Field(1000, description="Objective number when actor despawns (1000 = never)", ge=0, le=1000)
    must_survive: int = Field(0, description="If 1, mission fails if actor dies", ge=0, le=1)

    # Animation
    animation: Animation = Field(Animation.NONE, description="Animation type for this actor")
    animation_argument: int = Field(0, description="Additional argument for animation (route ID, seat, etc.)")

    class Config:
        use_enum_values = True
        json_schema_extra = {
            "example": {
                "skin": 105,
                "position_x": 2495.0,
                "position_y": -1688.0,
                "position_z": 13.3,
                "direction": 90.0,
                "interior": 0,
                "gang": 25,  # Gang.FRIEND
                "flags": 0,
                "weapon": 30,
                "ammo": 500,
                "accuracy": 75,
                "health": 100,
                "spawn": 0,
                "despawn": 1000,
                "must_survive": 0,
                "animation": -1,  # Animation.NONE
                "animation_argument": 0
            }
        }
