#!/usr/bin/python3
'''
Starts flask web app
'''
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
from os import getenv
from flask_cors import CORS


app = Flask(__name__)
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.teardown_appcontext
def teardown(self):
    ''' removes the current sqlalchemy session '''
    storage.close()

@app.errorhandler(404)
def error(e):
    ''' Handles 404 errors '''
    return jsonify({'error': 'Not found'}), 404

if __name__ == '__main__':
    host = getenv('TTR_API_HOST') if getenv('TTR_API_HOST') else '0.0.0.0'
    port = getenv('TTR_API_PORT') if getenv('TTR_API_PORT') else 5002
    app.run(host=host, port=port, threaded=True)
