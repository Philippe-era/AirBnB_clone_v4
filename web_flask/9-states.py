#!/usr/bin/python3
"""STARTS WEB APPLICATION"""

from flask import Flask, render_template
from models import *
from models import storage
app_flask = Flask(__name__)


@app_flask.route('/states', strict_slashes=False)
@app_flask.route('/states/<state_id>', strict_slashes=False)
def states(state_id=None):
    """alphabetical order display"""
    states = storage.all("State")
    if state_id is not None:
        state_id = 'State.' + state_id
    return render_template('9-states.html', states=states, state_id=state_id)


@app_flask.teardown_appcontext
def teardown_db(exception):
    """Torm down"""
    storage.close()

if __name__ == '__main__':
    app_flask.run(host='0.0.0.0', port='5000')
