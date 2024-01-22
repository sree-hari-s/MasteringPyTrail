import os
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
Bootstrap5(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"
db = SQLAlchemy(app)

MOVIE_DB_API_KEY=os.environ['API_KEY']
MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"
MOVIE_DB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie?query=avatar&include_adult=false&language=en-US&page=1"

headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {os.environ['ACCESS_TOKEN']}"
}
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

class FindMovieForm(FlaskForm):
    title = StringField("Movie Title",validators=[DataRequired()])
    submit = SubmitField("Submit")

@app.route("/")
def home():
    movie_data = db.session.execute(db.select(Movie).order_by(Movie.rating))
    all_movies = list(movie_data.scalars())
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
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

@app.route('/add', methods=['GET','POST'])
def add():
    form = FindMovieForm()
    if form.validate_on_submit():
        movie_title = form.title.data
        response = requests.get(MOVIE_DB_SEARCH_URL,headers=headers,params={
            'api_key': MOVIE_DB_API_KEY,
            'query':movie_title
        })
        data = response.json()['results']
        return render_template('select.html',options = data)
    return render_template('add.html',form = form)

@app.route("/find")
def find_movie():
    movie_api_id = request.args.get('id')
    if movie_api_id:
        movie_api_url = f"https://api.themoviedb.org/3/movie/{movie_api_id}"
        response = requests.get(movie_api_url,headers=headers,params={
            "api_key":MOVIE_DB_API_KEY,
            "language":"en-US"
        })
        data = response.json()
        new_movie = Movie(
            title=data['title'],
            year = data['release_date'].split('-')[0],
            img_url=f"{MOVIE_DB_IMAGE_URL}/{data['poster_path']}",
            description = data['overview'],
            rating = data['vote_average'],
            review = ''
        )                                          
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("home"))

if __name__ == '__main__':
    app.run(debug=True)
