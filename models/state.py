#!/usr/bin/python3
"""Defining the State class."""
from models.base_model import BaseModel


class State(BaseModel):
    """Representing a state.

    Attributes:
        name (str): The name of the state.
    """

    name = ""
