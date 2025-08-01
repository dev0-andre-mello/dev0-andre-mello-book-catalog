from flask import Flask, render_template
from models import db, Book

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///book.db"
app.config["SQLALCHEMY_TRACK_NOTIFICATIONS"] = False

db.init_app(app)


@app.route("/")
def index():
    return "<h1>Catálogo de Livros</h1>"


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
