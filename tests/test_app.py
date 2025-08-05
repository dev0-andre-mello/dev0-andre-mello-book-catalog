from project.models import db, Book


def test_homepage_loads(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Book Catalog" in response.data


def test_add_book(client):
    data = {"title": "Clean Code", "autor": "Robert C. Martin", "year": 2008}
    response = client.post("/add", data=data, follow_redirects=True)
    assert response.status_code == 200
    assert b"Clean Code" in response.data
    assert b"Robert C. Martin" in response.data


def test_delete_book(client, app_with_db):
    with app_with_db.app_context():
        book = Book(title="To Delete", autor="Someone", year=2020)
        db.session.add(book)
        db.session.commit()

        response = client.post(f"/delete/{book.id}", follow_redirects=True)
        assert response.status_code == 200
        assert b"To Delete" not in response.data
