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
* __language:__ Python 3.8.3
* __web server:__ nginx/1.4.6
* __application server:__ Flask 2.2.0, Jinja2 2.9.6
* __web server gateway:__ gunicorn (version 19.7.1)
* __database:__ mysql Ver 14.14 Distrib 5.7.18
* __documentation:__ Swagger (flasgger==0.6.6)
* __style:__
  * __python:__ PEP 8 (v. 1.7.0)
  * __web static:__ [W3C Validator](https://validator.w3.org/)
  * __bash:__ ShellCheck 0.3.3

<img src="https://github.com/davidbukz4/TaskTrackr/blob/master/dev/screenshot.png" />

---

## Testing

### `unittest`

This project uses python library, `unittest` to run tests on all python files.
All unittests are in the `./tests` directory with the command:


* DataBase Storage Engine Model

```
$ TTR_MYSQL_USER=ttr_test TTR_MYSQL_PWD=ttr_test_pwd \
TTR_MYSQL_HOST=localhost TTR_MYSQL_DB=ttr_test_db TTR_TYPE_STORAGE=db \
python3 -m unittest discover -v ./tests/
```

---

### All Tests

The bash script `init_test.sh` executes all these tests for 
DataBase Engine Model:

  * checks `pep8` style

  * runs all unittests

  * runs all w3c_validator tests

  * cleans up all `__pycache__` directories and unused files.

  * **Usage `init_test.sh`:**

```
$ ./dev/init_test.sh
```



## Authors

* Esther Ekanem, [ESTHEREKANEM](https://github.com/ESTHEREKANEM)
* David Egwuatu, [Davidbukz4](https://github.com/davidbukz4)


