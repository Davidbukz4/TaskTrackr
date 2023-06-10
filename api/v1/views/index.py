#!/usr/bin/python3
'''
Returns the status of the app
'''
from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.user import User
from models.task import Task
app_views.url_defaults = {'strict_slashes': False}


@app_views.route('/status')
def status():
    ''' Returns status of API '''
    return jsonify({'status': 'OK'})

@app_views.route('/stats/users', strict_slashes=False)
def all_stats():
    ''' Returns status of task of each user '''
    stat_dict = []
    objs = storage.all(Task)
    for key, value in objs.items():
        obj_dict = {}
        value = value.to_dict()
        obj_dict['Task_id'] = value['id']
        obj_dict['title'] = value['title']
        obj_dict['description'] = value['description']
        obj_dict['completed'] = value['completed']
        obj_dict['User_id'] = value['user_id']
        stat_dict.append(obj_dict)
    return jsonify(stat_dict)


@app_views.route('/stats/users/<int:user_id>', strict_slashes=False)
def user_stats(user_id):
    ''' Returns status of task of a user by user id '''
    stat_dict = []
    objs = storage.user_tasks(int(user_id))[0]
    if objs is not None:
        for key, value in objs.items():
            #key = 'task.{}'.format(user_id)
            #if key in objs:
            obj_dict = {}
            obj_dict['Task_id'] = objs[key]['id']
            obj_dict['title'] = objs[key]['title']
            obj_dict['description'] = objs[key]['description']
            obj_dict['completed'] = objs[key]['completed']
            obj_dict['User_id'] = objs[key]['user_id']
            stat_dict.append(obj_dict)
        return jsonify(stat_dict)
    return jsonify({})
