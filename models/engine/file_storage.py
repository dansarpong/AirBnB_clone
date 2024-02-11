#!/usr/bin/python3
""" Defines FileStorage which serializes and deserializes instances """
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


classes = {
    "BaseModel": BaseModel,
    "User": User,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Place": Place,
    "Review": Review
    }


class FileStorage:
    """ Class that serializes and deserializes
    to-and-fro instances and a JSON file """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the __objects dictionary """
        return self.__objects

    def new(self, obj):
        """ Sets obj in __objects """
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """ Serializes __objects to __file_path """
        obj = {}
        for key in self.__objects:
            obj[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(obj, f)

    def reload(self):
        """ Deserializes __file_path to __objects """
        try:
            with open(self.__file_path, "r") as f:
                obj_dict = json.load(f)
            for key, value in obj_dict.items():
                self.__objects[key] = classes[value["__class__"]](**value)
        except Exception:
            pass
