import math
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

    def __init__(self, difficulty, multiplier):
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

            self.base_max_kwh = 75_000 * (multiplier/5)  # Demanda máxima inicial depende de la dificultad
            self.growth_rate = 0.08 * multiplier   # Sube un 8% * pos_dificultad cada vez
            self.days_to_grow = 5     # Sube cada 5 días

            print("GameManager initialized successfully.")

        else:
            print("Error: GameManager could not be instanced, an instance of GameManager already exists!")

    def get_daily_max(self):
        """Calcula el tope de demanda actual basado en los días pasados."""
        # Cada 'self.days_to_grow', la demanda máxima sube un porcentaje
        periods_passed = self.day // self.days_to_grow
        return self.base_max_kwh * (1 + self.growth_rate) ** periods_passed

    def update_demand(self):
        """Calcula la demanda para el step actual usando la logística y el crecimiento."""
        # 1. Obtener el máximo actual (L)
        current_L = self.get_daily_max()
        
        # 2. Parámetros de la curva horaria
        k = 0.3      # Pendiente (ajustada para subir lento)
        x0 = 12      # El punto medio es al mediodía (step 12)
        
        # 3. Aplicar función logística
        logistic_factor = 1 / (1 + math.exp(-k * (self.step - x0)))
        
        # 4. Resultado final
        self.current_demand = round(current_L * logistic_factor,0)
        return self.current_demand

    def info_step(self):
        print(f"Info: Current demand: {self.current_demand} kwh ({self.step}/24)")
        print(f"Info: Current supply offered: {self.user.current_power} kwh")
    
    def start_day(self):
        for pl in self.user.plants:
            pl.allow_operation(self.current_weather)
    def finish_day(self):
        print(f"Info: Finish day!")

    def next_step(self):
        """Avanza el reloj del juego y actualiza condiciones."""
        self.step = self.step + 1
        self.info_step()
        if self.step >= 24:
            self.step = 0
            self.day += 1
    
    def user_action(self):
        while(True):
            print(f"User: ${self.user.balance}, {len(self.user.plants)} plants, {self.user.max_power} kwh (max)")
            print(f"What do you want to do?")
            print(f"")
            print(f"1. Buy plants")
            print(f"2. Sell plants")
            print(f"3. Change kwh of a plant")
            print(f"4. Skip for now")
    
    def new_weather(self):
        self.current_weather = random.choice(list(WeatherType))