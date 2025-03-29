class Member:
    members = []

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.borrowed_books: list['Book'] = []
        Member.members.append({'name': name, 'age': age})

    def view_borrowed_books(self):
        for book in self.borrowed_books:
            book.display_details()


class Book:
    def __init__(self, title, author, ISBN, num_of_copies=1):
        self.title = title
        self.author = author
        self.isbn = ISBN
        self.num_of_copies = num_of_copies

    def display_details(self):
        print(f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Number Of Copies: {self.num_of_copies}")


class Library:
    books = []

    def display_books(self):
        for book in Library.books:
            book.display_details()

    def add_book(self, book: Book):
        Library.books.append(book)

    def borrow_book(self, member: Member, book: Book):
        if book in member.borrowed_books:
            print("Book is already borrowed.")
        else:
            print(f"{member.name} is Borrowing Book: {book.title}")
            if book.num_of_copies == 1:
                Library.books.remove(book)
            else:
                book.num_of_copies -= 1
            member.borrowed_books.append(book)

    def return_book(self, member: Member, book: Book):
        if book not in member.borrowed_books:
            print(f"Member {member.name} has not borrowed book. Cannot return")
        else:
            print(f"Member {member.name} is returning book: {book.title}")
            if book.num_of_copies == 0:
                Library.books.append(book)
            else:
                book.num_of_copies += 1


member = Member("Jafar", 12)
member2 = Member("Akash", 33)
book1 = Book("Title", 12, 32, 2)
library = Library()

library.add_book(book1)

library.display_books()
library.borrow_book(member, book1)
library.return_book(member2, book1)
