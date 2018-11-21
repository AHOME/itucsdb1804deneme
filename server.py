from flask import Flask, render_template
from database import Database
from tables import Book, Store
import datetime

app = Flask(__name__)

db = Database()
bookdb = db.book
bookdb.add_book(Book("Enver", 2018, "tip1", 6053326045, 784, "Türkiye İş Bankası Kültür Yayınları"))
bookdb.add_book(Book("Hayvan Çiftliği", 2018, "tür2", 9750719387, 152, "Can Yayınları"))
bookdb.add_book(Book("Simyacı", 2018, "tür1", 9750726439, 184, "Can Yayınları"))
bookdb.add_book(Book("Göçüp Gidenler Koleksiyoncusu", 2018, "tür3", 6602026351, 168, "Doğan Kitap"))
bookdb.add_book(Book("Osmanlı Gerçekleri", 2018, "tür2", 6050827644, 288, "Timaş Yayınları"))
bookdb.update_book(5,Book("5Osmanlı Gerçekleri", 52018, "5tür2", 56050827644, 5288, "5Timaş Yayınları"))

db.store.add(Store("Store name 1", "+901234567899", 1, "email@gmail.com", datetime.date(2005, 11, 18), "1 explanation explanation explanationex planationexp lanation "))
db.store.add(Store("Store name 2", "+904563348645", 2, "email2@gmail.com", datetime.date(2015, 1, 8), "2 explanation explanation explanationex planationexp lanation "))
db.store.add(Store("Store name 3", "+901456453213", 3, "email3@gmail.com", datetime.date(2018, 8, 25), "3 explanation explanation explanationex planationexp lanation "))
    
@app.route("/")
def home_page():
    return render_template("home.html")

@app.route("/books")
def books_page():
    books = bookdb.get_books()
    return render_template("books.html", books=sorted(books))

@app.route("/stores")
def stores_page():
    stores = db.store.get()
    return render_template("stores.html", stores=sorted(stores))

if __name__ == "__main__":
    app.run()
