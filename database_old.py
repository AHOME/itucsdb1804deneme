from tables import Book

class Database:
    def __init__(self):
        self.book = self.Book()

    class Book:
        def __init__(self):
            self.books = {}
            self._last_book_key = 0

        def add_book(self, book):
            self._last_book_key += 1
            self.books[self._last_book_key] = book

        def delete_book(self, book_key):
            if book_key in self.books:
                del self.books[book_key]

        def get_book(self, book_key):
            book = self.book.get(book_key)
            if book is None:
                return None
            book_ = Book(book.name, book.date, book.type, book.isbn, book.numberOfPage, book.publisher)
            return book_

        def get_books(self):
            books = []
            for book_key, book in self.books.items():
                book_ = Book(book.name, book.date, book.type, book.isbn, book.numberOfPage, book.publisher)
                books.append((book_key, book_))
            return books

    class Store:
        def __init__(self):
            self.stores = {}
            self._last_store_key = 0

        def add_store(self, store):
            self._last_store_key += 1
            self.stores[self._last_store_key] = store
