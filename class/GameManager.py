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

class StartBalance(Enum):
    EASY = 750_000
    NORMAL = 350_000
    HARD = 275_000
    INSANE = 150_000
    ADMIN = 90_000

class GameManager:
    _instance = None  # Atributo privado para el Singleton

    def __new__(cls, *args):
        if cls._instance is None:
            cls._instance = super(GameManager, cls).__new__(cls)
        return cls._instance

    def __init__(self, difficulty):
        # El init puede ejecutarse cada vez, así que usamos un flag
        if not hasattr(self, 'initialized'):
            if StartBalance[difficulty]:
                print(f"Info: Setting difficulty to {difficulty}")
                self.difficulty = difficulty
                self.user = User(StartBalance[difficulty])
            else:
                print(f"Warning: Selected difficulty does not exist, setting to NORMAL")
                self.difficulty = "NORMAL"
                self.user = User(StartBalance.NORMAL)
            
            # Starting params
            self.day = 1
            self.step = 0
            self.current_weather = WeatherType.SUNNY
            self.unstable_steps = 0
            self.initialized = True

            print("GameManager initialized successfully.")

        else:
            print("Error: GameManager could not be instanced, an instance of GameManager already exists!")

    def next_step(self):
        """Avanza el reloj del juego y actualiza condiciones."""
        self.step += 1
        if self.step >= 24:
            self.step = 0
            self.day += 1
    

    def new_weather(self):
        self.current_weather = random.choice(list(WeatherType))