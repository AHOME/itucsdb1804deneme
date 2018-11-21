import os
import sys

import psycopg2 as dbapi2


INIT_STATEMENTS = [
    "CREATE DOMAIN GENDERTYPE AS CHAR(1) CHECK ((VALUE = 'M') OR (VALUE = 'F') OR (VALUE = 'O')) ",
    "CREATE TABLE PERSON (ID SERIAL PRIMARY KEY, NAME VARCHAR(40) NOT NULL, SURNAME VARCHAR(40) NOT NULL, GENDER GENDERTYPE NOT NULL, DATEOFBIRTH DATE NOT NULL, NATIONALITY VARCHAR(40))",
    "CREATE TABLE CUSTOMER (CUSTOMER_ID SERIAL PRIMARY KEY, PERSON_ID INTEGER REFERENCES PERSON (ID), USERNAME VARCHAR(20) UNIQUE NOT NULL, PHONE INTEGER UNIQUE NOT NULL, EMAIL VARCHAR(50) UNIQUE NOT NULL, IS_ACTIVE BOOLEAN DEFAULT TRUE)",
    "CREATE TABLE ADDRESS (ADDRESS_ID SERIAL PRIMARY KEY, COUNTRY VARCHAR(40) NOT NULL, CITY VARCHAR(40) NOT NULL, DISTRICT VARCHAR(40) NOT NULL, NEIGHBORHOOD VARCHAR(40) NOT NULL, AVENUE VARCHAR(40) NOT NULL, STREET VARCHAR(40) NOT NULL, ADDR_NUM INTEGER NOT NULL, ZIPCODE INTEGER, DIRECTIONS VARCHAR(200), ADDRESS_NAME VARCHAR(30) NOT NULL)",
    "CREATE TABLE BOOK (BOOK_ID SERIAL PRIMARY KEY, NAME VARCHAR(40) NOT NULL, WRITINGYEAR INTEGER NOT NULL, TYPE VARCHAR(40) NOT NULL, ISBN VARCHAR(20) NOT NULL, NUMBEROFPAGES INTEGER NOT NULL, PUBLISHER VARCHAR(40) NOT NULL)",
    #"CREATE TABLE STORE (STORE_ID SERIAL PRIMARY KEY, NAME VARCHAR(40) NOT NULL, PHONE VARCHAR(15) NOT NULL, ADRESS_ID INTEGER REFERENCES ADDRESS (ADDRESS_ID), EMAIL VARCHAR(50) UNIQUE NOT NULL, OPENEDDATE DATE NOT NULL, EXPLANATION VARCHAR(200) NOT NULL)",
    "CREATE TABLE STORE (STORE_ID SERIAL PRIMARY KEY, NAME VARCHAR(40) NOT NULL, PHONE VARCHAR(15) NOT NULL, ADRESS_ID INTEGER NOT NULL, EMAIL VARCHAR(50) NOT NULL, OPENEDDATE DATE NOT NULL, EXPLANATION VARCHAR(200) NOT NULL)",
    "CREATE TABLE COMMENT (COMMENT_ID SERIAL PRIMARY KEY, CUSTOMER_ID INTEGER REFERENCES CUSTOMER (CUSTOMER_ID), TITLE VARCHAR(30) NOT NULL, EXPLANATION VARCHAR(200) NOT NULL, UPDATETIME DATE NOT NULL, POINTTOBOOK INTEGER NOT NULL)",
]


def initialize(url):
    with dbapi2.connect(url) as connection:
        cursor = connection.cursor()
        for statement in INIT_STATEMENTS:
            cursor.execute(statement)
        cursor.close()


if __name__ == "__main__":
    url = os.getenv("DATABASE_URL")
    if url is None:
        print("Usage: DATABASE_URL=url python dbinit.py", file=sys.stderr)
        sys.exit(1)
    initialize(url)
