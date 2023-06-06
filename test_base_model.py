#!/usr/bin/python3
from models.task import Task

task1 = Task()
task1.name = 'first task'
task1.number = 1
print(task1)
task1.save()
print(task1)
task1_json = task1.to_dict()
print(task1_json)
