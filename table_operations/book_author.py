from table_operations.baseClass import baseClass
from tables import Book_AuthorObj

class Book_Author(baseClass):
    def __init__(self):
        super().__init__("BOOK_AUTHOR", Book_AuthorObj)

    def add(self, book_id, author_id):
        query = self.insertIntoFlex("BOOK_ID", "AUTHOR_ID")
        fill = (book_id, author_id)
        self.execute(query, fill)

    def update(self, new_values, update_columns, where_values, where_columns):
        self.updateGeneric(new_values, update_columns, where_values, where_columns)

    def delete(self, where_values, where_columns):
        self.deleteGeneric(where_values, where_columns)
    
    def get_row(self, where_columns, where_values, select_columns="*"):
        return self.getRowGeneric(where_columns, where_values, select_columns)

    def get_table(self, where_columns=None, where_values=None, select_columns="*"):
        return self.getTableGeneric(where_columns, where_values, select_columns)