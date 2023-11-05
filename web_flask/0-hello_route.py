#!/usr/bin/python3
""" THIS WILL START MY FLASK WEB APPLICATION """

from flask import Flask
app_flask = Flask(__name__)


@app_flask.route('/', strict_slashes=False)
def index():
    """return or (answer) Hello HBNB!"""
    return 'Hello HBNB!'

if __name__ == '__main__':
    app_flask.run(host='0.0.0.0', port='5000')
