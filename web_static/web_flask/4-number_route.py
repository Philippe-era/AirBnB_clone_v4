#!/usr/bin/python3
"""
This will start a web flask application
"""

from flask import Flask
app_flask = Flask(__name__)


@app_flask.route('/', strict_slashes=False)
def index():
    """return or (answer) Hello HBNB!"""
    return 'Hello HBNB!'


@app_flask.route('/hbnb', strict_slashes=False)
def hbnb():
    """returns HBNB"""
    return 'HBNB'


@app_flask.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """will display the necessary info"""
    return 'C ' + text.replace('_', ' ')


@app_flask.route('/python', strict_slashes=False)
@app_flask.route('/python/<text>', strict_slashes=False)
def pythoniscool(text='is cool'):
    """displays the relevant text after python"""
    return 'Python ' + text.replace('_', ' ')


@app_flask.route('/number/<int:n>', strict_slashes=False)
def imanumber(n):
    """Displays an integer if an integer is present"""
    return "{:d} is a number".format(n)

if __name__ == '__main__':
    app_flask.run(host='0.0.0.0', port='5000')
