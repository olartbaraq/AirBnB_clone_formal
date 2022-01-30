#!/usr/bin/python3

"""import several modules for accessibilty"""
import json
from models.base_model import BaseModel

"""Defines a class FileStorage that serializes instances
to a JSON file and deserializes JSON file to instances
"""


class FileStorage():
    """ Declares a class with private class attributes and
    public instance methods
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ method to return the dictionary of the private attribute
        __objects
        """
        return self.__objects

    def new(self, obj):
        """ method to sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """method to serialize __objects to the JSON file (path: __file_path"""
        json_objects = {}
        for key, values in self.__objects.items():
            json_objects[key] = values.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(json_objects, f)

    def reload(self):
        """deserializes the JSON file"""
        try:
            with open(self.__file_path, "r") as f:
                self.__objects = json.load(f)
            for key in prev:
                self.__objects[key] = BaseModel[prev[key]["__class__"]](**prev[key])
        except Exception as e:
            pass
