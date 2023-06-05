#!/usr/bin/python3
'''
CREATES AN INSTANCE OF DB STORAGE
'''
from models.engine.storage import Storage


storage = Storage()
storage.reload()
