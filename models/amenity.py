#!/usr/bin/python3
"""Amenties place blueprint"""
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """Amenities of the place in check and place going forward

    Attributes:
        __tablename__ (str): The table containing the information
        name (sqlalchemy String): The facility place
        place_amenities (sqlalchemy relationship): one-many relationship
    """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary="place_amenity",
                                   viewonly=False)
