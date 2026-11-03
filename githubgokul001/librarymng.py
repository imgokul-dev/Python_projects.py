class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"{book.title} added to the library.")

    def display_books(self):
        if not self.books:
            print("No books available")
            return

        print("\n----Library Books----")

        for book in self.books:
            status = "borrowed" if book.is_borrowed else "Available"
            print(f"Title: {book.title} | Author: {book.author} | Status: {status}")

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.is_borrowed:
                    print(f"{book.title} is already borrowed.")
                else:
                    book.is_borrowed = True
                    print(f"You borrowed {book.title}")
                return
        print("Book not found")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if not book.is_borrowed:
                    print(f"{book.title} was not borrowed")
                else:
                    book.is_borrowed = False
                    print(f"You returned {book.title}.")
                return
        print("Book not found")


library = Library()

book1 = Book("Python Basics", "gokul")
book2 = Book("Learn C++", "krishnan")
book3 = Book("Java programming", "robert")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

library.display_books()
library.borrow_book("python basics")
library.display_books()
library.return_book("python basics")
library.display_books()

                
                
                        

    



          

                 
          

