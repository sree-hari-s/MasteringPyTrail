"""Web interface for hello_form Flask application."""

from typing import Optional

from flask import Flask, redirect, render_template, request, url_for


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def form() -> str:
    """Endpoint to handle HTML form."""
    if request.method == "POST":
        name = request.form.get("name")
        return redirect(url_for("hello", name=name))
    return render_template("form.html")


@app.route("/hello/", methods=["GET"])
@app.route("/hello/<string:name>", methods=["GET"])
def hello(name: Optional[str] = None) -> str:
    """Endpoint to say hello to name."""
    if not name:
        return redirect(url_for("form"))
    return render_template("hello.html", name=name)


if __name__ == "__main__":
    app.run()
