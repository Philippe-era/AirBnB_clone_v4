#!/usr/bin/python3
""" FLASK WEB APPLICATION STARTS """
from models import storage
from os import environ
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from flask import Flask, render_template
import uuid
app = Flask(__name__)



@app.teardown_appcontext
def close_db(error):
    """ DESTORYS SQL ACADEMY SESSION"""
    storage.close()


@app.route('/3-hbnb', strict_slashes=False)
def hbnb():
    """ HBNB is living! """
    states = storage.all(State).values()
    states = sorted(states, key=lambda k: k.name)
    state_load = []
#iterates through the states 
    for state in states:
       state_load.append([state, sorted(state.cities, key=lambda k: k.name)])
#amenties
    amenities = storage.all(Amenity).values()
    amenities = sorted(amenities, key=lambda k: k.name)
#places from the storage object
    places = storage.all(Place).values()
    places = sorted(places, key=lambda k: k.name)

    return render_template('3-hbnb.html',
                           states=state_load,
                           amenities=amenities,
                           places=places, cache_id=uuid.uuid4())


if __name__ == "__main__":
    """ The executable function """
    app.run(host='0.0.0.0', port=5000)

