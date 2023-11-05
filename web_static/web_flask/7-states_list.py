#!/usr/bin/python3
""" This will start flask web apllication"""

from flask import Flask, render_template
from models import *
from models import storage
app_flask = Flask(__name__)


@app_flask.route('/states_list', strict_slashes=False)
def states_list():
    """displays the information in ascending order alphabetically"""
    list_of_states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template('7-states_list.html', list_of_states=list_of_states)


@app_flask.teardown_appcontext
def teardown_db(exception):
    """ tears down the flask info"""
    storage.close()

if __name__ == '__main__':
    app_flask.run(host='0.0.0.0', port='5000')
