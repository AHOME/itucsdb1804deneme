from book import Book

class Database:
    def __init__(self):
        self.books = {}
        self._last_book_key = 0

    def add_book(self, book):
        book.ID = self._last_book_key
        self._last_book_key += 1
        self.books[self._last_book_key] = book

    def delete_book(self, book_key):
        if book_key in self.books:
            del self.books[book_key]

    def get_book(self, book_key):
        book = self.book.get(book_key)
        if book is None:
            return None
        book_ = Book(book.name, book.year, book.isbn, book.numberOfPage, book.publisher, book.edition, ID=book.ID)
        return book_

    def get_books(self):
        books = []
        for book_key, book in self.books.items():
            book_ = Book(book.name, book.year, book.isbn, book.numberOfPage, book.publisher, book.edition, ID=book.ID)
            books.append((book_key, book_))
        return books