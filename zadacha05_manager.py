

class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def print(self):
        print(f"Служител: {self.name}, длъжност: {self.position}, заплата: {self.salary} лв.")


class Manager(Employee):
    def __init__(self, name, position, salary, department):
        super().__init__(name, position, salary)   # полетата на Employee
        self.department = department

    def print(self):   # предефиниране на print
        super().print()
        print(f"  Отдел: {self.department}")



managers = [
    Manager("Светла Ангелова", "мениджър", 5000, "Маркетинг"),
    Manager("Христо Попов", "ръководител", 5500, "ИТ"),
]
for m in managers:
    m.print()
