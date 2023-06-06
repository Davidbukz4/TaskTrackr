#!/usr/bin/python3
'''
USER MODEL
'''
import models
from models.base_model import Base, BaseModel
from uuid import uuid4
from datetime import datetime
import sqlalchemy
from sqlalchemy import Column, String, Integer, DateTime, func
from sqlalchemy import create_engine, Boolean, ForeignKey, Sequence
from sqlalchemy.orm import relationship, sessionmaker


class User(BaseModel, Base):
    ''' Representation of user '''
    __tablename__ = 'users'

    id = Column(Integer, Sequence('user_id_seq', start=1, increment=1),
                primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(256), nullable=False)
    tasks = relationship("Task", backref="users")
    
    def __init__(self, username, password):
        ''' initializes an instance of the model '''
        self.username = username
        self.password = password
