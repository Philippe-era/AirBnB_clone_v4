#!/usr/bin/python3
"""STARTS FLASK WEB APPLICATION """

from flask import Flask, render_template
from models import *
from models import storage
app_flask = Flask(__name__)


@app_flask.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """ALPHABETICAL ORDER DISPLAY OF CITITES"""
    states = storage.all("State").values()
    return render_template('8-cities_by_states.html', states=states)


@app_flask.teardown_appcontext
def teardown_db(exception):
    """will close the storage wen it teardown"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
