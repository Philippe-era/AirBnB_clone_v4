#!/usr/bin/python3
"""Starts my web appl fask"""

from flask import Flask, render_template
from models import *
from models import storage
app_flask = Flask(__name__)


@app_flask.route('/hbnb_filters', strict_slashes=False)
def filters():
    """shows it all"""
    states = storage.all("State").values()
    amenities = storage.all("Amenity").values()
    return render_template('10-hbnb_filters.html', states=states,
                           amenities=amenities)


@app_flask.teardown_appcontext
def teardown_db(exception):
    """torn down"""
    storage.close()

if __name__ == '__main__':
    app_flask.run(host='0.0.0.0', port='5000')
