#!/usr/bin/python3
""" This will start my web application properly"""

from flask import Flask
app_flask = Flask(__name__)


@app_flask.route('/', strict_slashes=False)
def index():
    """This will return nothing or (answer) Hello HBNB!"""
    return 'Hello HBNB!'


@app_flask.route('/hbnb', strict_slashes=False)
def hbnb():
    """ This should only return HBNB"""
    return 'HBNB'


@app_flask.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """will show “C ” followed by the value of the given  text variable"""
    return 'C ' + text.replace('_', ' ')

if __name__ == '__main__':
    app_flask.run(host='0.0.0.0', port='5000')
