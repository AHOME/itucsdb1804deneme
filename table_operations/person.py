from table_operations.baseClass import baseClass
from tables import PersonObj

class Person(baseClass):
    def __init__(self):
        super().__init__("PERSON", PersonObj)

    def add(self, *values):
        '''
        @param person_name, person_surname, gender, date_of_birth, nationality
        '''
        assert len(values) == 5
        query = self.insertIntoFlex("PERSON_NAME", "SURNAME", "GENDER", "DATE_OF_BIRTH", "NATIONALITY") + "RETURNING PERSON_ID"
        fill = (*values, )
        last_id = self.execute(query, fill)[0]
        return last_id if last_id != None else -1


    def update(self, new_values, update_columns, where_values, where_columns):
        self.updateGeneric(new_values, update_columns, where_values, where_columns)

    def delete(self, where_values, where_columns="PERSON_ID"):
        self.deleteGeneric(where_values, where_columns)
    
    def get_row(self, where_columns, where_values, select_columns="*"):
        return self.getRowGeneric(where_columns, where_values, select_columns)

    def get_table(self, where_columns=None, where_values=None, select_columns="*"):
        return self.getTableGeneric(where_columns, where_values, select_columns)