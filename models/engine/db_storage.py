#!/usr/bin/python3
"""
Module - DBStorage
"""
from os import getenv
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
from models.state import State
from models.city import City
from models.base_model import Base


class DBStorage():
    """
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        Create engine and link to MySQL Database
        """
        user = getenv("HBNB_MYSQL_USER")
        pwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        env = getenv("HBNB_ENV", "none")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, pwd, host, db), pool_pre_ping=True)
        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Query current database session
        """

        db_dict = {}
        if cls is not None:
            objects = self.__session.query(model.classes[cls]).all()
            for obj in objects:
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                db_dict[key] = obj
            return db_dict
        else:
            for k, v in model.classes.items():
                if k != "BaseModel":
                    objects = self.__session.query(v).all()
                    for obj in objects:
                         key = "{}.{}".format(obj.__class__.__name__, obj.id)
                         db_dict[key] = obj
            return db_dict

    def new(self, obj):
        """
        Add Object to current database session
        """
        self.__session.add(obj)

    def save(self):
        """
        commit all changes of current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Delete from the current database session
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        self.__session = Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine, expire_on_commit=False))
        self.__session = Session()

