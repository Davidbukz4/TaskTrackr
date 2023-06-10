#!/usr/bin/python3
'''
Creates a new view for user objects
'''
from models import storage
from models.user import User
from api.v1.views import app_views
from flask import jsonify, abort, request


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def read_all():
    ''' Returns all stored users '''
    objs = storage.user_info()
    if objs is None:
        abort(404)
    return jsonify(objs)

@app_views.route('/users/<int:user_id>', methods=['GET'],
                 strict_slashes=False)
def read_by_id(user_id):
    ''' Gets a user object by id '''
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    if user is None:
        abort(404)
    user = user.to_dict()
    del user['__class__']
    return jsonify(user)

@app_views.route('/users/<int:user_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete(user_id):
    ''' Deletes a user objects '''
    if user_id is None:
        abort(404)
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    storage.delete(User, user_id)
    storage.save()
    return jsonify({}), 200

@app_views.route('/users', methods=['POST'], strict_slashes=False)
def post():
    ''' Creates a user '''
    res = request.get_json()
    if type(res) != dict:
        return abort(400, {'message': 'Not a JSON'})
    attr = ['username', 'password', 'email']
    for x in attr:
        if x not in res:
            return abort(400, {'message': 'Missing {}'.format(x)})
    new_user = User(username=res['username'], password=res['password'],
                    email=res['email'])
    new_user.save()
    new_user = new_user.to_dict()
    del new_user['__class__']
    del new_user['updated_at']
    return jsonify(new_user), 201

@app_views.route('/users/<int:user_id>', methods=['PUT'],
                 strict_slashes=False)
def update(user_id):
    ''' Updates a user '''
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    res = request.get_json()
    if type(res) != dict:
        abort(400, {'message': 'Not a JSON'})
    for key, value in res.items():
        if key not in ['id']:
            setattr(user, key, value)
    storage.save()
    new_user = user.to_dict()
    del new_user['__class__']
    return jsonify(new_user), 200
