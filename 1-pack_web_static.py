#!/usr/bin/python3
"""A function that genarates a .tgz archive and """
from datetime import datetime
import os
from fabric.api import local


def do_pack():
    """Defining the function do_pack which will archive all the contents
    of the web_static directory"""

    now = datetime.now()
    times = now.strftime("%Y%m%d%H%M%S")  # Add a timestamp to the filename
    name = "versions/web_static_{}.tgz".format(times)

    os.makedirs("versions", exist_ok=True)
    if local("tar -cvzf {} web_static".format(name)).failed:
        return None
    return name
