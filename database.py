from tables import *
import psycopg2 as dbapi2
import os
import sys


class Database:
    def __init__(self):
        url = os.getenv("DATABASE_URL")
        if url is None:
            print("Usage: DATABASE_URL=url python database.py", file=sys.stderr)
            sys.exit(1)
        self.customer = self.Customer(url)

    class Customer:
        def __init__(self, url):
            self.url = url
            self.dbname = "CUSTOMER"
        
        def add(self, customer):
            query = "INSERT INTO CUSTOMER (PERSON_ID, USERNAME, EMAIL, PASS_HASH, PHONE, IS_ACTIVE) VALUES (%s, %s, %s, %s, %s, %s)"    
            fill = (customer.person_id, customer.username, customer.email, customer.pass_hash, customer.phone, customer.is_active)

            with dbapi2.connect(self.url) as connection:
                cursor = connection.cursor()
                cursor.execute(query, fill)
                cursor.close()
        
        def update(self, customer):
            query = "UPDATE CUSTOMER SET USERNAME = %s, EMAIL = %s, PASS_HASH = %s, PHONE = %s, IS_ACTIVE = %s WHERE (CUSTOMER_ID = %s)"
            fill = (customer.username, customer.email, customer.pass_hash, customer.phone, customer.is_active, customer.customer_id)

            with dbapi2.connect(self.url) as connection:
                cursor = connection.cursor()
                cursor.execute(query, fill)
                cursor.close()

        def delete(self, customer):
            query = "DELETE FROM CUSTOMER WHERE CUSTOMER_ID = %s"
            fill = (customer.customer_id)

            with dbapi2.connect(self.url) as connection:
                cursor = connection.cursor()
                cursor.execute(query, fill)
                cursor.close()

        def get_row(self, cust_id):
            _customer = None

            query = "SELECT * FROM CUSTOMER WHERE CUSTOMER_ID = %s"
            fill = (cust_id)

            with dbapi2.connect(self.url) as connection:
                cursor = connection.cursor()
                cursor.execute(query, fill)
                customer = cursor.fetchone()
                if customer is not None:
                    _customer = Customer(customer[0], customer[1], customer[2], customer[3], customer[4], customer[5], customer[6])

            return _customer

        def get_table(self):
            customers = []

            query = "SELECT * FROM CUSTOMER;"

            with dbapi2.connect(self.url) as connection:
                cursor = connection.cursor()
                cursor.execute(query)
                for customer in cursor:
                    customer_ = Customer(customer[0], customer[1], customer[2], customer[3], customer[4], customer[5], customer[6])
                    customers.append(customer_)
                cursor.close()

            return customers