#!/usr/bin/python3
"""The user class is being defined """
from models import storage
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy.orm import relationship
from sqlalchemy import Column
from sqlalchemy import String
from hashlib import md5
from os import getenv

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
    if models.storage == 'db':
        __tablename__ = "users"
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128))
        last_name = Column(String(128))
        places = relationship("Place", backref="user", cascade="delete")
        reviews = relationship("Review", backref="user", cascade="delete")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""


    def __init__(self, *args, **kwargs):
        """ constructpr for the task
            
            Args:
            kwargs: Additional keyword 

        """
        if kwargs:
            pwd = kwargs.pop('password', None)
            if pwd:
                secure = hashlib.md5()
                secure.update(pwd.encode("utf-8"))
                secure_pass = secure.hexdigest()
                kwargs['password'] = secure_pass
        super().__init__(*args, **kwargs)
