from Store import Store
from User import User
from BasePlant import BasePlant
from Plants import Coalplant
from PlantParams import CoalPlantParams

print("Probando la tienda :3")

Store.generate_plants()
Store.show_available_plants()

user = User()

plant0 = Coalplant(CoalPlantParams)
user.plants.append(plant0)
print(BasePlant.plant_id)
Store.sell_plant(user, BasePlant.plant_id-1)
print(user.plants)
print(user.balance)

