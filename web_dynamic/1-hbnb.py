#!/usr/bin/python3
""" Flask web application  """
from models import storage
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from os import environ
from flask import Flask, render_template
import uuid
app = Flask(__name__)

@app.teardown_appcontext
def close_db(error):
    """ Sql academy is removed instatnly """
    storage.close()


@app.route('/1-hbnb', strict_slashes=False)
def hbnb():
    """ HBNB is alive! """
    states = storage.all(State).values()
    states = sorted(states, key=lambda k: k.name)
    state_load = []

    for state in states:
        state_load.append([state, sorted(state.cities, key=lambda k: k.name)])

    amenities = storage.all(Amenity).values()
    amenities = sorted(amenities, key=lambda k: k.name)

    places = storage.all(Place).values()
    places = sorted(places, key=lambda k: k.name)

    return render_template('1-hbnb.html',
                           states=state_load,
                           amenities=amenities,
                           places=places, cache_id=uuid.uuid4())


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)

