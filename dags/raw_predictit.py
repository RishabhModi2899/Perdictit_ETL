import json
import requests
import datetime
import boto3
import airflow
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator

start_date = airflow.utils.dates.days_ago(2)

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "email": ["airflow@example.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": datetime.timedelta(minutes=5),
}


def json_scrapper(url, file_name, bucket):
    response = requests.request("GET", url)
    json_data = response.json()

    with open(file_name, 'w', encoding='utf-8') as json_file:
        json.dump(json_data, json_file, ensure_ascii=False, indent=4)

    s3 = boto3.client('s3')
    s3.upload_file(file_name, bucket, f"predictit/{file_name}")


with DAG(
    "raw_predictit",
    default_args=default_args,
    # schedule_interval=datetime.timedelta(days=1),
    schedule_interval="*/15 * * * *",
    start_date=start_date,
    catchup=False,
    tags=['sdg'],
) as dag:
    extract_predictit = PythonOperator(
        task_id='extract_predictit',
        python_callable=json_scrapper,
        op_kwargs={
            'url': "https://www.predictit.org/api/marketdata/all/",
            "file_name": 'predict_markets.json',
            'bucket': "predictit-s3-bucket"},
        dag=dag
    )

    ready = DummyOperator(task_id="ready")

    extract_predictit >> ready
