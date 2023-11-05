#!/usr/bin/python3
'''
View to be created for the Reviews you see'''


from flask import abort, jsonify, request
from api.v1.views import app_views
from models import storage
from models.place import Place
from models.review import Review
from models.user import User


# rerouting the information related
@app_views.route('/places/<place_id>/reviews', methods=['GET'],
                 strict_slashes=False)
def get_reviews_by_place(place_id):
    '''
    Displays the Review objects
    '''
    # Place will be received from the information
    place = storage.get(Place, place_id)
    if not place:
                abort(404)

    # Converts the information into a dictionary
    reviews = [review.to_dict() for review in place.reviews]
    return jsonify(reviews)

@app_views.route('/reviews/<review_id>', methods=['GET'],
                 strict_slashes=False)
def get_review(review_id):
    '''
   Displays the objects
    '''
        review = storage.get(Review, review_id)
    if review:
        
        return jsonify(review.to_dict())
    else:
        abort(404)

@app_views.route('/reviews/<review_id>', methods=['DELETE'])
def delete_review(review_id):
    '''
    Removes the review object
    '''
    review = storage.get(Review, review_id)
    if review:
        
        storage.delete(review)
        storage.save()
        return jsonify({}), 200
    else:
        # Return 404 error if the Review object is not found
        abort(404)

@app_views.route('/places/<place_id>/reviews', methods=['POST'],
                 strict_slashes=False)
def create_review(place_id):
    '''
    Creation of a Review object
    '''
    # Given Id Place retrieved
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    if not request.get_json():
        abort(400, 'Not a JSON')

    data = request.get_json()
    if 'user_id' not in data:
        abort(400, 'Missing user_id')
    if 'text' not in data:
        abort(400, 'Missing text')
   user = storage.get(User, data['user_id'])
    if not user:
        
        abort(404)

    
    data['place_id'] = place_id
    review = Review(**data)
        review.save()
    return jsonify(review.to_dict()), 201

@app_views.route('/reviews/<review_id>', methods=['PUT'], strict_slashes=False)
def update_review(review_id):
    '''
Modifies the Review object
    '''
  
    review = storage.get(Review, review_id)
    if review:
        if not request.get_json():
            
            abort(400, 'Not a JSON')
        data = request.get_json()
        ignore_keys = ['id', 'user_id', 'place_id', 'created_at', 'updated_at']
        # Update the attributes of the Review object with the JSON data
        for key, value in data.items():
            if key not in ignore_keys:
                setattr(review, key, value)

        review.save()
      
        return jsonify(review.to_dict()), 200
    else:
        # Return 404 error if the Review object is not found
        abort(404)

@app_views.errorhandler(404)
def not_found(error):
    '''
    404 not found will be displayed
    '''
    response = {'error': 'Not found'}
    return jsonify(response), 404

@app_views.errorhandler(400)
def bad_request(error):
    '''
    Bad message request returned
    '''
   
    response = {'error': 'Bad Request'}
    return jsonify(response), 400


