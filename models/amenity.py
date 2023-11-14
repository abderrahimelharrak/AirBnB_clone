#!/usr/bin/python3
"""Defining the Amenity class."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Representing an amenity.

    Attributes:
        name (str): The amenity name.
    """

    name = ""
