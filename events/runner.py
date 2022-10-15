from celery import Celery
import redis
from events.tasks import add

REDIS_HOST = "localhost"
REDIS_PORT = 6379

r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0)
sub = r.pubsub()
sub.subscribe("tasks")
while True:
    msg = sub.get_message()
    if msg is not None:
        print("Running...")
        res=add.delay(2,2)
        res.get(timeout=1)




