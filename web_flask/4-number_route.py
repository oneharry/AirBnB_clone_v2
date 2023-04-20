#!/usr/bin/python3
"""
    Starts a flask web application
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Function attached to root of url, return Hello HBNB!"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ FUnction returns text hbnb"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def C(text):
    """ Returns value of text variable"""
    return "C %s" % text.replace('_', ' ')


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """ Returns text when associated route is visited"""
    return "Python %s" % text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ Returns a text only if n variable is an int"""
    return "%s is a number" % n


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
