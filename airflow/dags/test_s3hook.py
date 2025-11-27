from datetime import datetime, timedelta
from airflow.sdk import dag, task
from airflow.providers.amazon.aws.hooks.s3 import S3Hook

@dag(
    dag_id = "test_s3hook",
    description = "",
    start_date = datetime(2025, 1, 1),
    # schedule = timedelta(days=1),
    catchup = False,
)
def test_s3hook():
    @task()
    def t1():
        pass

    @task()
    def t2():
        pass

    t1() >> t2()

test_s3hook()