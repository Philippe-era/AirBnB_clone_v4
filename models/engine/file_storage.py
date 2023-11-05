#!/usr/bin/python3
"""
FileStorage is contained in this module
"""

import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.state import State
from hashlib import md5

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class FileStorage:
    """instances of the serialization"""

    # JSON FILE CREATED
    __file_path = "file.json"
    #DICTIONARY 
    __objects = {}

    def all(self, cls=None):
        """dictionary will be returned"""
        if cls is not None:
            new_dict = {}
            for key, value in self.__objects.items():
                if cls == value.__class__ or cls == value.__class__.__name__:
                    new_dict[key] = value
            return new_dict
        return self.__objects

    def get(self, cls, id):
        """This will return all involved with id"""
        if cls is not None:
            res = list(
                filter(
                    lambda x: type(x) is cls and x.id == id,
                    self.__objects.values()
                )
            )
            if res:
                return res[0]
        return None

    def count(self, cls=None):
        """This returns the info"""
        return len(self.all(cls))

    def new(self, obj):
        """sets the objects in check"""
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """Serilaizations for this task"""
        json_objects = {}
        for key in self.__objects:
            json_objects[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(json_objects, f)

    def reload(self):
        """desiralization of the objetcs"""
        try:
            with open(self.__file_path, 'r') as f:
                jo = json.load(f)
            for key in jo:
                self.__objects[key] = classes[jo[key]["__class__"]](**jo[key])
        except Exception:
            pass

    def delete(self, obj=None):
        """The object will be deleted"""
        if obj is not None:
            key = obj.__class__.__name__ + '.' + obj.id
            if key in self.__objects:
                del self.__objects[key]

    def close(self):
        """JSON to object"""
        self.reload()

