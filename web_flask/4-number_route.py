#!/usr/bin/python3
"""Starts a Flask web application
- the application listens on 0.0.0.0 port 5000
Functtions:
hello: displays Hello HBNB
hbnb: displays HBNB
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """a function that displays Hello HBNB"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Displays C followed by the value of the text variable"""
    return "C {}".format(text.replace('_', ' '))


@app.route("/python", strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    """Displays Python followed by the value of the text variable"""
    return "Python {}".format(text.replace('_', ' '))


@app.route("/number", strict_slashes=False)
@app.route('/number/<n>', strict_slashes=False)
def number(n):
    """Displays n is a number only if n is integer"""
    if (isinstance(n, int)):
        return "{} is a number".format(n)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
