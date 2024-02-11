#!/usr/bin/python3
""" Defines class State """
from models.base_model import BaseModel


class State(BaseModel):
    """ Representation of state """
    name = ""

    def __init__(self, *args, **kwargs):
        """ Initializes state """
        super().__init__(*args, **kwargs)
