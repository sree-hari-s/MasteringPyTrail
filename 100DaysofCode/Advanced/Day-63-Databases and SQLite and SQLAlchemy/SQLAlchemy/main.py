from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

##CREATE DATABASE
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
# Optional: But it will silence the deprecation warning in the console.
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


##CREATE TABLE
with app.app_context():

    class Book(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String(250), unique=True, nullable=False)
        author = db.Column(db.String(250), nullable=False)
        rating = db.Column(db.Float, nullable=False)

        # Optional: this will allow each book object to be identified by its title when printed.
        def __repr__(self):
            return f"<Book {self.title}>"

    db.create_all()

    # CREATE RECORD
    new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)
    db.session.add(new_book)
    db.session.commit()
