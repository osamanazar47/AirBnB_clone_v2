#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from models.city import City
import models
import shlex


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all,delete, delete-orphan',
                          backref="state")

    @property
    def cities(self):
        var = models.storage.all()
        city_list = []
        result = []
        for k in var:
            c = k.replace('.', ' ')
            c = shlex.split(c)
            if (c[0] == "City"):
                city_list.append(var[k])
        for element in city_list:
            if (element.state_id == self.id):
                result.append(element)
        return result
