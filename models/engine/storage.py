#!/usr/bin/python3
"""
Contains the DBStorage class
"""

import models
from models.user import User, Base
from models.task import Task
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

classes = {"User": User, "Task": Task}


class Storage:
    """interaacts with the MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        TTR_MYSQL_USER = getenv('TTR_MYSQL_USER')
        TTR_MYSQL_PWD = getenv('TTR_MYSQL_PWD')
        TTR_MYSQL_HOST = getenv('TTR_MYSQL_HOST')
        TTR_MYSQL_DB = getenv('TTR_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(TTR_MYSQL_USER,
                                             TTR_MYSQL_PWD,
                                             TTR_MYSQL_HOST,
                                             TTR_MYSQL_DB))

    def get(self, cls, id):
        """ Retrieves an object """
        if cls in classes.values() and id:
            objs = self.all(cls)
            for k, v in objs.items():
                v = v.to_dict()
                if v['id'] == int(id):
                    return objs[k]
        return None

    def count(self, cls=None):
        """ Returns the number of objects in storage """
        objs = self.all(cls) if cls else {}
        return len(objs)

    def all(self, cls=None):
        """ Returns a dictionary of objects """
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(cls).all()
                if objs is not None:
                    for obj in objs:
                        key = obj.__class__.__name__ + '.' + str(obj.id)
                        new_dict[key] = obj
                return new_dict
        return {}

    def user_tasks(self, id):
        ''' Returns the number of tasks associated with a user '''
        user_tasks = self.__session.query(Task).filter(Task.user_id == id)
        task_count = 0
        tasks = {}
        for obj in user_tasks:
            obj = obj.to_dict()
            tasks['task.{}'.format(obj['id'])] = obj
            task_count += 1
        return [tasks, task_count]

    def user_info(self):
        ''' Returns users info '''
        objs = self.__session.query(User)
        users = []
        for obj in objs:
            obj = obj.to_dict()
            del obj['__class__']
            users.append(obj)
        return users

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, cls, id):
        """delete from the current database session obj if not None"""
        #if obj is not None and not(id):
        #   self.__session.delete(obj)
        if cls in classes.values():
            self.__session.query(cls).filter_by(id=id).delete()

    def reload(self):
        """ creates all table in the database and database session """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                    expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """call close() method on the private session attribute"""
        self.__session.close()
