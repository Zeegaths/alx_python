"""This script starts a Flask web application.

It creates a Flask web server that listens on 0.0.0.0 (all available network interfaces)
and port 5000. The main route, '/', displays 'Hello HBNB!' when accessed in a web browser.

Routes:
    '/': Displays 'Hello HBNB!' when accessed.

Attributes:
    app (Flask): The Flask application instance.
"""
from flask import Flask, render_template

# Create a Flask web application instance
app = Flask(__name__)

# Define a route for the main page '/'
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Route to display 'Hello HBNB!'."""
    return 'Hello HBNB!'

# Define a route for '/hbnb'
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Route to display 'HBNB'."""
    return 'HBNB'

# Define a route for '/c/<text>'
@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """Route to display 'C ' followed by the value of the text variable (replace underscore _ symbols with a space)."""
    return 'C {}'.format(text.replace('_', ' '))

# Define routes for '/python' and '/python/<text>'
@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def python_route(text='is_cool'):
    """Route to display 'Python ' followed by the value of the text variable (replace underscore _ symbols with a space). Default text is 'is_cool'."""
    return 'Python {}'.format(text.replace('_', ' '))

# Define a route for '/number/<int:n>'
@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """Route to display 'n is a number' only if n is an integer."""
    return '{} is a number'.format(n)

# Define a route for '/number_template/<n>' with strict_slashes=False
@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    if isinstance(n, int):
        return render_template('5-number.html', n=n)
    else:
        return "", 404

# Define a route for '/number_odd_or_even/<n>' with strict_slashes=False
@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    if isinstance(n, int):
        result = "even" if n % 2 == 0 else "odd"
        return render_template('6-number_odd_or_even.html', n=n, result=result)
    else:
        return "", 404

if __name__ == '__main__':
    # Run the Flask app on 0.0.0.0 and port 5000
    app.run(host='0.0.0.0', port=5000)
