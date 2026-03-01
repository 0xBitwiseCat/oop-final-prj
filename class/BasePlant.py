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
        self.changing_steps = 0
        # each time that a new plant is created then increment the id
        BasePlant.plant_id += 1 

        # this variable must be increase for each day in order to request maintainement
        self.days_without_maintainement = 0
        self.kwh_used_before_shutting_down = 0

        print(f"Info: the plant of type {self.type} with id {self.id} has been created")

    def set_initial_kwh(self, new_kwh):
        if(new_kwh < self.min_operative_kwh or new_kwh > self.max_kwh):
            print(f"Warning: {new_kwh} exceeds operative limits of this plant (id: {self.id})")
            print(f"Operative limits: [{self.min_operative_kwh}, {self.max_kwh}]")
            return
        self.kwh_used = new_kwh

    def verify_maintainement(self):
        if self.days_without_maintainement >= self.maintain_days_ratio:
            print(f"Info: plant with id {self.id} requires maintainement, shutting down...")
            self.kwh_used_before_shutting_down = self.kwh_used
            self.kwh_used = 0
            
    
    def apply_maintainement(self):
        print(f"Info: plant with id {self.id} is operative again...")
        self.days_without_maintainement = 0
        self.kwh_used = self.kwh_used_before_shutting_down
        self.kwh_used_before_shutting_down = 0

    def set_changing_steps(self, new_kwh):
        if(new_kwh < self.min_operative_kwh or new_kwh > self.max_kwh):
            print(f"Warning: {new_kwh} exceeds operative limits of this plant (id: {self.id})")
            print(f"Operative limits: [{self.min_operative_kwh}, {self.max_kwh}]")
            return
        diff = new_kwh - self.kwh_used
        acc = diff//self.ramp_rate
        self.changing_steps = acc

    def change_kwh_used_with_operating(self, new_kwh):
        if(new_kwh < self.min_operative_kwh or new_kwh > self.max_kwh):
            print(f"Warning: {new_kwh} exceeds operative limits of this plant (id: {self.id})")
            print(f"Operative limits: [{self.min_operative_kwh}, {self.max_kwh}]")
            return
    
        if self.kwh_used == new_kwh:
            print("Info: plant was loaded successfully!")
            self.set_changing_steps = 0
            return
        
        if self.changing_steps == 0 and self.kwh_used != new_kwh:
            self.set_changing_steps(new_kwh)
             
        s = f"Info: plant with id {self.id} will be setting its capacity "
        t = f"in steps of {self.changing_steps} kwh until {new_kwh} kwh"
        print(f"{s}{t}")
        self.kwh_used += self.changing_steps



    def __str__(self):
        head = f"Plant: (type: {self.type}, id: {self.id}, price: {self.price}, kwh used: {self.kwh_used})\n"
        body = f"This is plants properties: (max kwh: {self.max_kwh}, maintain cost: {self.maintain_cost}, "
        part1 = f"min operative kwh: {self.min_operative_kwh}, ramp rate: {self.ramp_rate}, "
        part2 = f"maintain days ratio: {self.maintain_days_ratio})\n"
        footer = "---------------------------------------------------------------------------------------\n"
        return  f"{footer}{head}{body}{part1}{part2}{footer}"
        