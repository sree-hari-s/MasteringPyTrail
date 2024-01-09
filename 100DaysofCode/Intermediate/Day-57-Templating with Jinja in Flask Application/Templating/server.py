import requests
from datetime import datetime as dt
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    current_year = dt.now().year
    return render_template("index.html", current_year=current_year)


@app.route("/guess/<name>")
def guess(name):
    age_url = f"https://api.agify.io?name={name}"
    gender_url = f"https://api.genderize.io?name={name}"
    age_response = requests.get(age_url)
    age_data = age_response.json()
    age = age_data["age"]
    print(age)
    gender_response = requests.get(gender_url)
    gender_data = gender_response.json()
    gender = gender_data["gender"]
    print(gender)
    return render_template("index.html", name=name.title(), gender=gender, age=age)


@app.route("/blogs")
def blog():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_blogs = response.json()
    current_year = dt.now().year
    return render_template("blog.html", blogs=all_blogs, current_year=current_year)


if __name__ == "__main__":
    app.run(debug=True)
