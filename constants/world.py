# World related enums
from enum import IntEnum

class Biomes(IntEnum):
    """Enums representing in-game world biomes."""

    OCEAN  = 0
    PLAINS = 1
    DESERT = 2
    ...

class Weather(IntEnum):
    """Enum representing the current weather."""

    CLEAR = 0
    RAIN = 1
    THUNDER = 2
