#!/usr/bin/python3
"""Starts a Flask web application
- the application listens on 0.0.0.0 port 5000
Functtions:
hello: displays Hello HBNB
hbnb: displays HBNB
"""
from flask import Flask, render_template

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


@app.route('/number/<int:n>', strict_slashes=False)
def is_integer(n):
    """Displays n is a number only if n is integer"""
    return "{} is a number".format(n)


@app.route('/number_template', strict_slashes=False)
@app.route('/number_template/<int:n>', strict_slashes=False)
def number_temp(n):
    """Displays (Number: n) only if n is integer using templates"""
    return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even', strict_slashes=False)
@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """Displays (Number: n is even|odd) only if n is integer using templates"""
    return render_template("6-number_odd_or_even.html", n=n)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
