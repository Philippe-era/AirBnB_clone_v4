#!/usr/bin/python3
'''
API handled in the context of cities
'''

# modules needed for the task will be required
from models.city import City
from api.v1.views import app_views
from models import storage
from flask import abort, jsonify, request
# Import the State and City models
from models.state import State

# routing information necessary
@app_views.route('/states/<state_id>/cities', methods=['GET'],
                 strict_slashes=False)
def get_cities_by_state(state_id):
    '''
    Displays all information from the city object
    '''
    #The information will be returned in this state and fashion
    state = storage.get(State, state_id)
    if not state:
        # 404 if error
        abort(404)

    # all city objects returned
    #   the State and convert them to dictionaries
    cities = [city.to_dict() for city in state.cities]
    return jsonify(cities)

@app_views.route('/cities/<city_id>', methods=['GET'], strict_slashes=False)
def get_city(city_id):
    '''
    Retrieves a City object.
    '''
    # City retrievied
    city = storage.get(City, city_id)
    if city:
        # City object in form of JSON 
        return jsonify(city.to_dict())
    else:
        
        abort(404)

# routing information necessary
@app_views.route('/cities/<city_id>', methods=['DELETE'])
def delete_city(city_id):
    '''
    Erases object completely
    '''
    # Returns city ID
    city = storage.get(City, city_id)
    if city:
        # Deletes the information necessary for infomration
        storage.delete(city)
        storage.save()
        # 200 status code
        return jsonify({}), 200
    else:
                abort(404)

# rerouting information
@app_views.route('/states/<state_id>/cities', methods=['POST'],
                 strict_slashes=False)
def create_city(state_id):
    '''
    City object to be created 
    '''
    #Displays ID necessary
    state = storage.get(State, state_id)
    if not state:
        
        abort(404)

    # Json format enabled
    if not request.get_json():
        abort(400, 'Not a JSON')

    # requested information returned
    data = request.get_json()
    if 'name' not in data:
        
        abort(400, 'Missing name')

    # json key assigned to the party
    data['state_id'] = state_id
    
    city = City(**data)
    # the object will be saved
    city.save()
    # 201 status code returned 
    return jsonify(city.to_dict()), 201

# rerouting information
@app_views.route('/cities/<city_id>', methods=['PUT'], strict_slashes=False)
def update_city(city_id):
    '''
    City object created 
    '''
    city = storage.get(City, city_id)
    if city:
        # JSON DATA CHECK
        if not request.get_json():
            # 400 if not found
            abort(400, 'Not a JSON')

        # Json data information requested
        data = request.get_json()
        ignore_keys = ['id', 'state_id', 'created_at', 'updated_at']
        
        for key, value in data.items():
            if key not in ignore_keys:
                setattr(city, key, value)

        city.save()
        
        return jsonify(city.to_dict()), 200
    else:
        # 404 if not returned 
        abort(404)

# Error Handlers:
@app_views.errorhandler(404)
def not_found(error):
    '''
    404: Not Found.
    '''
    #JSON RESPONSE
    return jsonify({'error': 'Not found'}), 404

@app_views.errorhandler(400)
def bad_request(error):
    '''
    REQUEST MESSAGE FOR THE INFORMATION
    '''
    # Json 400
    return jsonify({'error': 'Bad Request'}), 400


