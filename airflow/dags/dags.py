from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'embiekhochiu',
    'depends_on_past': False,
    'start_date': datetime(2023, 4, 2),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG('scrapy_dag', default_args=default_args, schedule_interval= '@daily')

t1 = DockerOperator(
    task_id='run_scrapy',
    image='scrapy_project:latest',
    api_version='auto',
    auto_remove=True,
    command='scrapy crawl linkedin_jobs',  
    docker_url="unix://var/run/docker.sock",
    network_mode="bridge",
    dag=dag
)
