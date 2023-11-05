#!/usr/bin/python3
'''
User object to be created
'''

from flask import abort, jsonify, request
from models.user import User
from models import storage
from api.v1.views import app_views



@app_views.route('/users', methods=['GET'], strict_slashes=False)
def get_all_users():
    '''
    Erases the object User
    '''
        users = storage.all(User).values()
    return jsonify([user.to_dict() for user in users])

@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def get_user(user_id):
    '''
Displays the Review object
    '''
    
    user = storage.get(User, user_id)
    if user:
        return jsonify(user.to_dict())
    else:
       
        abort(404)
@app_views.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    '''
Erases the User Object    '''
 
    user = storage.get(User, user_id)
    if user:
        
        storage.delete(user)
        storage.save()
        return jsonify({}), 200
    else:
        
        abort(404)
@app_views.route('/users', methods=['POST'], strict_slashes=False)
def create_user():
    '''
User Object to be formed
    '''
        if not request.get_json():
        abort(400, 'Not a JSON')

    data = request.get_json()
    if 'email' not in data:
        abort(400, 'Missing email')
    if 'password' not in data:
        abort(400, 'Missing password')
    user = User(**data)
    
    user.save()
        return jsonify(user.to_dict()), 201

@app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
def update_user(user_id):
    '''
Modification of the user object
    '''
    
    user = storage.get(User, user_id)
    if user:
        
        if not request.get_json():
            
            abort(400, 'Not a JSON')

        data = request.get_json()
        ignore_keys = ['id', 'email', 'created_at', 'updated_at']
        for key, value in data.items():
            if key not in ignore_keys:
                setattr(user, key, value)

        user.save()
        return jsonify(user.to_dict()), 200
    else:
        abort(404)

@app_views.errorhandler(404)
def not_found(error):
    '''
 404 not found will be returned
    '''
    response = {'error': 'Not found'}
    return jsonify(response), 404

@app_views.errorhandler(400)
def bad_request(error):
    '''
    Bad request returned 
    '''
 
    response = {'error': 'Bad Request'}
    return jsonify(response), 400



