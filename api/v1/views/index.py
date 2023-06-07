#!/usr/bin/python3
'''
Returns the status of the app
'''
from api.v1.views import app_views
from flask import jsonify
app_views.url_defaults = {'strict_slashes': False}


@app_views.route('/status')
def status():
    ''' Returns status of API '''
    return jsonify({'status': 'OK'})
