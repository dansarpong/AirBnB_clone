#!/usr/bin/python3
""" Defines class Amenity"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Representation of Amenity """
    name = ""

    def __init__(self, *args, **kwargs):
        """ Initializes amenity """
        super().__init__(*args, **kwargs)
