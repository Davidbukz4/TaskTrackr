#!/usr/bin/python3
'''
TASK MODEL
'''
import models
from models.user import User


class Task(User):
    ''' Representation of task '''

    id = ''
    title = ''
    description = ''
    due_date = ''
    completed = ''
    user_id = ''

    def __init__(self):
        super().__init__()
