#!/usr/bin/python3
"""
A script for starting web application
- the web app is listening o 0.0.0.0, port 5000
- fetches data from the storage engine
- removes the current SQLAlchemy session after each request
- routes to /states_list to display a list of all states objects present
in DBStorage sorted by name
"""
from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states_list():
    """
    Displays an HTML page with a list of all State objects in DBStorage.
    """
    states = storage.all("State")
    return render_template("9-states.html", state=states)


@app.route('/states/<id>', strict_slashes=False)
def state__id_list(id):
    """
    Displays an HTML page with a list of all cities in
    a specific state objects in DBStorage.
    """
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


@app.teardown_appcontext
def tear(exc):
    """A method to remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
