"""Web interface for hello Flask application."""

from typing import Optional

from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/", methods=["GET"])
@app.route("/<string:name>", methods=["GET"])
def hello(name: Optional[str] = None) -> str:
    """Endpoint to say hello to name."""
    if not name:
        name = request.args.get("name") or "world"
    return render_template("hello.html", name=name)


if __name__ == "__main__":
    app.run()
