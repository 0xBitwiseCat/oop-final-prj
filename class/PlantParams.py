from enum import Enum

# this classes describes all properties in order to create new plants
# i do not want to change values directly in the factory class so i prefer
# to create a new class where to find the values


## ! it is necessary to add logic that describes when the plant needs maintainement

class CoalPlantParams(Enum):
    PRICE = 1e6
    MAX_KWH = 100e3
    MIN_OPERATIVE_KWH = 10e3
    MAINTAIN_COST = 7e3
    MAINTAIN_DAYS_RATIO = 3

class GasTurbineParams(Enum):
    PRICE = 1.35e3
    MAX_KWH = 140e3
    MIN_OPERATIVE_KWH = 28e3
    MAINTAIN_COST = 7.75e3
    MAINTAIN_DAYS_RATIO = 3

class SolarFarmParams(Enum):
    PRICE = 1.9e4
    MAX_KWH = 80e3
    MIN_OPERATIVE_KWH = 0.1e3
    MAINTAIN_COST = 1.38e3
    MAINTAIN_DAYS_RATIO = 1

class HydroPlantParams(Enum):
    PRICE = 1e9
    MAX_KWH = 2e7
    MIN_OPERATIVE_KWH = 50e3
    MAINTAIN_COST = 1e4
    MAINTAIN_DAYS_RATIO = 7

class WindTurbineParams(Enum):
    PRICE = 0.9e4
    MAX_KWH = 10e3
    MIN_OPERATIVE_KWH = 0
    MAINTAIN_COST = 0.8e3
    MAINTAIN_DAYS_RATIO = 1

class NuclearPlantParams(Enum):
    PRICE = 1.7e12
    MAX_KWH = 9e9
    MIN_OPERATIVE_KWH = 8e4
    MAINTAIN_COST = 8e5
    MAINTAIN_DAYS_RATIO = 20