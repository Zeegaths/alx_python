"""This script starts a Flask web application.

It creates a Flask web server that listens on 0.0.0.0 (all available network interfaces)
and port 5000. The main route, '/', displays 'Hello HBNB!' when accessed in a web browser.

Routes:
    '/': Displays 'Hello HBNB!' when accessed.

Attributes:
    app (Flask): The Flask application instance.
"""
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/number_template/<int:n>', strict_slashes=False)
def render_template_with_number(n):
    if isinstance(n, int):
        return render_template('5-number_template.html', n=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Route to display 'Hello HBNB!'."""
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Route to display 'HBNB'."""
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """Route to display 'C ' followed by the value of the text variable (replace underscore _ symbols with a space)."""
    return 'C {}'.format(text.replace('_', ' '))

@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def python_route(text='is_cool'):
    """Route to display 'Python ' followed by the value of the text variable (replace underscore _ symbols with a space). Default text is 'is_cool'."""
    return 'Python {}'.format(text.replace('_', ' '))

@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """Route to display '{} is a number' only if n is an integer."""
    return '{} is a number'.format(n)

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template_route(n):
    """Route to display an HTML page with 'Number: n' in an H1 tag inside the BODY tag. Displays only if n is an integer."""
    return render_template('5-number_template.html', n=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
