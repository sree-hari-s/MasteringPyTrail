import requests
from flask import Flask,render_template
from post import Post

response = requests.get('https://api.npoint.io/79af83afe03463a29f67')
data = response.json()
post_objects = []
for post in data:
    post_obj = Post(post['id'],post['body'],post['date'],post['image'],post['title'],post['author'],post['subtitle'])
    post_objects.append(post_obj)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',all_posts=post_objects)

@app.route('/post/<int:id>')
def post(id):
    requested_post = None
    for post in post_objects:
        if post.id == id:
            requested_post = post
    return render_template('post.html',post=requested_post)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')