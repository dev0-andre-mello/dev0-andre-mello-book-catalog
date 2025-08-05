from project.models import db, Book


def test_create_book():
    book = Book(title="Test Title", autor="Test Author", year=2020)

    assert book.title == "Test Title"
    assert book.autor == "Test Author"
    assert book.year == 2020
    assert repr(book) == "Book Test Title"


def test_add_book_to_db(app_with_db):
    with app_with_db.app_context():
        book = Book(title="DB Title", autor="DB Author", year=2021)
        db.session.add(book)
        db.session.commit()

        queried = Book.query.filter_by(title="DB Title").first()
        assert queried is not None
        assert queried.autor == "DB Author"
        assert queried.year == 2021


def test_delete_book_from_db(app_with_db):
    with app_with_db.app_context():
        book = Book(title="Delete Me", autor="Author", year=2019)
        db.session.add(book)
        db.session.commit()

        db.session.delete(book)
        db.session.commit()

        queried = Book.query.filter_by(title="Delete Me").first()
        assert queried is None
