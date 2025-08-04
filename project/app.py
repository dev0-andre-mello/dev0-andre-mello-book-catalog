from flask import Flask, render_template, request, url_for, redirect
from models import db, Book

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///book.db"
app.config["SQLALCHEMY_TRACK_NOTIFICATIONS"] = False
db.init_app(app)


@app.route("/")
def index():
    books = Book.query.all()
    return render_template("index.html", books=books)


@app.route("/add", methods=["GET", "POST"])
def add_book():
    if request.method == "POST":
        title = request.form["title"]
        autor = request.form["autor"]
        year = request.form["year"]

        new_book = Book(title=title, autor=autor, year=year)
        db.session.add(new_book)
        db.session.commit()

        return redirect(url_for("index"))
    return render_template("add_book.html")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
