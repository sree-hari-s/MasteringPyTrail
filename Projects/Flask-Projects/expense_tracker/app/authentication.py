# authentication.py

from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a strong, random secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expense_tracker.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)

def register_user(username, password):
    new_user = User(username=username, password=password)
    db.session.add(new_user)
    db.session.commit()

def login_user(username, password):
    user = User.query.filter_by(username=username, password=password).first()
    return user

# Routes for user registration and login...

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
