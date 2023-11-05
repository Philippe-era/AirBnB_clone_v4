"""Defines the State class."""
import models
from os import getenv
from sqlalchemy import String
from sqlalchemy.orm import relationship
from models.base_model import Base
from models.base_model import BaseModel
from models.city import City
from sqlalchemy import Column


class State(BaseModel, Base):
    """database with infromation of states stored

    Attributes:
        __tablename__ (str): The name of the MySQL table to store States.
        name (sqlalchemy String): The name of the State.
        cities (sqlalchemy relationship): The State-City relationship.
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City",  backref="state", cascade="delete")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """all objects of citites will be returned in context."""
            list_of_cities = []
            for city in list(models.new_storage.all(City).values()):
                if city.state_id == self.id:
                    list_of_cities.append(city)
            return list_of_cities
