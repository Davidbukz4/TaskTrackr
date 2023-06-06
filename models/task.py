#!/usr/bin/python3
'''
TASK MODEL
'''
import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Sequence
from sqlalchemy import ForeignKey, func

class Task(BaseModel, Base):
    ''' Representation of task '''
    __tablename__ = 'tasks'

    id = Column(Integer, Sequence('task_id_seq', start=1, increment=1),
                     primary_key=True)
    title = Column(String(100), nullable=False)
    description = Column(String(256))
    completed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    due_date = Column(DateTime)

    def __init__(self, title, description, completed, due_date, user_id):
        ''' Initializes instance of the class '''
        self.title = title
        self.description = description
        self.completed = completed
        self.due_date = due_date
        self.user_id = user_id
