# Import Flask to create the web application and jsonify to return JSON responses
from flask import Flask, jsonify 
# Import CORS to enable cross-origin requests (from different domains)
from flask_cors import CORS
# Import os and socket for potential use in the application (e.g., environment variables, networking)
import os
import socket

# Create a Flask application instance
app = Flask(__name__)
# Enable CORS to allow requests from any origin
CORS(app)

# Define a route for the root endpoint ("/")
@app.route('/')
def hello():
    # Return a JSON response with a greeting message
    return jsonify(message="Ciao da k8s!")

@app.route('/hostname')
def get_hostname():
    msg = os.getenv('MESSAGE', 'hello from k8s')
    hostname= socket.gethostname()
    # Get the hostname of the machine running the application
    # Return a JSON response with the hostname and message
    return jsonify(hostname=hostname, message=msg)


# Check if the script is being run directly (not imported as a module)
if __name__ == '__main__':
    # Start the Flask server:
    # - host='0.0.0.0': accept connections from any IP address
    # - port=5000: use port 5000
    # - debug=True: enable debug mode for development
    app.run(host='0.0.0.0', port=5000, debug=True)

