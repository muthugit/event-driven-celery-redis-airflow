from celery import Celery
from datetime import datetime
from airflow import DAG

REDIS_HOST = "localhost"
REDIS_PORT = 6379

app = Celery('tasks', backend=f'redis://{REDIS_HOST}:{REDIS_PORT}/0', broker=f'redis://{REDIS_HOST}:{REDIS_PORT}/0')

@app.task
def add(x, y):
    return x + y




