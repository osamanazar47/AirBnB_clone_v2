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

if __name__ == "__main__":
    app.run(host='0.0.0.0')
