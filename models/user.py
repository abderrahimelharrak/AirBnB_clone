#!/usr/bin/python3
"""Defining the User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """Representing a User.

    Attributes:
        email (str): The email.
        password (str): The password.
        first_name (str): The first name.
        last_name (str): The last name.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
