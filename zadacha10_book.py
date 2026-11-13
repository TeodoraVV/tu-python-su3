# Задача 10: клас Book

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def print(self):
        print(f"Книга: „{self.title}“, автор: {self.author}, година: {self.year}")


# Създаване на обекти и извикване на метода
books = [
    Book("Под игото", "Иван Вазов", 1894),
    Book("Тютюн", "Димитър Димов", 1951),
    Book("1984", "Джордж Оруел", 1949),
]
for b in books:
    b.print()
