#!/usr/bin/python3
'''
Starts flask web app
'''
from flask import Flask
from models import storage
from api.v1.views import app_views
from os import getenv


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(self):
    ''' removes the current sqlalchemy session '''
    storage.close()

if __name__ == '__main__':
    host = getenv('TTR_API_HOST') if getenv('TTR_API_HOST') else '0.0.0.0'
    port = getenv('TTR_API_PORT') if getenv('TTR_API_PORT') else 5000
    app.run(host=host, port=port, threaded=True, debug=True) # remove debug mode later
