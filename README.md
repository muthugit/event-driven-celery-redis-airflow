# event-driven-celery-redis-airflow

celery -A events.tasks worker --loglevel=INFO


https://towardsdatascience.com/a-complete-introduction-to-apache-airflow-b7e238a33df

https://towardsdatascience.com/setting-up-apache-airflow-with-docker-compose-in-5-minutes-56a1110f4122

## Install the dependencies
```
pip install -r requirements.txt
```

## Start the Celery
```
celery -A events.tasks worker --loglevel=INFO
```

## Start the services
```
docker-compose up --build
```

## Send message
```python
import redis
REDIS_HOST = "localhost"
REDIS_PORT = 6379
r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0)
r.publish("tasks", "run a task")
```