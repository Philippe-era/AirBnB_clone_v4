#!/usr/bin/python3
""" FLASK WEB APPLICATION STARTS"""
from models import storage
from flask import Flask, render_template
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from os import environ

app = Flask(__name__)

@app.teardown_appcontext
def close_db(error):
    """ Current SQL academy session removed """
    storage.close()

#location of what we will be analysing
@app.route('/0-hbnb/', strict_slashes=False)
def hbnb():
    """ HBNB is living! """
    states = storage.all(State).values()
    states = sorted(states, key=lambda k: k.name)
    states_load = []
#for loop to iterate thru all states
    for state in states:
        states_load.append([state, sorted(state.cities, key=lambda k: k.name)])

    amenities = storage.all(Amenity).values()
    amenities = sorted(amenities, key=lambda k: k.name)
#places in action and consideration 
    places = storage.all(Place).values()
    places = sorted(places, key=lambda k: k.name)

    return render_template('100-hbnb.html',
                           states=states_load,
                           amenities=amenities,
                           places=places, cache_id=uuid.uuid4())


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)

