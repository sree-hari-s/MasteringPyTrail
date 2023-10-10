# Flask Projects

`hello` is a sample "Hello, world" Flask application.

It will display "Hello, \[name\]!", where `name` is passed in the URL, either as a URL or query parameter, e.g. `localhost:5000/bob` or `localhost:5000?name=bob`.
If no name is supplied, it is set to `"world"`.

The `hello.html` template is formatted using [Jinja2](https://pypi.org/project/Jinja2/), and is found in the `templates` directory.

By default, Flask listens on `127.0.0.1:5000`.
