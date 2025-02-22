#!/usr/bin/python3
"""Contains the City class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel):
    """This is the City class
    Attributes:
        state_id: The state id
        name: input name
    """
   __tablename__ = 'cities'
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    name = Column(String(128), nullable=False)
    # One2many relationship to places
    places = relationship("Place", backref="cities",
                          cascade="all, delete, delete-orphan")
