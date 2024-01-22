import os
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
Bootstrap5(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"
db = SQLAlchemy(app)

# CREATE DB
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255),unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(255), nullable=False)
    rating = db.Column(db.Float,nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(255), nullable=True)
    img_url = db.Column(db.String(255), nullable=False)
# CREATE TABLE
with app.app_context():
    db.create_all()

# CREATE EDIT FORM
class RateMovieForm(FlaskForm):
    rating = StringField("Your Rating Out of 10 e.g. 7.5")
    review = StringField("Your Review")
    submit = SubmitField("Submit")

@app.route("/")
def home():
    movie_data = db.session.execute(db.select(Movie).order_by(Movie.title))
    all_movies = list(movie_data.scalars())
    for movie in all_movies:
        print(f"Name:{movie.title}")
    return render_template("index.html",movies=all_movies)

@app.route('/edit',methods=["GET", "POST"])
def edit():
    form = RateMovieForm()
    movie_id = request.args.get('id')
    movie = db.get_or_404(Movie,movie_id)
    if form.validate_on_submit():
        try:
            movie.rating = float(form.rating.data)
        except ValueError:
            movie.rating = movie.rating
        finally:
            movie.review = form.review.data
            db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html',movie=movie,form=form)

@app.route('/delete')
def delete():
    movie_id = request.args.get('id')
    movie_to_delete = db.get_or_404(Movie,movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
