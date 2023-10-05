# Import the Flask module
from flask import Flask

# Create a Flask web application instance
app = Flask(__name__)

# Define a route for the root URL '/' and disable strict slashes
@app.route('/', strict_slashes=False)
def hello_hbnb():
    # Return the string 'Hello HBNB!' as the response
    return 'Hello HBNB!'

# Run the application if the script is executed
if __name__ == '__main__':
    # Start the Flask application on host '0.0.0.0' and port 5000
    app.run(host='0.0.0.0', port=5000)
