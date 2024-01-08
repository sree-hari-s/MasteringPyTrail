from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper_function1():
        return f"<b>{function()}</b>"
    return wrapper_function1


def make_italics(function):
    def wrapper_function2():
        return f"<i>{function()}</i>"
    return wrapper_function2


def make_emphasis(function):
    def wrapper_function3():
        return f"<em>{function()}</em>"

    return wrapper_function3


def make_underline(function):
    def wrapper_function4():
        return f"<u>{function()}</u>"
    return wrapper_function4


@app.route("/")
@make_italics
def hello_world():
    return "Hello, world!"

@app.route("/bye")
@make_bold
def bye():
    return "bye!"


if __name__ == "__main__":
    app.run(debug=True)
