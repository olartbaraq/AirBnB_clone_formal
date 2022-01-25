#!/usr/bin/python3
""" imports python modules"""
import json
import uuid
import time
from datetime import datetime

"""Defines a class BaseModel that defines all
   common attributes/method for other classes
"""


class BaseModel():
    """Declared a class with attributes and methods"""
    def __init__(self, *args, **kwargs):
        """instantiation of class BaseModel"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

        if kwargs is not None:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                setattr(self, key, value)
        # setattr() function sets the value of the attribute of an object

    def __str__(self):
        """prints the class attributes as a string"""
        return("[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__))

    def save(self):
        """updates the attribute updated_at with current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all
        keys-values pair of __dict__ of the instance
        """
        dico = {}
        # empty dictionary declared.
        dico.update(self.__dict__)
        # .update() command updates the dictionary with the elements
        # from another dictionary object or from an
        # iterable of key/value pairs.
        dico["__class__"] = self.__class__.__name__
        dico["created_at"] = self.created_at.isoformat()
        dico["updated_at"] = self.updated_at.isoformat()
        dico["id"] = self.id
        # above are keys and the corresponding values added to the dictionary.
        return dico
