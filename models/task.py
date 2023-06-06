#!/usr/bin/python3
'''
TASK MODEL
'''
import models
from models.user import User, Base
import sqlalchemy
from sqlalchemy import Column, Integer, String, Boolean, DateTime


class Task(User, Base):
    ''' Representation of task '''
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, autoincrement='auto',
                server_default='1')
    title = Column(String(100), nullable=False)
    description = Column(String(256))
    completed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    due_date = Column(DateTime)


    def __init__(self):
        super().__init__()
