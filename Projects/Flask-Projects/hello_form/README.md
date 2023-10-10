# Flask Projects

`hello_form` is a sample "Hello, world" Flask application, demonstrating forms with POST.

It will display "Hello, \[name\]!", where `name` is passed as a URL parameter, i.e. `localhost:5000/name/bob`.

Templates are formatted using [Jinja2](https://pypi.org/project/Jinja2/), and are found in the `templates` directory.

`form.html` has a simple HTML form where the user can POST their name.
When submitted, the user is redirected to the URL for `hello.html` with the name passed as a URL parameter.

By default, Flask listens on `127.0.0.1:5000`.
