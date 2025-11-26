from airflow.sdk import dag, task
from datetime import datetime, timedelta

@dag(
    dag_id = "weather_api_orchestrator",
    description = "",
    start_date = datetime(2025, 1, 1),
    schedule = timedelta(days=1),
    catchup = False,
)
def weather_api_orchestrator():

    @task()
    def api_request():
        pass

    @task()
    def ingest():
        pass

    @task()
    def dbt_run():
        pass

    api_request() >> ingest()

weather_api_orchestrator()