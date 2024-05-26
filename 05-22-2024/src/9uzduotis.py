#9 užduotis
#	9.1 Apibrėžkite klasę Book su atributais title, author ir available (numatytoji reikšmė yra True).
#	9.2 Apibrėžkite klasę Library su atributu books (Book objektų sąrašas).
#	9.3 Į Library pridėkite metodus: add_book - pridėti knygą, borrow_book - pasiskolinti knygą (nustatykite, kad available yra False) ir return_book - grąžinti knygą (nustatykite, kad available yra True).
#	9.4 Sukurkite Library ir Book objektus ir imituokite knygų skolinimąsi bei grąžinimą.

class Book:
    def __init__(self, title: str, author: str, available = True) -> None:
        self.title = title
        self.author = author
        self.available = available

class Library:
    def __init__(self, books = []):
        self.books = books

    def add_book(self, title, author):
        self.books.append(Book(title, author))
    
    def borrow_book(self, title:str, author:str):
        for book in self.books:
            if book.title == title and book.author == author:
                book.availability = False
            else:
                print("No such book")
    
    def return_book(self, title:str, author:str):
        for book in self.books:
            if book.title == title and book.author == author:
                book.availability = True
            else:
                print("No such book")

mylib = Library()

