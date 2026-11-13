# Задача 7: клас Car, наследник на Vehicle

class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def print(self):
        print(f"Превозно средство: {self.brand} {self.model}, година: {self.year}")


class Car(Vehicle):
    def __init__(self, brand, model, year, doors):
        super().__init__(brand, model, year)   # полетата на Vehicle
        self.doors = doors

    def print(self):   # предефиниране на print
        print(f"Автомобил: {self.brand} {self.model}, година: {self.year}, брой врати: {self.doors}")


# Създаване на обекти и извикване на метода
cars = [
    Car("Toyota", "Corolla", 2019, 4),
    Car("BMW", "M4", 2022, 2),
]
for c in cars:
    c.print()
