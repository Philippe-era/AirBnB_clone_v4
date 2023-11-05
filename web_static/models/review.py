#!/usr/bin/python3
"""review class prototype"""
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import relationship


class Review(BaseModel, Base):
    """database for the review section

    Attributes:
        __tablename__ (str): table that will store reviews
        text (sqlalchemy String): review information by reviewer
        place_id (sqlalchemy String): the review where he stays
        user_id (sqlalchemy String): the review identity key
    """
    __tablename__ = "reviews"
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
