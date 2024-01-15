import os
import requests
import smtplib
from flask import Flask,render_template,request
from post import Post
from dotenv import load_dotenv

load_dotenv()
OWN_EMAIL=os.environ['EMAIL']
OWN_PASSWORD=os.environ['PASSWORD']

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

@app.route('/contact',methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        data = request.form
        name = data.get("name")
        email = data.get("email")
        phone = data.get("phone")
        message = data.get("message")
        send_email(name,email,phone,message)
        return render_template('contact.html',msg_sent = True)
    return render_template('contact.html')

def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com", port="587") as connection:
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        connection.sendmail(OWN_EMAIL, OWN_EMAIL, email_message)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')