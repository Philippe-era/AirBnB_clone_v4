#!/usr/bin/python3
"""the engine of the database will be created now """
from os import getenv
from models.base_model import Base
from models.base_model import BaseModel
from models.amenity import Amenity
from models.state import State
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from models.city import City
from models.place import Place
from models.review import Review



class DBStorage:
    """ENGINE REPRESENTED IN THIS DATABASE

    Attributes:
        __engine (sqlalchemy.Engine): The working SQLAlchemy engine.
        __session (sqlalchemy.Session): The working SQLAlchemy session.
    """

    __engine = None
    __session = None

    def __init__(self):
        """Initialize a new DBStorage instance."""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                      format(getenv("HBNB_MYSQL_USER"),
                                             getenv("HBNB_MYSQL_PWD"),
                                             getenv("HBNB_MYSQL_HOST"),
                                             getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """CURRENT DATABASE QUERY EXECUTED 

        
        Return:
            DICTIONARY RETURNED 
        """
        if cls is None:
            object_create = self.__session.query(State).all()
            object_create.extend(self.__session.query(City).all())
            object_create.extend(self.__session.query(User).all())
            object_create.extend(self.__session.query(Place).all())
            object_create.extend(self.__session.query(Review).all())
            object_create.extend(self.__session.query(Amenity).all())
        else:
            if type(cls) == str:
                cls = eval(cls)
            object_create = self.__session.query(cls)
        return {"{}.{}".format(type(o).__name__, o.id): o for o in object_create}

    def new(self, obj):
        """OBJECT WILL BE ADDED TO THE INFORMATION"""
        self.__session.add(obj)

    def save(self):
        """commit to all databases"""
        self.__session.commit()

    def delete(self, obj=None):
        """remove database object"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """creation of tables ."""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """session closed in one space"""
        self.__session.close()

