from table_operations.baseClass import baseClass
from tables import AddressObj

class Address(baseClass):
    def __init__(self):
        super().__init__("ADDRESS", AddressObj)

    def add(self, *values):
        '''
        @params address_name, country, city, district, neighborhood, avenue, street, addr_number, zipcode, explanation
        '''
        assert len(values) == 10
        query = self.insertIntoFlex("ADDRESS_NAME", "COUNTRY", "CITY", "DISTRICT", "NEIGHBORHOOD", "AVENUE", "STREET", "ADDR_NUMBER", "ZIPCODE", "EXPLANATION")
        fill = (*values, )
        self.execute(query, fill)


    def update(self, new_values, update_columns, where_values, where_columns):
        self.updateGeneric(new_values, update_columns, where_values, where_columns)

    def delete(self, where_values, where_columns="ADDRESS_ID"):
        self.deleteGeneric(where_values, where_columns)
    
    def get_row(self, where_columns, where_values, select_columns="*"):
        return self.getRowGeneric(where_columns, where_values, select_columns)

    def get_table(self, where_columns=None, where_values=None, select_columns="*"):
        return self.getTableGeneric(where_columns, where_values, select_columns)
