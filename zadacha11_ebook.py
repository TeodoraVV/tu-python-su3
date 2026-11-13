

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def print(self):
        print(f"Книга: „{self.title}“, автор: {self.author}, година: {self.year}")


class EBook(Book):
    def __init__(self, title, author, year, format, size):
        super().__init__(title, author, year)   # полетата на Book
        self.format = format
        self.size = size

    def print(self):   
        super().print()
        print(f"  Формат: {self.format}, размер: {self.size} MB")



ebooks = [
    EBook("Python за начинаещи", "Мартин Иванов", 2023, "PDF", 12.5),
    EBook("Изкуството на войната", "Сун Дзъ", 2015, "EPUB", 1.8),
]
for e in ebooks:
    e.print()
