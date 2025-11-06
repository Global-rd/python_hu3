class Author:
    
    def __init__(self, name:str, nationality: str):
        self.name = name
        self.nationality = nationality

    def __str__(self):
        return f"{self.name}"
    
    def __repr__(self):
        return f"Author(name={self.name}, nationality={self.nationality})"

class Book:
    
    def __init__(self, title:str, genre:str, author: Author):
        self.title = title
        self.genre = genre
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

class Library:
    
    def __init__(self, name:str):
        self.name = name
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)

    def list_books(self):
        print(f"Available books in {self.name}: ")
        for book in self.books:
            print(book)

    def remove_book(self, title:str):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                return
        print(f"No book {title} found in book shelf.")



author_1 = Author(name="X", nationality="Hungarian")
author_2 = Author(name="Y", nationality="Bulgarian")

book_1 = Book(title="Adventures", genre="sci-fi", author=author_1)
book_2 = Book(title="Adventures 2", genre="sci-fi", author=author_1)

library_1 = Library(name="Szabó Ervin Város Könyvtár")
library_1.add_book(book=book_1)
library_1.add_book(book=book_2)

library_1.list_books()


