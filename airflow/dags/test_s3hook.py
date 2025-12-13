from datetime import datetime

from airflow.providers.amazon.aws.hooks.s3 import S3Hook
from airflow.sdk import dag, task

S3_BUCKET = "weather-cheddr-weddr"


@dag(
    dag_id="test_s3hook",
    description="",
    start_date=datetime(2025, 1, 1),
    catchup=False,
)
def test_s3hook():
    @task()
    def t1():
        hook = S3Hook(aws_conn_id="aws_default")
        hook.load_string(
            string_data="Hello World!",
            key="random.txt",
            bucket_name=S3_BUCKET,
        )

    t1()


test_s3hook()
