#4. Sukurkite paprastą bibliotekos sistemą su knygomis, nariais ir skolintomis knygomis.

#	4.1 Sukurkite bazinę klasę Book su atributais title, author ir isbn (knygis id).
class Book:
    def __init__(self, title, author, isbn) -> None:
        self.title = title
        self.author = author
        self.isbn = isbn
#	4.2 Sukurkite bazinę klasę Member su atributais name ir member_id.
class Member:
    def __init__(self, name, member_id) -> None:
        self.name = name
        self.member_id = member_id
        
#	4.3 Sukurkite išvestinę klasę BorrowedBook, kuri paveldi iš Book ir prideda atributus borrower_name (member vardas kuris pasiėmė knygą) ir due_date (iki kada pasiėmė).
class BorrowedBook(Book):
    def __init__(self, title, author, isbn, borrower_name, due_date) -> None:
        super().__init__(title, author, isbn)
        self.borrower_name = borrower_name
        self.due_date = due_date

#	4.4. Sukurkite Member ir imituokite bibliotekos veiklą.

member1 = Member("Matas", "A000")

book1 = BorrowedBook("Life of the kardashians", "Kanye west", "YE1", member1.name, "1973-04-20")



