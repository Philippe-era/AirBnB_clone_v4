api/v1/views/places.py

#!/usr/bin/python3
'''
View for places .py
'''

# Import necessary modules
from flask import abort, jsonify, request
# Import the required models
from models.city import City
from models.place import Place
from models import storage
from models.state import State
from models.user import User
from models.amenity import Amenity
from api.v1.views import app_views


# routing fot city place
@app_views.route('/cities/<city_id>/places', methods=['GET'],
                 strict_slashes=False)
def get_places_by_city(city_id):
    '''
    Retrieves all places from the city place
    '''
    city = storage.get(City, city_id)
    if not city:
        # 404 if there is nothing
        abort(404)

    #Converts to dictionaries
    places = [place.to_dict() for place in city.places]
    return jsonify(places)

# routing information from the info 
@app_views.route('/places/<place_id>', methods=['GET'],
                 strict_slashes=False)
def get_place(place_id):
    '''
    Place object in place    '''
    
    place = storage.get(Place, place_id)
    if place:
        return jsonify(place.to_dict())
    else:
        # 404 in check
        abort(404)

@app_views.route('/places/<place_id>', methods=['DELETE'])
def delete_place(place_id):
    '''
    Place object checked
    '''
    place_check = storage.get(Place, place_id)
    if place_check:
        # Place Object deleted 
        storage.delete(place_check)
        storage.save()
        # 200 status code
        return jsonify({}), 200
    else:
        abort(404)

# routing for the information
@app_views.route('/cities/<city_id>/places', methods=['POST'],
                 strict_slashes=False)
def create_place(city_id):
    '''Place object created in place
    '''
    city = storage.get(City, city_id)
    if not city:
     
        abort(404)

        if not request.get_json():
        abort(400, 'Not a JSON')

    data_check = request.get_json()
    if 'user_id' not in data_check:
        
        abort(400, 'Missing user_id')
    if 'name' not in data_check:
        abort(400, 'Missing name')

    user = storage.get(User, data_check['user_id'])
    if not user:
        
        abort(404)

        data_check['city_id'] = city_id
    
    place = Place(**data)
    #Place saved
    place.save()
    # 201 status code
    return jsonify(place.to_dict()), 201

@app_views.route('/places/<place_id>', methods=['PUT'], strict_slashes=False)
def update_place(place_id):
    '''
Place object modified
    '''
    
    place = storage.get(Place, place_id)
    if place:
        if not request.get_json():
            abort(400, 'Not a JSON')

  
        data_check = request.get_json()
        ignore_keys = ['id', 'user_id', 'city_id', 'created_at', 'updated_at']
      
        for key, value in data.items():
            if key not in ignore_keys:
                setattr(place, key, value)

        place.save()
        return jsonify(place.to_dict()), 200
    else:
        abort(404)


@app_views.errorhandler(404)
def not_found(error):
    '''
    Error 404 found will be returned
    '''
    # Return a JSON response for 404 error
    response = {'error': 'Not found'}
    return jsonify(response), 404

@app_views.errorhandler(400)
def bad_request(error):
    '''
    Returns the information
    '''
 
    response = {'error': 'Bad Request'}
    return jsonify(response), 400

# redirection
@app_views.route('/places_search', methods=['POST'], strict_slashes=False)
def places_search():
    """
    Displays the information back
    """
    if request.get_json() is None:
        abort(400, description="Not a JSON")

    data_check = request.get_json()

    if data_check and len(data):
        states = data_check.get('states', None)
        cities = data_check.get('cities', None)
        amenities = data_check.get('amenities', None)
    if not data_check or not len(data_check) or (
            not states and
            not cities and
            not amenities):
        places = storage.all(Place).values()
        placed_lists= []
        for place in places:
            list_places.append(place.to_dict())
        return jsonify(list_places)

    placed_lists= []
    if states:
        states_obj = [storage.get(State, s_id) for s_id in states]
        for state in states_obj:
            if state:
                for city in state.cities:
                    if city:
                        for place in city.places:
                            list_places.append(place)

    
    if cities:
        city_obj = [storage.get(City, c_id) for c_id in cities]
        for city in city_obj:
            if city:
                for place in city.places:
                    if place not in placed_lists:
                        list_places.append(place)

    
    if amenities:
        if not placed_lists:
            placed_lists= storage.all(Place).values()
        amenities_obj = [storage.get(Amenity, a_id) for a_id in amenities]

        placed_lists= [place for place in placed_lists
                       if all([am in place.amenities
                               for am in amenities_obj])]

        places = []
    for p in placed_lists:
        d = p.to_dict()
        d.pop('amenities', None)
        places.append(d)

    return jsonify(places)

