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


@app.route('/states', strict_slashes=False)
def states():
    """ Render list of all the states """
    states = storage.all("State")
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def state_id(id):
    """ Render a state based on the id """
    states = storage.all("State").values()
    for state in states:
        if state.id == id:
            return render_template('9-states.html', state=state)
    return render_template('9-states.html', state=None)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
