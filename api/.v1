app.py

#!/usr/bin/python3
'''Flask app to be created with reports and views 
'''

from os import getenv
from flask_cors import CORS
from models import storage
from api.v1.views import app_views
from flask import Flask, jsonify

app_run = Flask(__name__)

# Allows for origin enabled by CORS
CORS(app_run, resources={r'/api/v1/*': {'origins': '0.0.0.0'}})

app_run.register_blueprint(app_views)
app_run.url_map.strict_slashes = False

@app.teardown_appcontext
def teardown_engine(exception):
    '''
    Removes the information after it has been deleted
    '''
    storage.close()

# Error handlers for expected app behavior:
@app.errorhandler(404)
def not_found(error):
    '''
Error message will be returned
    '''
    response = {'error': 'Not found'}
    return jsonify(response), 404

if __name__ == '__main__':
    HOST = getenv('HBNB_API_HOST', '0.0.0.0')
    PORT = int(getenv('HBNB_API_PORT', 5000))
    app_run.run(host=HOST, port=PORT, threaded=True)

