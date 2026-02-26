class BasePlant():
    plant_id = 0
    # I think it's a better option to initialize using Params Classes but anyways
    def __init__(self, params: Enum):
        properties = vars(params)
        
        plant_type = properties.get("TYPE")
        if plant_type is None:
            print("Warning: This plant could not be created")
            return None
        
        # param assignement
        min_operative_kwh = properties.get("MIN_OPERATIVE_KWH", 1)
        max_kwh = properties.get("MAX_KWH", 100)
        price = properties.get("PRICE")
        maintain_cost = properties.get("MAINTAIN_COST")
        ramp_rate = properties.get("RAMP_RATE")
        kwh_used = 0

        if(max_kwh < 1):
            max_kwh = 1e3

        if(min_operative_kwh > max_kwh):
            min_operative_kwh = max_kwh + min_operative_kwh
            max_kwh = min_operative_kwh - max_kwh
            min_operative_kwh = min_operative_kwh - max_kwh
        
        if(min_operative_kwh < 1):
            min_operative_kwh = max_kwh * 0.15
        
        if(price < 1):
            price = 1e4

        if(maintain_cost < 1):
            maintain_cost = price * 0.005


        if(ramp_rate < 1):
            ramp_rate = 1 # i do not how to use this variable yet so, that's it

        if(kwh_used < 0):
            kwh_used = 0
        

        # this class does not do anything i think
        self.max_kwh = max_kwh
        self.min_operative_kwh = min_operative_kwh
        self.price = price
        self.maintain_cost = maintain_cost
        self.type = plant_type
        self.id = BasePlant.plant_id
        
        # each time that a new plant is created then increment the id
        BasePlant.plant_id += 1 

        print(f"Info: the plant of type {self.type} with id {self.id} has been created")
