# controls buying-selling plants
class Store:
    available_plants = [] 
    
    def show_available_plats():
        for pl in Store.available_plants:
            print(f"id({pl.plant_id}) - {pl.plant_type}: price: ${pl.price}")

    def generate_plants():
        # generates a random number to define the amount of new plants
        # generates a random number for each new plant in order to select the type
        pass

    def sell_plant():
        # user wants to sell one of their plants
        pass

    def buy_plant():
        # user wants to buy one of the Store's plants
        pass