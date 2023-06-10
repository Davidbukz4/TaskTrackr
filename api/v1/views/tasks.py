#!/usr/bin/python3
'''
Creates a new view for task objects
'''
from models import storage
from models.task import Task
from api.v1.views import app_views
from flask import jsonify, abort, request
from datetime import datetime


@app_views.route('/tasks', methods=['GET'], strict_slashes=False)
def all_task():
    ''' Returns all stored task '''
    objs = storage.all(Task)
    if objs is None:
        abort(404)
    task_dict = {}
    for key, value in objs.items():
        task_dict[key] = value.to_dict()
        del task_dict[key]['__class__']
    return jsonify(task_dict)

@app_views.route('/tasks/<int:task_id>', methods=['GET'],
                 strict_slashes=False)
def task_by_id(task_id):
    ''' Gets a task object by id '''
    task = storage.get(Task, task_id)
    if task is None:
        abort(404)
    if task is None:
        abort(404)
    task = task.to_dict()
    del task['__class__']
    return jsonify(task)

@app_views.route('/tasks/user/<int:user_id>', methods=['GET'],
                 strict_slashes=False)
def user_tasks(user_id):
    ''' Returns all tasks of a user by id '''
    stat_dict = []
    objs = storage.user_tasks(int(user_id))[0]
    if objs is not None:
        for key, value in objs.items():
            #key = 'task.{}'.format(user_id)
            #if key in objs:
            obj_dict = {}
            obj_dict['User_id'] = objs[key]['user_id']
            obj_dict['title'] = objs[key]['title']
            obj_dict['description'] = objs[key]['description']
            obj_dict['completed'] = objs[key]['completed']
            obj_dict['due_date'] = objs[key]['due_date']
            obj_dict['updated_at'] = objs[key]['updated_at']
            obj_dict['created_at'] = objs[key]['created_at']
            obj_dict['Task_id'] = objs[key]['id']
            stat_dict.append(obj_dict)
        return jsonify(stat_dict)
    return jsonify({})

@app_views.route('/tasks/<int:task_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_task(task_id):
    ''' Deletes a task object '''
    if task_id is None:
        abort(404)
    user = storage.get(Task, task_id)
    if user is None:
        abort(404)
    storage.delete(Task, task_id)
    storage.save()
    return jsonify({}), 200

@app_views.route('/tasks/<int:user_id>', methods=['POST'],
                 strict_slashes=False)
def post_task(user_id):
    ''' Creates a task '''
    res = request.get_json()
    if type(res) != dict:
        return abort(400, {'message': 'Not a JSON'})
    attr = ['title', 'description', 'due_date']
    for x in attr:
        if x not in res:
            return abort(400, {'message': 'Missing {}'.format(x)})
    date = datetime.strptime(res['due_date'], '%Y-%m-%d')
    user_objs = storage.user_info()
    user_ids = []
    for item in user_objs:
        user_ids.append(item['id'])
    if user_id not in user_ids:
        return abort(404)
    new_task = Task(title=res['title'], description=res['description'],
                    due_date=date, user_id=user_id)
    new_task.save()
    new_task = new_task.to_dict()
    del new_task['__class__']
    return jsonify(new_task), 201

@app_views.route('/tasks/<int:task_id>', methods=['PUT'],
                 strict_slashes=False)
def update_task(task_id):
    ''' Updates a user '''
    user = storage.get(Task, task_id)
    if user is None:
        abort(404)
    res = request.get_json()
    if type(res) != dict:
        abort(400, {'message': 'Not a JSON'})
    for key, value in res.items():
        if key == 'due_date':
            value = datetime.strptime(res['due_date'], '%Y-%m-%d')
            setattr(user, key, value)
        if key not in ['id']:
            setattr(user, key, value)
    storage.save()
    new_user = user.to_dict()
    del new_user['__class__']
    return jsonify(new_user), 200
