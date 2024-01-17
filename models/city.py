#!/usr/bin/python3
"""'city' Module"""
from models.base_model import BaseModel


class City(BaseModel):
    """Class to manage city objects"""
    state_id = ""
    name = ""
