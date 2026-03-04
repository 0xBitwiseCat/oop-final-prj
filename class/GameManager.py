from User import User
from PlantParams import (
    CoalPlantParams, GasTurbineParams, SolarFarmParams,
    HydroPlantParams, WindTurbineParams, NuclearPlantParams
)
from Plants import (
    Coalplant, GasTurbine, SolarFarm, 
    HydroPlant, WindTurbine, NuclearPlant
)

from enum import Enum

class WeatherType(Enum):
    SUNNY = "SUNNY"
    CLOUDY = "CLOUDY"
    RAINY = "RAINY"
    STORMY = "STORMY"
    WINDY = "WINDY"
    CALM = "CALM"

class GameManager:
    day = 1
    instance = None
    weather = WeatherType.SUNNY

    def __init__(self):
        if GameManager.instance != None:
            print("Error: GameManager could not be instanced, an instance of GameManager already exists!")
            return GameManager.instance 
        
        self.day = 1
        self.step = 0
        GameManager.instance = self
        self.current_weather = WeatherType.SUNNY # Clima inicial
