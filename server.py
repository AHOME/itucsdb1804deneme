from flask import Flask, render_template
from database import Database
from tables import *
import datetime

app = Flask(__name__)

db = Database()
bookdb = db.book


@app.route("/")
def home_page():
    return render_template("home.html")

@app.route("/customers")
def customers_page():
    customers = db.customer.get_table()
    return render_template("customers.html", customers=sorted(customers))

if __name__ == "__main__":
    app.run()
