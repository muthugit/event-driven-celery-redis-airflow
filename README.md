# event-driven-celery-redis-airflow

celery -A events.tasks worker --loglevel=INFO


https://towardsdatascience.com/a-complete-introduction-to-apache-airflow-b7e238a33df

https://towardsdatascience.com/setting-up-apache-airflow-with-docker-compose-in-5-minutes-56a1110f4122

```
pip install airflow

export AIRFLOW_HOME=$PWD/events

airflow db init

airflow users  create --role Admin --username admin --email admin --firstname admin --lastname admin --password admin

airflow webserver --port 8081

airflow scheduler

airflow webserver \
--pid ${AIRFLOW_HOME}/logs/airflow-webserver.pid \
--stdout ${AIRFLOW_HOME}/logs/airflow-webserver.out \
--stderr ${AIRFLOW_HOME}/logs/airflow-webserver.out \
-l ${AIRFLOW_HOME}/logs/airflow-webserver.log \
-p 8080
-D

airflow scheduler \
--pid ${AIRFLOW_HOME}/logs/airflow-scheduler.pid \
--stdout ${AIRFLOW_HOME}/logs/airflow-scheduler.out \
--stderr ${AIRFLOW_HOME}/logs/airflow-scheduler.out \
-l ${AIRFLOW_HOME}/logs/airflow-scheduler.log \
-D

```