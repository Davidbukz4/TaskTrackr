#!/usr/bin/python3
import multiprocessing
import os

# Bind to the appropriate host and port
bind = '127.0.0.1:8000'

# Number of worker processes
workers = multiprocessing.cpu_count() * 2 + 1

# Set the maximum number of requests a worker will process before restarting
max_requests = 1000

# Set the maximum number of simultaneous clients that a single worker can handle
worker_connections = 1000

# Specify the modules and applications to be served by Gunicorn
web_app_module = 'web_app.app'
api_v1_module = 'api.v1.app'

# Set up your environment variables
os.environ['TTR_MYSQL_USER'] = 'ttr_dev'
os.environ['TTR_MYSQL_PWD'] = 'ttr_dev_pwd'
os.environ['TTR_MYSQL_HOST'] = 'localhost'
os.environ['TTR_MYSQL_DB'] = 'ttr_dev_db'

# Logging configuration
accesslog = '-'  # Log to stdout
errorlog = '-'   # Log to stderr
