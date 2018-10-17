from flask import Flask
import views

def create_app():
    app = Flask(__name__)

    app.add_url_rule("/", view_func=views.home_page)
    app.add_url_rule("/books", view_func=views.books_page)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run()
