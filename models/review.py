#!/user/bin/python3
"""The Reviews Module"""
from models.base_model import BaseModel


lass Review(BaseModel):
    """Class to manage reviews"""
    place_id = ""
    user_id = ""
    text = ""
