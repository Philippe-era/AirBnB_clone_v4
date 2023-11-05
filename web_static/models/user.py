#!/usr/bin/python3
"""The user class is being defined """
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy.orm import relationship
from sqlalchemy import Column
from sqlalchemy import String


class User(BaseModel, Base):
    """Class database of the class and the niherittable information

    Attributes:
        __tablename__ (str):the table name where info will be stored
        email: (sqlalchemy String): the users email from the information
        password (sqlalchemy String): password of the user in check
        first_name (sqlalchemy String): first name of the user
        last_name (sqlalchemy String): last name of the user in place
        places (sqlalchemy relationship): the place relationship
        reviews (sqlalchemy relationship): the user review relationship
    """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = relationship("Place", backref="user", cascade="delete")
    reviews = relationship("Review", backref="user", cascade="delete")
