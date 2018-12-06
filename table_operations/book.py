from table_operations.baseClass import baseClass
from tables import BookObj
import psycopg2 as dbapi2

class Book(baseClass):
    def __init__(self):
        super().__init__("BOOK", BookObj)

    def add_book(self, book):
        query = "INSERT INTO BOOK (BOOK_NAME, RELEASE_YEAR, BOOK_EXPLANATION) VALUES (%s, %s, %s)"
        fill = (book.book_name, book.release_year, book.explanation)

        with dbapi2.connect(self.url) as connection:
            cursor = connection.cursor()
            cursor.execute(query, fill)
            cursor.close()

    def update(self, book_key, book):
        query = "UPDATE BOOK SET BOOK_NAME = %s, RELEASE_YEAR = %s, BOOK_EXPLANATION = %s WHERE BOOK_ID = %s"
        # TODO book_key or book.book_id
        fill = (book.book_name, book.release_year, book.explanation, book_key)

        with dbapi2.connect(self.url) as connection:
            cursor = connection.cursor()
            cursor.execute(query, fill)
            cursor.close()

    def delete(self, book_key):
        if type(book_key) == int:
            book_key = str(book_key)

        query = "DELETE FROM BOOK WHERE BOOK_ID = %s"
        fill = (book_key)

        with dbapi2.connect(self.url) as connection:
            cursor = connection.cursor()
            cursor.execute(query, fill)
            cursor.close()

    def get_row(self, book_key):
        _book = None
        if type(book_key) == int:
            book_key = str(book_key)

        query = "SELECT * FROM BOOK WHERE BOOK_ID = %s"
        fill = (book_key)

        with dbapi2.connect(self.url) as connection:
            cursor = connection.cursor()
            cursor.execute(query, fill)
            book = cursor.fetchone()
            if book is not None:
                _book = BookObj(book[1], book[2], book[3])

        return _book

    def get_table(self):
        books = []

        query = "SELECT * FROM BOOK;"

        with dbapi2.connect(self.url) as connection:
            cursor = connection.cursor()
            cursor.execute(query)
            for book in cursor:
                book_ = BookObj(book[1], book[2], book[3], book_id=book[0])
                books.append((book[0], book_))
            cursor.close()

        return books
