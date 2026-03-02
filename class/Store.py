from User import User
from PlantParams import (
    CoalPlantParams, GasTurbineParams, SolarFarmParams,
    HydroPlantParams, WindTurbineParams, NuclearPlantParams
)
from Plants import (
    Coalplant, GasTurbine, SolarFarm, 
    HydroPlant, WindTurbine, NuclearPlant
)
import random

class Store:
    available_plants = []
    
    # Diccionario de mapeo: relaciona el Enum de parámetros con la Clase
    PLANT_MAP = {
        CoalPlantParams: Coalplant,
        GasTurbineParams: GasTurbine,
        SolarFarmParams: SolarFarm,
        HydroPlantParams: HydroPlant,
        WindTurbineParams: WindTurbine,
        NuclearPlantParams: NuclearPlant
    }

    PLANT_PRICES = {
        "COAL": 560_000
    }

    @staticmethod
    def show_available_plants():
        for pl in Store.available_plants:
            print(f"id({pl.id}) - {pl.type}: price: ${pl.price}") 

    @staticmethod
    def generate_plants():
        # Limpiar la tienda antes de generar nuevas (opcional)
        Store.available_plants = []
        
        cantidad = random.randint(1, 5)
        posibles_params = list(Store.PLANT_MAP.keys())
        
        for _ in range(cantidad):
            # 1. Elegimos un parámetro al azar
            param_elegido = random.choice(posibles_params)
            
            # 2. Obtenemos la CLASE correspondiente del mapeo
            clase_planta = Store.PLANT_MAP[param_elegido]
            
            # 3. Instanciamos dinámicamente pasando el parámetro
            # Esto llama al __init__ de BasePlant a través de la subclase
            nueva_planta = clase_planta(param_elegido)
            
            Store.available_plants.append(nueva_planta)
        
        print(f"Tienda: Se han generado {cantidad} nuevas plantas.")

    @staticmethod
    def sell_plant(user: User, plant_id):
        for pl in user.plants:
            if pl.id == plant_id:
                print(f"Info: {pl.type} plant with id {pl.id} will be sold at ${Store.PLANT_PRICES[pl.type]}")
                user.plants = [item for item in user.plants if item.id != plant_id]
                user.balance += Store.PLANT_PRICES[pl.type]

        # user wants to sell one of their plants

        pass

    def buy_plant():
        # user wants to buy one of the Store's plants
        pass