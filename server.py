from flask import Flask, render_template
from database import Database
from book import Book

app = Flask(__name__)

db = Database()
db.add_book(Book("Enver", 2018, 6053326045, 784, "Türkiye İş Bankası Kültür Yayınları", 2))
db.add_book(Book("Hayvan Çiftliği", 2018, 9750719387, 152, "Can Yayınları", 55))
db.add_book(Book("Simyacı", 2018, 9750726439, 184, "Can Yayınları", 144))
db.add_book(Book("Göçüp Gidenler Koleksiyoncusu", 2018, 6602026351, 168, "Doğan Kitap", 1))
db.add_book(Book("Osmanlı Gerçekleri", 2018, 6050827644, 288, "Timaş Yayınları", 1))

@app.route("/")
def home_page():
    return render_template("home.html")

@app.route("/books")
def books_page():
    books = db.get_books()
    return render_template("books.html", books=sorted(books))

if __name__ == "__main__":
app.run()