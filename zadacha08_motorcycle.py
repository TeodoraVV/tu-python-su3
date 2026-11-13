

class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def print(self):
        print(f"Превозно средство: {self.brand} {self.model}, година: {self.year}")


class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, engine_capacity):
        super().__init__(brand, model, year)  
        self.engine_capacity = engine_capacity

    def print(self):   
        print(f"Мотоциклет: {self.brand} {self.model}, година: {self.year}, "
              f"кубатура: {self.engine_capacity} куб. см")



motorcycles = [
    Motorcycle("Yamaha", "MT-07", 2021, 689),
    Motorcycle("Honda", "CBR600RR", 2020, 599),
]
for m in motorcycles:
    m.print()
