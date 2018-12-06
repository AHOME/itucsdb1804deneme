import psycopg2 as dbapi2
import os
import sys

class baseClass:

    def __init__(self, table_name, constructor):
        self.tablename = table_name
        self.cons = constructor
        self.url = os.getenv("DATABASE_URL")
        if self.url is None:
            print("Usage: DATABASE_URL=url python database.py", file=sys.stderr)
            sys.exit(1)


    def deleteGeneric(self, where_values, where_columns):
        '''
        @param values (list), conditions (list)
        '''

        query = self.deleteFlex(where_columns)
        fill = (where_values, )
        self.execute(query, fill)

    def updateGeneric(self, new_values, update_columns, where_values, where_columns):
        query = self.updateFlex(where_columns, update_columns)
        fill = (*new_values, *where_values)
        self.execute(query, fill)

    def getRowGeneric(self, where_columns, where_values, select_columns):
        query = self.getRowFlex(where_columns, select_columns)
        fill = (where_values, )

        result = self.execute(query, fill)
        if result is not None:
            result = result[0]
            if select_columns == "*":
                result = self.cons(*result, )
            else:
                result = result[0]
        return result

    def getTableGeneric(self, where_columns=None, where_values=None, select_columns=None):
        results_list = []

        query = self.getTableFlex(where_columns, select_columns)
        fill = (where_values, ) if where_columns is not None else None

        result = self.execute(query, fill)        
        if result is not None:
            for it in result:
                results_list.append(self.cons(*it))

        return results_list



    def whereFlex(self, *where_columns):
        col_list = list(where_columns)
        col_count = len(col_list)
        return (" WHERE {} = %s" + (col_count-1)*(" AND {} = %s")).format(*where_columns, )

    def insertIntoFlex(self, *insert_columns):
        col_count = len(insert_columns)
        valStr = ("%s, "*(col_count-1)) + "%s"
        columnStr = ("{}, "*(col_count-1)) + "{}"
        return ("INSERT INTO {tab} ("+columnStr+") VALUES ({fill})").format(tab=self.tablename, fill=valStr, *insert_columns, )

    def deleteFlex(self, *where_columns):
        return ("DELETE FROM {tab})"+self.whereFlex(where_columns)).format(tab=self.tablename, )

    def updateFlex(self, update_columns, where_columns):
        #columns shows the columns that will be updated
        valStr = ("{} = %s, "*(len(update_columns)-1) + "{} = %s ").format(*update_columns, )
        return ("UPDATE {tab} SET ".format(tab=self.tablename, ))+valStr+self.whereFlex(where_columns)

    def getRowFlex(self, where_columns, select_columns="*"):
        selectStr = ("SELECT {}"+(", {}"*(len(select_columns)-1))).format(*select_columns)
        return selectStr+(" FROM {tab}").format(tab=self.tablename)+self.whereFlex(where_columns)

    def getTableFlex(self, where_columns, select_columns="*"):
        selectStr = ("SELECT {}"+(", {}"*(len(select_columns)-1))).format(*select_columns)
        return selectStr+(" FROM {tab}".format(tab=self.tablename))+self.whereFlex(where_columns)



    def execute(self, query, fill=None):
        result = []
        with dbapi2.connect(self.url) as connection:
            with connection.cursor() as curs:
                try:
                    print(curs.mogrify(query, fill))
                    curs.execute(query, fill)
                    result = curs.fetchall()
                except dbapi2.Error as err:
                    print("Error: %s", err)
        
        return None if len(result) == 0 else result
