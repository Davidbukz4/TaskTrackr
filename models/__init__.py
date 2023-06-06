#!/usr/bin/python3
'''
CREATES AN INSTANCE OF DB STORAGE
'''
from models.engine.storage import Storage
from models.user import User
from models.task import Task


storage = Storage()
storage.reload()
