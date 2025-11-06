"""
DYOM Mission Constants

This module contains constant definitions and enumerations used throughout
DYOM missions, including weather types, weapons, and other fixed values.
"""

from enum import IntEnum
from pydantic import RootModel
from pydantic.types import NonNegativeInt


class Weather(IntEnum):
    """
    Weather conditions available in GTA San Andreas for DYOM missions.

    Available weather types:
    - 0: Sunny heat clear
    - 1: Sunny heat small clouds
    - 2: Sunny light clouds
    - 3: Sunny medium clouds
    - 4: Overcast gray clouds
    - 5: Sunny medium clouds 2
    - 6: Sunny foggy
    - 7: Overcast dark clouds
    - 8: Rain & lighting
    - 9: Fog heavy
    - 10: Sunny big clouds
    - 11: Sunny heat 2
    - 12: Overcast gray clouds 2
    - 13: Sunny big clouds 2
    - 14: Sunny big clouds 3
    - 15: Overcast dark
    - 16: Rain & lighting 2
    - 17: Sunny heat 3
    - 18: Sunny heat clouds
    - 19: Sand storm
    - 20: Fog black clouds (underwater weather)
    - 21: Interiors weather
    - 22: Interiors weather clouds
    """
    SUNNY_HEAT_CLEAR = 0
    SUNNY_HEAT_SMALL_CLOUDS = 1
    SUNNY_LIGHT_CLOUDS = 2
    SUNNY_MEDIUM_CLOUDS = 3
    OVERCAST_GRAY_CLOUDS = 4
    SUNNY_MEDIUM_CLOUDS_2 = 5
    SUNNY_FOGGY = 6
    OVERCAST_DARK_CLOUDS = 7
    RAIN_AND_LIGHTING = 8
    FOG_HEAVY = 9
    SUNNY_BIG_CLOUDS = 10
    SUNNY_HEAT_2 = 11
    OVERCAST_GRAY_CLOUDS_2 = 12
    SUNNY_BIG_CLOUDS_2 = 13
    SUNNY_BIG_CLOUDS_3 = 14
    OVERCAST_DARK = 15
    RAIN_AND_LIGHTING_2 = 16
    SUNNY_HEAT_3 = 17
    SUNNY_HEAT_CLOUDS = 18
    SAND_STORM = 19
    FOG_BLACK_CLOUDS_UNDERWATER = 20
    INTERIORS_WEATHER = 21
    INTERIORS_WEATHER_CLOUDS = 22


class Weapon(IntEnum):
    """
    Weapon IDs available in GTA San Andreas for DYOM missions.

    Available weapons:
    - 0: None
    - 1: Brass knuckles
    - 2: Golf club
    - 3: Nightstick
    - 4: Knife
    - 5: Baseball bat
    - 6: Shovel
    - 7: Pool cue
    - 8: Katana
    - 9: Chainsaw
    - 10: Dildo
    - 11: Vibrator
    - 12: Dildo 2
    - 13: Vibrator 2
    - 14: Flowers
    - 15: Cane
    - 16: Grenade
    - 17: Tear gas
    - 18: Molotov Cocktail
    - 22: Pistol
    - 23: Pistol - silenced
    - 24: Desert Eagle
    - 25: Shotgun
    - 26: Shotgun - sawn-off
    - 27: Shotgun - combat
    - 28: Micro SMG
    - 29: SMG
    - 30: AK-47
    - 31: M4
    - 32: Tec-9
    - 33: Rifle
    - 34: Rifle Sniper
    - 35: Rocket launcher
    - 36: Rocket launcher - heat seeking
    - 37: Flame thrower
    - 38: Mini gun
    - 39: Remote explosives
    - 40: Remote detonator
    - 41: Spraycan
    - 42: Fire extinguisher
    - 43: Camera
    - 44: Goggles night-vision
    - 45: Goggles thermal
    - 46: Parachute
    - 47: Pistol - jammed
    - 48: Random
    """
    NONE = 0
    BRASS_KNUCKLES = 1
    GOLF_CLUB = 2
    NIGHTSTICK = 3
    KNIFE = 4
    BASEBALL_BAT = 5
    SHOVEL = 6
    POOL_CUE = 7
    KATANA = 8
    CHAINSAW = 9
    DILDO = 10
    VIBRATOR = 11
    DILDO_2 = 12
    VIBRATOR_2 = 13
    FLOWERS = 14
    CANE = 15
    GRENADE = 16
    TEAR_GAS = 17
    MOLOTOV_COCKTAIL = 18
    PISTOL = 22
    PISTOL_SILENCED = 23
    DESERT_EAGLE = 24
    SHOTGUN = 25
    SHOTGUN_SAWNOFF = 26
    SHOTGUN_COMBAT = 27
    MICRO_SMG = 28
    SMG = 29
    AK47 = 30
    M4 = 31
    TEC9 = 32
    RIFLE = 33
    RIFLE_SNIPER = 34
    ROCKET_LAUNCHER = 35
    ROCKET_LAUNCHER_HEAT_SEEKING = 36
    FLAME_THROWER = 37
    MINI_GUN = 38
    REMOTE_EXPLOSIVES = 39
    REMOTE_DETONATOR = 40
    SPRAYCAN = 41
    FIRE_EXTINGUISHER = 42
    CAMERA = 43
    GOGGLES_NIGHT_VISION = 44
    GOGGLES_THERMAL = 45
    PARACHUTE = 46
    PISTOL_JAMMED = 47
    RANDOM = 48


