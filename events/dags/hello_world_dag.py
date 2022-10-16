from airflow.models import DAG
from airflow.utils.dates import days_ago
from airflow.operators.python import PythonOperator
from datetime import timedelta, datetime

# initializing the default arguments
default_args = {
		'owner': 'Ranga',
		'start_date': datetime(2022, 3, 4),
		'retries': 3,
		'retry_delay': timedelta(minutes=5)
}

# Instantiate a DAG object
hello_world_dag = DAG('hello_world_dag',
		default_args=default_args,
		description='Hello World DAG',
		schedule_interval='* * * * *', 
		catchup=False,
		tags=['example, helloworld']
)

# python callable function
def print_hello():
	print("====")
	return 'Hello World!'


# # Creating second task
hello_world_task = PythonOperator(task_id='hello_world_task', python_callable=print_hello, dag=hello_world_dag)


# # Set the order of execution of tasks. 
hello_world_task


# with DAG("my_dag", start_date=datetime.now() as dag:
#     op = PythonOperator(task_id='hello_world_task', python_callable=print_hello)
#     print(op.owner)	