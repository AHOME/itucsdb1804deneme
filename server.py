from flask import Flask, render_template
from database import Database
from book import Book

app = Flask(__name__)


@app.route("/")
def home_page():
    return render_template("home.html")

db = Database()
db.add_book(Book("Enver", 2018, 6053326045, 784, "TÜRKİYE İŞ BANKASI KÜLTÜR YAYINLARI", 2))
db.add_book(Book("Osmanlı Gerçekleri", 2018, 6050827644, 288, "Timaş Yayınları", 1))

@app.route("/books")
def books_page():
    books = db.get_books()
    return render_template("books.html", books=sorted(books))

if __name__ == "__main__":
    app.run()