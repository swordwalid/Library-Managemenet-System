class Library:
    def __init__(self):
        self.books = []
        self.lent_books = {}

    def add_book(self, book):
        self.books.append(book)

    def view_all_books(self):
        if not self.books:
            print("No books available.")
        for book in self.books:
            print(f"{book} - Price: ${book.price:.2f}, Quantity: {book.quantity}")


    def search_books(self, search_term):
        results = []
        for book in self.books:
            if search_term.lower() in book.title.lower() or search_term.lower() in book.isbn.lower():
                results.append(book)
        return results

    def search_by_author(self, author_name):
        results = []
        for book in self.books:
            if any(author_name.lower() in author.lower() for author in book.authors):
                results.append(book)
        return results

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            return True
        return False

    def lend_book(self, book, borrower):
        if book.quantity > 0:
            book.quantity -= 1
            if borrower not in self.lent_books:
                self.lent_books[borrower] = []
            self.lent_books[borrower].append(book)
            return True
        return False

    def view_lent_books(self):
        for borrower, books in self.lent_books.items():
            print(f"{borrower}:")
            for book in books:
                print(f"  - {book}")

    def return_book(self, book, borrower):
        if borrower in self.lent_books and book in self.lent_books[borrower]:
            self.lent_books[borrower].remove(book)
            book.quantity += 1
            if not self.lent_books[borrower]:
                del self.lent_books[borrower]
            return True
        return False