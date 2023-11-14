#!/usr/bin/python3
"""Definnges the FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Representng an abstracted storage engine.

    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returning the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Seting in __objects obj with key <obj_class_name>.id"""
        oc_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(oc_name, obj.id)] = obj

    def save(self):
        """Serializzing __objects to the JSON file __file_path."""
        odi_ct = FileStorage.__objects
        obj_dict = {obje: odi_ct[obje].to_dict() for obje in odi_ct.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializing the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as f:
                obj_dict = json.load(f)
                for x in obj_dict.values():
                    cls__name = x["__class__"]
                    del x["__class__"]
                    self.new(eval(cls__name)(**x))
        except FileNotFoundError:
            return
