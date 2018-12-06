from table_operations.baseClass import baseClass
from tables import CategoryObj

class Category(baseClass):
    def __init__(self):
        super().__init__("CATEGORY", CategoryObj)

    def add(self, category_name):
        query = "INSERT INTO CATEGORY (CATEGORY_NAME) VALUES (%s)"
        fill = (category_name)
        self.execute(query, fill)

    def update(self, new_values, update_columns, where_values, where_columns):
        self.updateGeneric(new_values, update_columns, where_values, where_columns)

    def delete(self, where_values, where_columns="CATEGORY_ID"):
        self.deleteGeneric(where_values, where_columns)
    
    def get_row(self, where_columns, where_values, select_columns="*"):
        return self.getRowGeneric(where_columns, where_values, select_columns)

    def get_table(self, where_columns=None, where_values=None, select_columns="*"):
        return self.getTableGeneric(where_columns, where_values, select_columns)