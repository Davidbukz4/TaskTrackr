#!/usr/bin/python3
""" Starts The TaskTrackr Web Application """
from models import storage
from models.user import User
from models.task import Task
from os import environ
from flask import Flask, render_template
app = Flask(__name__)
import uuid


@app.route('/', strict_slashes=False)
def hbnb():
    """ TaskTrackr homepage """
    states = storage.all(State).values()

    return render_template('0-hbnb.html',
                           states=st_ct,
                           amenities=amenities,
                           places=places,
                           cache_id=uuid.uuid4())


@app.teardown_appcontext
def close(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()

if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000, threaded=True, debug=True)
