# Задача 9: клас Animal и наследници Dog и Cat

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sound(self):
        print(f"{self.name} издава звук.")


class Dog(Animal):
    def sound(self):   # предефиниране на sound
        print(f"Кучето {self.name} ({self.age} г.) лае: Бау-бау!")


class Cat(Animal):
    def sound(self):   # предефиниране на sound
        print(f"Котката {self.name} ({self.age} г.) мяука: Мяу!")


# Създаване на обекти и извикване на метода
animals = [
    Dog("Рекс", 4),
    Cat("Мърка", 2),
    Dog("Шаро", 7),
    Cat("Пухчо", 1),
]
for a in animals:
    a.sound()
