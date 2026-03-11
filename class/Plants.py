from BasePlant import BasePlant

class Coalplant(BasePlant):
    pass

class GasTurbine(BasePlant):
    pass

class SolarFarm(BasePlant):
    def allow_operation(self, weather):
        if weather != "SUNNY" and weather != "CALM":
            print(f"Warning: Plant with id {self.id} can't operate on this weather, shutting down...")
            self.kwh_used = 0
            self.kwh_used_before_shutting_down = 0 
            self.is_operative = False
        else:
            print(f"Info: Plant with id {self.id} is operative for today!")

class HydroPlant(BasePlant):
    pass

class WindTurbine(BasePlant):
    pass

class NuclearPlant(BasePlant):
    pass
    