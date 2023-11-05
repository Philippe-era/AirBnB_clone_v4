#!/usr/bin/python3
""" This will start my flask web application """

from flask import Flask
app_flask = Flask(__name__)


@app_flask.route('/', strict_slashes=False)
def index():
    """This will return or (answer) Hello HBNB!"""
    return 'Hello HBNB!'


@app_flask.route('/hbnb', strict_slashes=False)
def hbnb():
    """This  will return  HBNB"""
    return 'HBNB'

if __name__ == '__main__':
    app_flask.run(host='0.0.0.0', port='5000')
