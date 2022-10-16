# Celery - Redis - Airflow
[A proof of concept]



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