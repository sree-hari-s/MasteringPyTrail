from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Create a SQLite database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# Define the Book model
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<Book {self.title}>"

# Create tables
with app.app_context():
    db.create_all()

# Create a new book record
with app.app_context():
    new_book = Book(title="Harry Potter", author="J. K. Rowling", rating=9.3)
    db.session.add(new_book)
    db.session.commit()

# Read all books
with app.app_context():
    all_books = Book.query.order_by(Book.title).all()

# Read a particular record by query
with app.app_context():
    book = Book.query.filter_by(title="Harry Potter").first()

# Update a particular record by query
with app.app_context():
    book_to_update = Book.query.filter_by(title="Harry Potter").first()
    if book_to_update:
        book_to_update.title = "Harry Potter and the Chamber of Secrets"
        db.session.commit()

# Update a record by PRIMARY KEY
book_id = 1
with app.app_context():
    book_to_update = db.session.get(Book, book_id)
    if book_to_update:
        book_to_update.title = "Harry Potter and the Goblet of Fire"
        db.session.commit()

# Delete a particular record by PRIMARY KEY
book_id = 1
with app.app_context():
    book_to_delete = db.session.get(Book, book_id)
    if book_to_delete:
        db.session.delete(book_to_delete)
        db.session.commit()

