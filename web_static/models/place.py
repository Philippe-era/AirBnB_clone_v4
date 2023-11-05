#!/usr/bin/python3
"""Place class blueprint implementation"""
import models
from os import getenv
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Table
from models.amenity import Amenity
from models.review import Review
from sqlalchemy.orm import relationship


table_place= Table("place_amenity", Base.metadata,
                          Column("place_id", String(60),
                                 ForeignKey("places.id"),
                                 primary_key=True, nullable=False),
                          Column("amenity_id", String(60),
                                 ForeignKey("amenities.id"),
                                 primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """Place database
    Attributes:
        __tablename__ (str): table storing the information of place
        city_id (sqlalchemy String): the city identity number
        user_id (sqlalchemy String): the user identity
        name (sqlalchemy String): the string name
        description (sqlalchemy String): the information needed
        number_rooms (sqlalchemy Integer): The number of rooms.
        number_bathrooms (sqlalchemy Integer): The number of bathrooms.
        max_guest (sqlalchemy Integer): The maximum number of guests.
        price_by_night (sqlalchemy Integer): per night prince
        latitude (sqlalchemy Float): latitutde of the place
        longitude (sqlalchemy Float): longitude of the place
        reviews (sqlalchemy relationship): place - review relationship
        amenities (sqlalchemy relationship): places linked
        amenity_ids (list): list of places
    """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0)
    number_bathrooms = Column(Integer, default=0)
    max_guest = Column(Integer, default=0)
    price_by_night = Column(Integer, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    reviews = relationship("Review", backref="place", cascade="delete")
    amenities = relationship("Amenity", secondary="place_amenity",
                             viewonly=False)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE", None) != "db":
        @property
        def reviews(self):
            """links all review places"""
            list_of_reviews = []
            for review in list(models.new_storage.all(Review).values()):
                if review.place_id == self.id:
                   list_of_reviews.append(review)
            return list_of_reviews

        @property
        def amenities(self):
            """gets the linked inallll."""
            place_lists = []
            for amenity in list(models.new_storage.all(Amenity).values()):
                if amenity.id in self.amenity_ids:
                    place_lists.append(amenity)
            return place_lists

        @amenities.setter
        def amenities(self, value):
            if type(value) == Amenity:
                self.amenity_ids.append(value.id)
