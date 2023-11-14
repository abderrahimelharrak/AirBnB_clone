#!/usr/bin/python3
"""Defining the City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """Representing a city.

    Attributes:
        state_id (str): The state id.
        name (str): The city name.
    """

    state_id = ""
    name = ""
