from enum import Enum
class BasePlant():
    plant_id = 0
    # I think it's a better option to initialize using Params Classes but anyways
    def __init__(self, params: Enum):

        plant_type = params.TYPE.value
        if plant_type is None:
            print("Warning: This plant could not be created")
            return None
        
        # param assignement
        min_operative_kwh = params.MIN_OPERATIVE_KWH.value
        max_kwh = params.MAX_KWH.value
        price = params.PRICE.value
        maintain_cost = params.MAINTAIN_COST.value
        ramp_rate = params.RAMP_RATE.value
        kwh_used = 0
        maintain_days_ratio = params.MAINTAIN_DAYS_RATIO.value

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
        
        if(maintain_days_ratio < 1):
            maintain_days_ratio = 1
        # this class does not do anything i think
        self.max_kwh = max_kwh
        self.min_operative_kwh = min_operative_kwh
        self.price = price
        self.maintain_cost = maintain_cost
        self.type = plant_type
        self.id = BasePlant.plant_id
        self.ramp_rate = ramp_rate
        self.maintain_days_ratio = maintain_days_ratio
        self.kwh_used = kwh_used
        
        # each time that a new plant is created then increment the id
        BasePlant.plant_id += 1 

        print(f"Info: the plant of type {self.type} with id {self.id} has been created")

    def __str__(self):
        head = f"Plant: (type: {self.type}, id: {self.id}, price: {self.price}, kwh used: {self.kwh_used})\n"
        body = f"This is plants properties: (max kwh: {self.max_kwh}, maintain cost: {self.maintain_cost}, "
        part1 = f"min operative kwh: {self.min_operative_kwh}, ramp rate: {self.ramp_rate}, "
        part2 = f"maintain days ratio: {self.maintain_days_ratio})\n"
        footer = "---------------------------------------------------------------------------------------\n"
        return  f"{footer}{head}{body}{part1}{part2}{footer}"
        