#!/usr/bin/python3
"""This module defines a class to manage DataBase
 storage for hbnb clone"""
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import (create_engine)
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """DataBase Storage"""
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'\
                                      .format(getenv("HBNB_MYSQL_USER"),
                                              getenv("HBNB_MYSQL_PWD"),
                                              getenv("HBNB_MYSQL_HOST"),
                                              getenv("HBNB_MYSQL_DB")),
                                              pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """retrive all objects"""
        object_list = dict()
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            res = self.__session.query(cls)
            for row in res:
                key = "{}.{}".format(type(row).__name__, row.id)
                object_list[key] = row
            return object_list
        else:
            class_list = [State, City, User, Place, Review, Amenity]
            for class_name in class_list:
                res = self.__session.query(class_name)
                for row in res:
                    key = "{}.{}".format(type(row).__name__, row.id)
                    object_list[key] = row
            return object_list

    def new(self, obj):
        """Adda an object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit change"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes the obj from the current session"""
        if obj:
            self._session.delete(obj)

    def reload(self):
        """reload all tables"""
        Base.metadata.create_all(self.__engine)
        Sess = sessionmaker(bind=self.__engine,
                               expire_on_commit=False)
        Session = scoped_session(Sess)
        self.__session = Session()

    def close(self):
        """Closes the session"""
        self.__session.close()
