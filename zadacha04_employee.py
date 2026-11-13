# Задача 4: клас Employee

class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def print(self):
        print(f"Служител: {self.name}, длъжност: {self.position}, заплата: {self.salary} лв.")


# Създаване на обекти и извикване на метода
employees = [
    Employee("Николай Стоянов", "програмист", 3500),
    Employee("Анна Колева", "счетоводител", 2800),
    Employee("Димитър Тодоров", "техник", 2200),
]
for e in employees:
    e.print()
