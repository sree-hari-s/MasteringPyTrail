import os
import smtplib
from datetime import date
from flask import Flask, abort, render_template, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from flask_gravatar import Gravatar
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import ForeignKey
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from flask import abort
# Import your forms from the forms.py
from forms import CreatePostForm,RegisterForm,LoginForm,CommentForm
from dotenv import load_dotenv

load_dotenv()

OWN_EMAIL=os.environ['EMAIL']
OWN_PASSWORD=os.environ['PASSWORD']

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap5(app)

# Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)

# For adding profile images to the comment section
gravatar = Gravatar(app,
                    size=100,
                    rating='g',
                    default='retro',
                    force_default=False,
                    force_lower=False,
                    use_ssl=False,
                    base_url=None)

# CREATE DATABASE
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CONFIGURE TABLES
class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    img_url = db.Column(db.String(250), nullable=False)
    author = db.relationship("User", back_populates="blogposts")
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    comments = db.relationship("Comment", back_populates="blogpost")

class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text, nullable=False)
    author = db.relationship("User", back_populates="comments")
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    blogpost = db.relationship("BlogPost", back_populates="comments")
    blogpost_id = db.Column(db.Integer, db.ForeignKey('blog_posts.id'))

# TODO: Create a User table for all your registered users. 
class User(db.Model, UserMixin):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1000))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    blogposts = db.relationship("BlogPost", back_populates="author")
    comments = db.relationship("Comment", back_populates="author")
    
with app.app_context():
    db.create_all()

# admin-only decorator
def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or current_user.id != 1 :
            return abort(403)
        return f(*args, **kwargs)
    return decorated_function

# creating a new user.
@app.route('/register',methods=['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        # Check if user email is already present in the database.
        result = db.session.execute(db.select(User).where(User.email == form.email.data))
        user = result.scalar()
        if user:
            # User already exists
            flash("You've already signed up with that email, log in instead!")
            return redirect(url_for('login'))
        hash_password = generate_password_hash(
            form.password.data,
            method='pbkdf2:sha256',
            salt_length=8
        )   
        new_user = User(
            name=form.name.data,
            email = form.email.data,
            password=hash_password
        )
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)  #This line will authenticate the user with Flask-Login
        return redirect(url_for('get_all_posts'))
    return render_template("register.html",form=form)


# Retrieve a user from the database based on their email. 
@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        result = db.session.execute(db.select(User).where(User.email == email))
        user = result.scalar()
        if not user:
            flash("Email does not exist")
            return redirect(url_for('login'))
        elif not check_password_hash(user.password,password):
            flash("Password Incorrect")
            return redirect(url_for('login'))
        else:
            login_user(user)
            return redirect(url_for('get_all_posts'))
    return render_template("login.html",form = form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('get_all_posts'))


@app.route('/')
def get_all_posts():
    try:
        result = db.session.execute(db.select(BlogPost))
        posts = result.scalars().all()
    except Exception as e:
        print(f"Error fetching posts: {str(e)}")
        posts = None
    return render_template("index.html", all_posts=posts)


# Allow logged-in users to comment on posts
@app.route("/post/<int:post_id>", methods=["GET", "POST"])
def show_post(post_id):
    requested_post = db.get_or_404(BlogPost, post_id)
    form = CommentForm()
    if form.validate_on_submit():
        if current_user.is_authenticated: # type: ignore
            new_comment = Comment(
                body = form.comment.data,
                author = current_user,
                blogpost = requested_post
            )
            db.session.add(new_comment)
            db.session.commit()
            return redirect(url_for('show_post', post_id=post_id)), 201
        else:
            error = "Login required, Please log in."
            flash(error)
            return redirect(url_for('login')), 401
    return render_template("post.html", post=requested_post,current_user=current_user, form=form)


# decorator so only an admin user can create a new post
@app.route("/new-post", methods=["GET", "POST"])
@admin_only
def add_new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            author=current_user,
            date=date.today().strftime("%B %d, %Y")
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form)


# decorator so only an admin user can edit a post
@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
@admin_only
def edit_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.author = current_user
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))
    return render_template("make-post.html", form=edit_form, is_edit=True)


# decorator so only an admin user can delete a post
@app.route("/delete/<int:post_id>")
@admin_only
def delete_post(post_id):
    post_to_delete = db.get_or_404(BlogPost, post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


@app.route("/about")
def about():
    return render_template("about.html")


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


if __name__ == "__main__":
    app.run(debug=True, port=5002)