class RadarMarker(IntEnum):
    """
    Radar marker color types for objectives.

    Available colors:
    - -1: None (no marker)
    - 0: Red
    - 1: Green
    - 2: Blue
    - 3: White
    - 4: Yellow
    """
    NONE = -1
    RED = 0
    GREEN = 1
    BLUE = 2
    WHITE = 3
    YELLOW = 4


class Skin(RootModel[NonNegativeInt]):
    """Character skin/model ID for actors and players.
    """
    root: NonNegativeInt

    model_config = {
        'json_schema_extra': {
            'type': 'integer',
            'minimum': 0,
            'description': """Character skin/model ID for actors and players.

            Available skins (300 total):
            - 0: CJ
            - 7: Casual man black 1
            - 9: Elegant granny black
            - 10: Rural granny black
            - 11: Elegant woman black (bow tie)
            - 12: Glamour woman black 1
            - 13: Rasta woman black 1
            - 14: Vacation sir black
            - 15: Casual sir black 1
            - 16: Worker man black (orange vest)
            - 17: Elegant sir black
            - 18: Beach man black
            - 19: Rap man black 1
            - 20: Casual man black 2
            - 21: Rap man black 2
            - 22: Rap man black 3
            - 23: Dude man white 1
            - 24: Casual sir black 2
            - 25: Casual man black 3
            - 26: Vacation man white (backpack)
            - 27: Worker man white (construction)
            - 28: Rap man black (drug dealer)
            - 29: Dude man white (drug dealer)
            - 30: Casual man mexican (drug dealer)
            - 31: Western mrs white
            - 32: Rural sir black (eyepatch)
            - 33: Western man white 1
            - 34: Western man white 2
            - 35: Casual sir black 3
            - 36: Casual sir black 4
            - 37: Casual man white 1
            - 38: Casual granny black
            - 39: Rural granny white 1
            - 40: Glamour woman black 2
            - 41: Rap woman black
            - 43: Elegant grandpa mexican
            - 44: Casual sir mexican
            - 45: Beach man white 1
            - 46: Elegant man mexican 1
            - 47: Casual man mexican 1
            - 48: Casual man mexican 2
            - 49: Traditional grandpa asian
            - 50: Worker man mexican (overalls)
            - 51: Sport man black
            - 52: Sport man white 1
            - 53: Casual mrs white
            - 54: Rural mrs black 1
            - 55: Glamour woman white 1
            - 56: Dude woman white
            - 57: Elegant grandpa asian
            - 58: Casual sir native
            - 59: Elegant man asian 1
            - 60: Casual man white 2
            - 61: Worker man white (uniform)
            - 62: Pyjamas grandpa white
            - 63: Erotic woman black 1
            - 64: Erotic woman black 2
            - 66: Casual man black 4
            - 67: Casual man black 5
            - 68: Priest grandpa white
            - 69: Casual woman black 1
            - 70: Worker sir white (lab coat)
            - 71: Worker sir mexican (blue collar)
            - 72: Casual man white 3
            - 73: Casual man white 4
            - 75: Erotic granny white
            - 76: Elegant woman black 1
            - 77: Hobbo mrs white
            - 78: Hobbo grandpa black
            - 79: Hobbo man black
            - 80: Boxer man black
            - 81: Boxer man white
            - 82: Elvis man black 1
            - 83: Elvis man black 2
            - 84: Elvis sir black
            - 85: Glamour woman white 2
            - 87: Erotic woman white 1
            - 88: Casual granny white 1
            - 89: Rural granny white 2
            - 90: Erotic woman white 2
            - 91: Glamour woman black 3
            - 92: Sport woman white (rollers)
            - 93: Elegant woman white
            - 94: Casual grandpa white 1
            - 95: Rural sir white 1
            - 96: Sport man white 2
            - 97: Beach man white 2
            - 98: Elegant man mexican 2
            - 99: Sport man white (rollers)
            - 100: Biker man white 1
            - 101: Dude man white 2
            - 102: Balla man black 1
            - 103: Balla man black 2
            - 104: Balla man black 3
            - 105: Grove man black 1
            - 106: Grove man black 2
            - 107: Grove man black 3
            - 108: Vagos man mexican 1
            - 109: Vagos man mexican 2
            - 110: Vagos man mexican 3
            - 111: Russian man white 1
            - 112: Russian man white 2
            - 113: Elegant sir white 1
            - 114: Aztecas man mexican 1
            - 115: Aztecas man mexican 2
            - 116: Aztecas man mexican 3
            - 117: Triad man asian 1
            - 118: Triad man asian 2
            - 120: Elegant man asian 2
            - 121: Thug man asian 1
            - 122: Thug man asian 2
            - 123: Traditional man asian
            - 124: Elegant man white 1
            - 125: Casual man white 5
            - 126: Elegant man white 2
            - 127: Elegant sir white 2
            - 128: Casual man native
            - 129: Traditional granny native
            - 130: Traditional mrs native
            - 131: Traditional woman mexican
            - 132: Rural grandpa white
            - 133: Biker sir white
            - 134: Redneck sir black
            - 135: Redneck man white
            - 136: Rasta sir black
            - 137: Hobbo man white
            - 138: Beach woman white 2
            - 139: Beach woman black
            - 140: Beach woman black 2
            - 141: Elegant woman asian
            - 142: Rasta sir black 2
            - 143: Dude man black (hair net)
            - 144: Worker man black (mask)
            - 145: Erotic woman black 3 (mask)
            - 146: Beach man black (mask)
            - 147: Elegant sir white 3
            - 148: Elegant mrs black 1
            - 150: Elegant woman black 2
            - 151: Casual woman white
            - 152: Erotic woman white 3
            - 153: Worker man white (helmet elegant)
            - 154: Beach man white 3
            - 155: Worker man white (pizza)
            - 156: Worker sir black (barber)
            - 157: Redneck woman white
            - 158: Rural sir white 2
            - 159: Redneck sir white 2
            - 160: Redneck sir white 3
            - 161: Rural man white
            - 162: Redneck man white (deformed)
            - 163: Worker man black (earpiece elegant)
            - 164: Worker man white (earpiece elegant)
            - 165: Worker man white (M.I.B)
            - 166: Worker man black (M.I.B)
            - 167: Worker man white (Cluckin Bell)
            - 168: Worker man black (appron)
            - 169: Elegant woman asian 2
            - 170: Casual man white 6
            - 171: Elegant man white (bow tie)
            - 172: Elegant woman white (bow tie)
            - 173: Rifa man mexican
            - 174: Rifa man mexican 2
            - 175: Rifa man mexican 3
            - 176: Worker man black (barber)
            - 177: Worker man white (barber)
            - 178: Erotic woman black 4
            - 179: Worker man white (Ammunation)
            - 180: Casual man black 6
            - 181: Punk man white
            - 182: Casual sir black 5
            - 183: Casual sir black 6
            - 184: Casual man white 7
            - 185: Elegant man black
            - 186: Elegant man asian 3
            - 187: Elegant man white 3
            - 188: Casual man white 8
            - 189: Elegant man white (red vest)
            - 190: Girlfriend Barbara black
            - 191: Girlfriend Helena white
            - 192: Girlfriend Michelle white
            - 193: Girlfriend Katie asian
            - 194: Girlfriend Millie black
            - 195: Girlfriend Denise
            - 196: Rural granny white 3
            - 197: Rural granny white 4
            - 198: Western woman white
            - 199: Rural woman white 2
            - 200: Redneck man white
            - 201: Redneck woman white
            - 202: Casual man white 9
            - 203: Martial arts man asian
            - 204: Martial arts man white
            - 205: Worker woman black (Burgershot)
            - 206: Casual man white 10
            - 207: Casual woman black 2
            - 209: Worker grandpa asian (appron)
            - 210: Casual man asian 1
            - 211: Worker woman black (STAFF)
            - 212: Hobbo sir white
            - 213: Hobbo Elvis sir white
            - 214: Glamour woman black 4
            - 215: Elegant mrs black 2
            - 216: Elegant woman black 3
            - 217: Worker man white (STAFF)
            - 218: Rural mrs black 2
            - 219: Elegant woman black 4
            - 220: Traditional sir jamaican
            - 221: Casual sir black 7
            - 222: Casual sir black 8
            - 223: Elegant man mexican 3
            - 224: Glamour mrs asian
            - 225: Casual mrs asian
            - 226: Dude woman asian
            - 227: Elegant sir asian 1
            - 228: Elegant sir asian 2
            - 229: Casual sir asian
            - 230: Hobbo man white
            - 231: Casual granny white 2
            - 232: Casual granny white 3
            - 233: Elegant woman black 5
            - 234: Casual sir white
            - 235: Casual grandpa asian
            - 236: Casual grandpa white 2
            - 237: Erotic woman white 4
            - 238: Erotic woman black 5
            - 239: Redneck sir white
            - 240: Elegant man white 4
            - 241: Biker man white 2
            - 242: Biker man white 3
            - 243: Casual woman mexican
            - 244: Erotic woman black 6
            - 245: Casual woman black 3
            - 246: Erotic woman white 5
            - 247: Biker man white 4
            - 248: Biker man white 5
            - 249: Pimp man black
            - 250: Casual man white 11
            - 251: Beach woman white 1
            - 252: Beach man white 4
            - 253: Worker sir black (uniform)
            - 254: Biker man white 6
            - 255: Worker sir white (uniform)
            - 256: Erotic woman black 7
            - 257: Erotic woman white 6
            - 258: Casual sir black 9
            - 259: Casual man white 12
            - 260: Worker man black (construction)
            - 261: Casual man asian 2
            - 262: Casual sir black 10
            - 263: Elegant woman asian
            - 264: Clown man white
            - 274: Worker man black (blue-collar)
            - 275: Worker man black (blue-collar)
            - 276: Worker man asian (blue-collar)
            - 277: Firefighter man white
            - 278: Firefighter man black
            - 279: Firefighter man mexican
            - 280: Police man white
            - 281: Police sir white
            - 282: Police man black
            - 283: Police man white (sherif)
            - 284: Police man black (bike)
            - 285: SWAT man white
            - 286: FBI man white
            - 287: Soldier man white
            - 288: Police man white (sherif)
            - 289: RANDOM
            - 1000: Elegant sir white 4
            - 1001: Casual man black (thin)
            - 1002: Casual man black (fat)
            - 1003: Catalina
            - 1004: Cesar
            - 1005: Claude
            - 1006: Worker man white (mechanic)
            - 1007: Emmet
            - 1008: Mafia man white
            - 1009: Worker sir mexican (janitor)
            - 1010: Worker man white (mechanic)
            - 1011: Jizzy
            - 1012: Police man mexican
            - 1013: Rasta woman black 2
            - 1014: Dude man white 3
            - 1015: Madd Dogg
            - 1016: OG Loc
            - 1017: Biker man white 7
            - 1018: Pulaski (police)
            - 1019: Rosenberg
            - 1020: Ryder
            - 1021: Ryder masked
            - 1022: Mafia man white
            - 1023: Big Smoke
            - 1024: Big Smoke (vest)
            - 1025: Triad man asian
            - 1026: Sweet
            - 1027: T-Bone
            - 1028: Tenpenny (police)
            - 1029: Toreno
            - 1030: Truth
            - 1031: Woozie
            - 1032: Zero
            """
        }
    }
