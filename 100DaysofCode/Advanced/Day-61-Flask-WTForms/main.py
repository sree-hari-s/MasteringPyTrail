import os
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField 


class LoginForm(FlaskForm):
    email = StringField('Email')
    password = PasswordField ('Password')
    submit = SubmitField("Login")
    
app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login",methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    return render_template('login.html', form=login_form)

if __name__ == '__main__':
    app.run(debug=True)
