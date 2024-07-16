import json
from book import Book
from library import Library


class FileHandler:
    @staticmethod
    def save_library(library, filename):
        data = {
            "books": [
                {
                    "title": book.title,
                    "authors": book.authors,
                    "isbn": book.isbn,
                    "year": book.year,
                    "price": book.price,
                    "quantity": book.quantity
                }
                for book in library.books
            ],
            "lent_books": {
                borrower: [book.__dict__ for book in books]
                for borrower, books in library.lent_books.items()
            }
        }
        with open(filename, "w") as f:
            json.dump(data, f)

    @staticmethod
    def load_library(filename):
        try:
            with open(filename, "r") as f:
                data = json.load(f)

            library = Library()
            library.books = [Book(**book_data) for book_data in data["books"]]
            library.lent_books = {
                borrower: [Book(**book_data) for book_data in books]
                for borrower, books in data["lent_books"].items()
            }
            return library
        except FileNotFoundError:
            return Library()