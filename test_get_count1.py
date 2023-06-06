#!/usr/bin/python3
'''
Test get and count method of storage class
'''
from models import storage
from models.task import Task

print('All objects: {}'.format(storage.count()))
print('Task objects: {}'.format(storage.count(Task)))

res = list(storage.all(Task).values())
print(res[0].to_dict())
#first_user_id = list(res)[0].id
#print('First state: {}'.format(storage.get(User, first_user_id)))
