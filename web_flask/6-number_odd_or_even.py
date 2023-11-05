#!/usr/bin/python3
""" This will start flask web application"""

from flask import Flask, render_template
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

@app_flask.route('/number_template/<int:n>', strict_slashes=False)
def numbersandtemplates(n):
    """if n is an integer an html page will be displayed"""
    return render_template('5-number.html', n=n)

@app_flask.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def numbersandevenness(n):
    """if n is an integer display html page missing"""
    if n % 2 == 0:
        even_number = 'even'
    else:
        even_number = 'odd'
    return render_template('6-number_odd_or_even.html', n=n,
                           even_number=even_number)


if __name__ == '__main__':
    app_flask.run(host='0.0.0.0', port='5000')
