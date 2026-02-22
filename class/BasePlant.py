class BasePlant():
    plant_id = 0
    
    def __init__(self, max_kwh: int, min_operative_kwh: int, 
    price: int, maintain_cost: int, ramp_rate: float, capacity_used: float,
    plant_type: int):

        if(min_operative_kwh > max_kwh):
            min_operative_kwh = max_kwh + min_operative_kwh
            max_kwh = min_operative_kwh - max_kwh
            min_operative_kwh = min_operative_kwh - max_kwh

        if(max_kwh < 1):
            max_kwh = 1e3
        
        if(min_operative_kwh < 1):
            min_operative_kwh = max_kwh * 0.15
        
        if(price < 1):
            price = 1e4

        if(maintain_cost < 1):
            maintain_cost = price * 0.005


        if(ramp_rate < 1):
            ramp_rate = 1 # i do not how to use this variable yet so, that's it

        if(capacity_used < 0):
            capacity_used = 0 # this variable represents a percentage
        

        # this class does not do anything i think
        self.max_kwh = max_kwh
        self.min_operative_kwh = min_operative_kwh
        self.price = price
        self.maintain_cost = maintain_cost
        self.plant_type = plant_type
        self.plant_id = BasePlant.plant_id
        
        # each time that a new plant is created then increment the id
        BasePlant.plant_id += 1 
