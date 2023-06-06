#!/usr/bin/python3
'''
USER MODEL
'''
#import models
from uuid import uuid4
from datetime import datetime
import sqlalchemy
from sqlalchemy import Column, String, Integer, DateTime, func, create_engine, Boolean, ForeignKey, Sequence
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = sqlalchemy.orm.declarative_base()


class User(Base):
    ''' Representation of user '''
    __tablename__ = 'users'

    id = Column(Integer, Sequence('user_id_seq', start=1, increment=1),
                primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(256), nullable=False)
    tasks = relationship("Task", backref="users")
    
    def __init__(self, username, password):
        ''' initializes an instance of the model '''
        self.username = username
        self.password = password
        #self.id = id
        #self.created_at = datetime.utcnow()
        #self.updated_at = self.created_at
        # code to save new object

    def __str__(self):
        ''' returns a string representation of an object '''
        return '[{}] ({}) {}'.format(type(self).__name__, self.id,
                                     self.__dict__)

    def save(self):
        ''' updates the attribute "updated_at" with the current time '''
        self.updated_at = datetime.utcnow()
        # code to save changes

    def to_dict(self):
        ''' returns a dictionary containing all key-value pair of the obj '''
        objs = self.__dict__.copy()
        objs['__class__'] = self.__class__.__name__
        objs['created_at'] = objs['created_at'].isoformat()
        objs['updated_at'] = objs['updated_at'].isoformat()
        return objs

class Task(Base):
    ''' Representation of task '''
    __tablename__ = 'tasks'

    id = Column(Integer, Sequence('task_id_seq', start=1, increment=1),
                     primary_key=True)
    title = Column(String(100), nullable=False)
    description = Column(String(256))
    completed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    due_date = Column(DateTime)

    def __init__(self, title, description, completed, due_date, user_id):
        self.title = title
        self.description = description
        self.completed = completed
        self.due_date = due_date
        self.user_id = user_id


engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                       .format('david', 'david', 'alx'),
                       pool_pre_ping=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

user1 = User(username='chris', password='pwd123')
user2 = User(username='ace', password='pwd456')
user3 = User(username='dada', password='pwd789')

session.add(user1)
session.add(user2)
session.add(user3)
session.commit()


task1 = Task(title='laundry', description='this is my first task', due_date=datetime(2023, 6, 7), completed=False, user_id=user1.id)
task2 = Task(title='dishes', description='this is my first task', due_date=datetime(2023, 6, 8), completed=True, user_id=user2.id)
task3 = Task(title='groceries', description='this is my first task', due_date=datetime(2023, 6, 9), completed=False, user_id=user3.id)


session.add(task1)
session.add(task2)
session.add(task3)
session.commit()

task = session.query(Task).filter(Task.id == 1).one()
task.title = 'Gym'
task.updated_at = func.now()
session.commit()

session.close()
