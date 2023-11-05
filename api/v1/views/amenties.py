#!/usr/bin/python3
'''
An amenity view for amenties 
'''

# Modules needed for this to be successful
from models.amenity import Amenity
from api.v1.views import app_views
from models import storage
from flask import abort, jsonify, request

# changes the route of the information sent 
@app_views.route('/amenities', methods=['GET'], strict_slashes=False)
def get_all_amenities():
    '''Displays all the information necessary'''
        amenities = storage.all(Amenity).values()
    # Dictionaries will be formed from the objects
    return jsonify([amenity.to_dict() for amenity in amenities])

# rerouting the information 
@app_views.route('/amenities/<amenity_id>',
                 methods=['GET'], strict_slashes=False)
def get_amenity(amenity_id):
    '''Amenity object will be retrieved'''
    #The ID WILL BE RETRIEVED
    amenity = storage.get(Amenity, amenity_id)
    if amenity:
     
        return jsonify(amenity.to_dict())
    else:
        #the 404 will be displayed as a form of not in
        abort(404)

# rerouting the necessary information
@app_views.route('/amenities/<amenity_id>', methods=['DELETE'])
def delete_amenity(amenity_id):
    '''The amenity class will be deleted'''
    
    amenity = storage.get(Amenity, amenity_id)
    if amenity:
        #Deletes everything
        storage.delete(amenity)
        storage.save()
        # status 200 code will be returned 
        return jsonify({}), 200
    else:
        # 404 will be returned 
        abort(404)

# Route for creating a new Amenity object
@app_views.route('/amenities', methods=['POST'], strict_slashes=False)
def create_amenity():
    '''Amenity Object created '''
    if not request.get_json():
        abort(400, 'Not a JSON')

    # Json data will be returned
    data_check = request.get_json()
    if 'name' not in data_check:
        # error 404 to be returned
        abort(400, 'Missing name')

    # Creates JSON DATA FILE
    amenity = Amenity(**data)
    # amenity saved
    amenity.save()
    
    #   object in 201 format
    return jsonify(amenity.to_dict()), 201

# routing information
@app_views.route('/amenities/<amenity_id>', methods=['PUT'],
                 strict_slashes=False)
def update_amenity(amenity_id):
    '''Amenity objected modified'''
        amenity = storage.get(Amenity, amenity_id)
    if amenity:
        # 404 found in the mix up
        if not request.get_json():
            abort(400, 'Not a JSON')

        # Data from the request
        data = request.get_json()
        ignore_keys = ['id', 'created_at', 'updated_at']
        # Amenity in the office
        for key, value in data.items():
            if key not in ignore_keys:
                setattr(amenity, key, value)

        # Updated storage is saved
        amenity.save()
        # status 200 code
        return jsonify(amenity.to_dict()), 200
    else:
        # Return 404 error if the Amenity object is not found
        abort(404)

# Error handling the information 
@app_views.errorhandler(404)
def not_found(error):
    '''Returns 404: Not Found'''
    
    response = {'error': 'Not found'}
    return jsonify(response), 404

@app_views.errorhandler(400)
def bad_request(error):
    '''Illegal information'''
    # 400 found 
    response = {'error': 'Bad Request'}
    return jsonify(response), 400



