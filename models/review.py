#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey

class Review(BaseModel):
    """ Review classto store review information """
    place_id = Column(String(60),ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60),ForeignKey("user.id"), nullable=False)
    text = Column(String(1024), nullable=False)


    place_id = ""
    user_id = ""
    text = ""
