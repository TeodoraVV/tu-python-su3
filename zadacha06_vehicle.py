# Задача 6: клас Vehicle

class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def print(self):
        print(f"Превозно средство: {self.brand} {self.model}, година: {self.year}")


# Създаване на обекти и извикване на метода
vehicles = [
    Vehicle("Volvo", "FH16", 2020),
    Vehicle("Mercedes", "Sprinter", 2018),
    Vehicle("Iveco", "Daily", 2021),
]
for v in vehicles:
    v.print()
