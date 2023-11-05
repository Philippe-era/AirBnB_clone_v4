#!/usr/bin/python3
"""This will start flask web application """

from flask import Flask
app_flask = Flask(__name__)


@app_flask.route('/', strict_slashes=False)
def index():
    """returns or (answer) Hello HBNB!"""
    return 'Hello HBNB!'


@app_flask.route('/hbnb', strict_slashes=False)
def hbnb():
    """should return  HBNB"""
    return 'HBNB'


@app_flask.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """Display  “C ” followed by the value of the text variable"""
    return 'C ' + text.replace('_', ' ')


@app_flask.route('/python', strict_slashes=False)
@app_flask.route('/python/<text>', strict_slashes=False)
def pythoniscool(text='is cool'):
    """Display “Python ”, followed by the value of the text variable"""
    return 'Python ' + text.replace('_', ' ')

if __name__ == '__main__':
    app_flask.run(host='0.0.0.0', port='5000')
