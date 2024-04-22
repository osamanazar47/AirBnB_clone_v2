#!/usr/bin/python3
"""
A script for starting web application
- the web app is listening o 0.0.0.0, port 5000
- fetches data from the storage engine
- removes the current SQLAlchemy session after each request
- routes to /states_list to display a list of all states objects and cities in those states present
in DBStorage sorted by name
"""
from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_in_states_list():
    """
    Displays an HTML page with a list of all State objects and
    cities in thise states in DBStorage.
    """
    states = storage.all("State")
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def tear(exc):
    """A method to remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
