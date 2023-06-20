# TaskTrackr


## Description

TaskTrackr is task management web application that help users manage their tasks effectively. It provides features such as the save, edit, add, cancel and delete task option, task highlighting when due date has reached. More features coming soon.
Currently the
application is designed to run with 1 storage engine model:


* Database Storage Engine:

  * `/models/engine/storage.py`

  * To Setup the DataBase for testing and development, there are 2 setup
  scripts that setup a database with certain privileges: `setup_mysql_test.sql`
  & `setup_mysql_dev.sql` (for more on setup, see below).

  * The Database uses Environmental Variables for tests.  To execute tests with
  the environmental variables prepend these declarations to the execution
  command:

```
$ TTR_MYSQL_USER=ttr_test TTR_MYSQL_PWD=ttr_test_pwd \
TTR_MYSQL_HOST=localhost TTR_MYSQL_DB=ttr_test_db TTR_TYPE_STORAGE=db \
[COMMAND HERE]
```

## Environment

* __OS:__ Ubuntu 20.04 LTS
* __language:__ Python 3.8.10
* __web server:__ nginx/1.4.6
* __application server:__ Flask 2.2.0, Jinja2 3.1.2
* __web server gateway:__ gunicorn (version 19.7.1)
* __database:__ mysql Ver 8.0.33
* __style:__
  * __python:__ PEP 8 (v. 1.7.0)
  * __web static:__ [W3C Validator](https://validator.w3.org/)
  * __bash:__ ShellCheck 0.3.3

<img src="https://github.com/davidbukz4/TaskTrackr/static/images/screenshot.png" />

## Requirements

* MySQLdb==2.0.x
* SQLAlchemy==1.4.x
* bcrypt==3.1.7
* Flask==2.2.0
* Flask-Cors==3.0.10
* Flask-Login==0.6.2
* Flask-RESTful==0.3.9
* Flask-SQLAlchemy==3.0.3
* Flask-WTF==1.1.1
* email-validator==2.0.0.post2
* WTForms==3.0.1

---

## Testing

### `unittest`

This project uses python library, `unittest` to run tests on all python files.
All unittests are in the `./tests` directory with the command:
```
python3 -m unittest discover tests
```


* DataBase Storage Engine Model

```
$ TTR_MYSQL_USER=ttr_test TTR_MYSQL_PWD=ttr_test_pwd \
TTR_MYSQL_HOST=localhost TTR_MYSQL_DB=ttr_test_db TTR_TYPE_STORAGE=db \
python3 -m unittest discover -v ./tests/
```

---


## Authors

* Esther Ekanem, [ESTHEREKANEM](https://github.com/ESTHEREKANEM)
* David Egwuatu, [Davidbukz4](https://github.com/davidbukz4)


