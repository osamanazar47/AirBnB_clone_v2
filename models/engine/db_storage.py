#!/usr/bin/python3
"""This module defines a class to manage DataBase
 storage for hbnb clone"""
import os
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine, MetaData
from models.base_model import BaseModel, Base
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
                                      .format(os.environ['HBNB_MYSQL_USER'],
                                              os.environ['HBNB_MYSQL_PWD'],
                                              os.environ['HBNB_MYSQL_HOST'],
                                              os.environ['HBNB_MYSQL_DB']),
                                              pool_pre_ping=True)
        if os.environ['HBNB_ENV'] == "test":
            metadata = MetaData()
            metadata.reflect()
            metadata.drop_all()

    def all(self, cls=None):
        """retrive all objects"""
        object_list = dict()
        if cls:
            res = self.__session.query(cls).all()
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
        from models.base_model import BaseModel, Base
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine,
                               expire_on_commit=False)
        ScopedSession = scoped_session(Session)
        self.__session = ScopedSession()
