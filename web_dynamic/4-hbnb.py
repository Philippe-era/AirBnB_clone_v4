#!/usr/bin/python3
""" FLASK WEB APPLICATION STARTED """
from models import storage
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from os import environ
from flask import Flask, render_template
import uuid
app = Flask(__name__)

@app.teardown_appcontext
def close_db(error):
    """ Destroys the sql acadey session """
    storage.close()

#routes location
@app.route('/4-hbnb', strict_slashes=False)
def hbnb():
    """ HBNB is livingg! """
    states = storage.all(State).values()
    states = sorted(states, key=lambda k: k.name)
    state_load = []
#iterates through states
    for state in states:
        state_load.append([state, sorted(state.cities, key=lambda k: k.name)])
#amenties in line 
    amenities = storage.all(Amenity).values()
    amenities = sorted(amenities, key=lambda k: k.name)
#places in the line to be iterates 
    places = storage.all(Place).values()
    places = sorted(places, key=lambda k: k.name)

    return render_template('4-hbnb.html',
                           states=state_load,
                           amenities=amenities,
                           places=places, cache_id=uuid.uuid4())


if __name__ == "__main__":
    """ Executable Function """
    app.run(host='0.0.0.0', port=5000)

