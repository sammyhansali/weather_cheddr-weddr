import json
from airflow.sdk import dag, task
from datetime import datetime, timedelta

from common.endpoint_params import weather


@dag(
    dag_id = "weather_api_orchestrator",
    description = "",
    start_date = datetime(2025, 1, 1),
    schedule = timedelta(days=1),
    catchup = False,
)
def weather_api_orchestrator():

    @task
    def get_locations():
        fp = "config/locations.json"
        with open(fp, "r") as f:
            locations = json.load(f)
        return locations
    
    @task
    def get_endpoints():
        fp = "config/endpoints.json"
        with open(fp, "r") as f:
            endpoints = json.load(f)
        return endpoints

    @task
    def fetch_endpoint(location, endpoint):
        print(location)
        print(endpoint)

    @task
    def ingest_to_snowflake(file_path):
        pass

    # @task()
    # def dbt_run():
    #     pass

    locations = get_locations()
    endpoints = get_endpoints()
    fetch_tasks = fetch_endpoint.expand(
        endpoint=endpoints,
        location=locations,
    )
    ingest_to_snowflake.expand(
        file_path=fetch_tasks,
    )

weather_api_orchestrator()