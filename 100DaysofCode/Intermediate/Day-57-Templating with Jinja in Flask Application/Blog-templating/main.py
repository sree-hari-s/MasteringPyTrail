from flask import Flask, render_template
from post import Post
import requests

posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
post_objects = []
for post in posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html",all_posts=post_objects)

@app.route('/post/<int:id>')
def show_post(id):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == id:
            requested_post = blog_post
    return render_template("post.html",post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)
