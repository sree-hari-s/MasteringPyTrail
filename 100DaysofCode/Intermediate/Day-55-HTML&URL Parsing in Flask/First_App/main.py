from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, world!"

@app.route('/bye')
def bye():
    return "bye!"

@app.route('/username/<name>/<int:num>') # by default it takes as string
def greet(name,num):
    return f"Hello {name}!,I am {num} years old"

if __name__ == '__main__':
    app.run(debug=True)