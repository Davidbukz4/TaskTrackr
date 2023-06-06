#!/usr/bin/python3
'''
Test get and count method of storage class
'''
from models import storage
from models.user import User

print('All objects: {}'.format(storage.count()))
print('User objects: {}'.format(storage.count(User)))

#res = list(storage.all(User).values())
#print(res[0].to_dict())
#first_user_id = list(res)[0].id
#print('First state: {}'.format(storage.get(User, first_user_id)))

print(storage.get(User, 6))
storage.close()
