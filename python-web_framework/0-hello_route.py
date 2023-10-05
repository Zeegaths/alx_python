"""This script starts a Flask web application.

It creates a Flask web server that listens on 0.0.0.0 (all available network interfaces)
and port 5000. The main route, '/', displays 'Hello HBNB!' when accessed in a web browser.

Routes:
    '/': Displays 'Hello HBNB!' when accessed.

Attributes:
    app (Flask): The Flask application instance.
"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Route to display 'Hello HBNB!'."""
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
