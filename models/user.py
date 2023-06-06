#!/usr/bin/python3
'''
USER MODEL
'''
import models
from uuid import uuid4
from datetime import datetime
import sqlalchemy
from sqlalchemy import Column, String, Integer, DateTime, func, create_engine
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    ''' Representation of user '''
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement='auto',
                server_default='1000')
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(256), nullable=False)
    tasks = relationship("Task", backref="users")
    
    
    def __init__(self):
        ''' initializes an instance of the model '''
        #self.id = str(uuid4())
        #self.created_at = datetime.utcnow()
        #self.updated_at = self.created_at
        # code to save new object

    def __str__(self):
        ''' returns a string representation of an object '''
        return '[{}] ({}) {}'.format(type(self).__name__, self.id,
                                     self.__dict__)

    def save(self):
        ''' updates the attribute "updated_at" with the current time '''
        self.updated_at = datetime.utcnow()
        # code to save changes

    def to_dict(self):
        ''' returns a dictionary containing all key-value pair of the obj '''
        objs = self.__dict__.copy()
        objs['__class__'] = self.__class__.__name__
        objs['created_at'] = objs['created_at'].isoformat()
        objs['updated_at'] = objs['updated_at'].isoformat()
        return objs



engine = create_engine()
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

user1 = User()