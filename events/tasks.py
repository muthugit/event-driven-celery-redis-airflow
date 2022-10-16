from celery import Celery
from datetime import datetime
from airflow import DAG
from datetime import datetime, timedelta
from requests.auth import HTTPBasicAuth
import requests
import json
import base64
from dateutil import tz
from zoneinfo import ZoneInfo


from_zone = tz.gettz('UTC')
to_zone = tz.gettz('America/New_York')



REDIS_HOST = "localhost"
REDIS_PORT = 6379

app = Celery('tasks', backend=f'redis://{REDIS_HOST}:{REDIS_PORT}/0', broker=f'redis://{REDIS_HOST}:{REDIS_PORT}/0')

@app.task
def add(x, y):
    return x + y


@app.task
def af():
    from requests.auth import HTTPBasicAuth
    import requests
    import json
    import base64
    from dateutil import tz
    from zoneinfo import ZoneInfo
    from datetime import datetime
    from airflow import DAG
    from datetime import datetime, timedelta


    print("Executing")
    airflow_host = "localhost:8080"
    airflow_username = "airflow"
    airflow_password = "airflow"

    dag = "first_sample_dag"
    url = f'http://{airflow_host}/api/v1/dags/{dag}/dagRuns'
    up = f"{airflow_username}:{airflow_password}".encode("utf=8")
    
    headers = {
        'Content-type': 'application/json', 
        # 'Accept': 'application/json',
        # 'Authorization': f"B {base64.b64encode(up)}"
    }
    data = {
        'conf': {}
    }
    print(url)
    result = requests.post(
        url,
        json=data,
        headers=headers,
        auth=(airflow_username, airflow_password)
    )
    result_json = result.json()
    print(result_json)
    return True


# af()

