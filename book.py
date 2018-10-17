class Book:
    def __init__(self, name, year, isbn, numberOfPage, publisher, edition, ID=-1):
        self.ID = ID
        self.name = name
        self.year = year
        self.isbn = isbn
        self.numberOfPage = numberOfPage
        self.publisher = publisher
        self.edition = edition
