#!/usr/bin/python3
"""Defining the BaseModel class."""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Representing the BaseModel of the HBnB project."""

    def __init__(self, *args, **kwargs):
        """Initializing a new BaseModel.

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        t_form = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for x, y in kwargs.items():
                if x == "created_at" or x == "updated_at":
                    self.__dict__[x] = datetime.strptime(y, t_form)
                else:
                    self.__dict__[x] = y
        else:
            models.storage.new(self)

    def save(self):
        """Updating updated_at with the current datetime."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Returning the dictionary of the BaseModel instance.

        Includeing the key value pair __class__ representing
        class name of the object.
        """
        r_dict = self.__dict__.copy()
        r_dict["created_at"] = self.created_at.isoformat()
        r_dict["updated_at"] = self.updated_at.isoformat()
        r_dict["__class__"] = self.__class__.__name__
        return r_dict

    def __str__(self):
        """Returnng the print or str representation of the BaseModel instance."""
        cl_name = self.__class__.__name__
        return "[{}] ({}) {}".format(cl_name, self.id, self.__dict__)
