from table_operations.baseClass import baseClass
from tables import CustomerObj

class Customer(baseClass):
    def __init__(self):
        super().__init__("CUSTOMER", CustomerObj)

    def add(self, *values):
        '''
        @param person_id, username, email, password_hash, phone, active
        '''
        assert len(values) == 6
        query = self.insertIntoFlex("PERSON_ID", "USERNAME", "EMAIL", "PASS_HASH", "PHONE", "IS_ACTIVE")
        fill = (*values, )
        self.execute(query, fill)

    def update(self, new_values, update_columns, where_values, where_columns):
        self.updateGeneric(new_values, update_columns, where_values, where_columns)

    def delete(self, where_values, where_columns="CUSTOMER_ID"):
        self.deleteGeneric(where_values, where_columns)
    
    def get_row(self, where_columns, where_values, select_columns="*"):
        return self.getRowGeneric(where_columns, where_values, select_columns)

    def get_table(self, where_columns=None, where_values=None, select_columns="*"):
        return self.getTableGeneric(where_columns, where_values, select_columns)