api/v1/views/index.py

#!/usr/bin/python3
'''
Route created for the information
'''

from flask import jsonify
from models import storage
from api.v1.views import app_views

@app_views.route('/status', methods=['GET'])
def api_status():
    '''
    API HEALTH
    '''
    response = {'status': 'OK'}
    return jsonify(response)

@app_views.route('/stats', methods=['GET'])
def get_stats():
    '''
    Displays the information needed
    '''
    stats = {
        'amenities': storage.count('Amenity'),
        'cities': storage.count('City'),
        'places': storage.count('Place'),
        'reviews': storage.count('Review'),
        'states': storage.count('State'),
        'users': storage.count('User')
    }
    return jsonify(stats)

