from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, world!"

"""
Without the code below 
we would have to set FLASK_APP=filename without extension
and then run the command flask run
"""
if __name__ == '__main__':
    app.run(debug=True)

"""
With this code we can run it normally like 
python hello.py
"""