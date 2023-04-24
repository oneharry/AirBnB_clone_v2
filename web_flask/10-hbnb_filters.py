#!/usr/bin/python3
"""
    Starts a flask web application
"""

from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def teardown(err):
    """ Remove the current sqlalchemy session"""
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """ Render list of all the states """
    states = storage.all("State").values()
    amenities = storage.all("Amenity").values()
    return render_template('10-hbnb_filters.html', states=states,
                           amenities=amenities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
