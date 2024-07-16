from book import Book
from file_handler import FileHandler
from utils import get_float_input, get_int_input

def main():
    library = FileHandler.load_library("library_data.json")

    while True:
        print("\nLibrary Management System")
        print("1. Add a book")
        print("2. View all books")
        print("3. Search books")
        print("4. Search books by author")
        print("5. Remove a book")
        print("6. Lend a book")
        print("7. View lent books")
        print("8. Return a book")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book(library)
        elif choice == "2":
            library.view_all_books()
        elif choice == "3":
            search_books(library)
        elif choice == "4":
            search_by_author(library)
        elif choice == "5":
            remove_book(library)
        elif choice == "6":
            lend_book(library)
        elif choice == "7":
            library.view_lent_books()
        elif choice == "8":
            return_book(library)
        elif choice == "0":
            print("Thank you for using the Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

        FileHandler.save_library(library, "library_data.json")

def add_book(library):
    title = input("Enter book title: ")
    authors = input("Enter author(s) (comma-separated): ").split(",")
    isbn = input("Enter ISBN: ")
    year = get_int_input("Enter publishing year: ")
    price = get_float_input("Enter price: ")
    quantity = get_int_input("Enter quantity: ")

    book = Book(title, authors, isbn, year, price, quantity)
    library.add_book(book)
    print("Book added successfully.")

def search_books(library):
    search_term = input("Enter search term (title or ISBN): ")
    results = library.search_books(search_term)
    if results:
        print("Search results:")
        for book in results:
            print(book)
    else:
        print("No books found.")

def search_by_author(library):
    author_name = input("Enter author name: ")
    results = library.search_by_author(author_name)
    if results:
        print("Search results:")
        for i, book in enumerate(results, 1):
            print(f"{i}. {book}")

    else:
        print("No books found.")

def remove_book(library):
    search_term = input("Enter search term (title or ISBN): ")
    results = library.search_books(search_term)
    if results:
        print("Search results:")
        for i, book in enumerate(results, 1):
            print(f"{i}. {book}")
        choice = get_int_input("Enter the number of the book to remove: ") - 1
        if 0 <= choice < len(results):
            if library.remove_book(results[choice]):
                print("Book removed successfully.")
            else:
                print("Error: Book not found in the library.")
        else:
            print("Invalid choice.")
    else:
        print("No books found.")

def lend_book(library):
    search_term = input("Enter search term (title or ISBN): ")
    results = library.search_books(search_term)
    if results:
        print("Search results:")
        for i, book in enumerate(results, 1):
            print(f"{i}. {book}")
        choice = get_int_input("Enter the number of the book to lend: ") - 1
        if 0 <= choice < len(results):
            borrower = input("Enter borrower's name: ")
            if library.lend_book(results[choice], borrower):
                print("Book lent successfully.")
            else:
                print("Error: Not enough books available to lend.")
        else:
            print("Invalid choice.")
    else:
        print("No books found.")

def return_book(library):
    borrower = input("Enter borrower's name: ")
    if borrower in library.lent_books:
        print("Books borrowed by", borrower)
        for i, book in enumerate(library.lent_books[borrower], 1):
            print(f"{i}. {book}")
        choice = get_int_input("Enter the number of the book to return: ") - 1
        if 0 <= choice < len(library.lent_books[borrower]):
            book = library.lent_books[borrower][choice]
            if library.return_book(book, borrower):
                print("Book returned successfully.")
            else:
                print("Error: Book not found in the lent books list.")
        else:
            print("Invalid choice.")
    else:
        print("No books lent to this borrower.")

if __name__ == "__main__":
    main()