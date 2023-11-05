#!/usr/bin/python3
"""Base model set and ready you check"""
import models
from uuid import uuid4
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import String

Base = declarative_base()


class BaseModel:
    """IMplementation of the base model class

    Attributes:
        id (sqlalchemy String): The id set and in control
        created_at (sqlalchemy DateTime): the date time it was created
        updated_at (sqlalchemy DateTime): the last time it was updated
    """

    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Prototype of the thing

        Args:
            *args (any): Not used
            **kwargs (dict): pairs in question.
        """
        self.id = str(uuid4())
        self.created_at = self.updated_at = datetime.utcnow()
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)

    def save(self):
        """updated time."""
        self.updated_at = datetime.utcnow()
        models.new_storage.new(self)
        models.new_storage.save()

    def to_dict(self):
        """dictionary will be return
        """
        dictionary_mine = self.__dict__.copy()
        dictionary_mine["__class__"] = str(type(self).__name__)
        dictionary_mine["created_at"] = self.created_at.isoformat()
        dictionary_mine["updated_at"] = self.updated_at.isoformat()
        dictionary_mine.pop("_sa_instance_state", None)
        return dictionary_mine

    def delete(self):
        """delete current object"""
        models.new_storage.delete(self)

    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        d = self.__dict__.copy()
        d.pop("_sa_instance_state", None)
        return "[{}] ({}) {}".format(type(self).__name__, self.id, d)
