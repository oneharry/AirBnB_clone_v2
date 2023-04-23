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


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ Render list of all the states """
    states = storage.all("State")
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
