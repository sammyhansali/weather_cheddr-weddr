import os
import json
import requests
from airflow.sdk import dag, task
from datetime import datetime, timedelta
from airflow.providers.amazon.aws.hooks.s3 import S3Hook

# Constants
S3_BUCKET = "weather-cheddr-weddr"

# DAG logic
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
        return locations[:2]
    
    @task
    def get_requests():
        fp = "config/requests.json"
        with open(fp, "r") as f:
            requests = json.load(f)
        return requests[:2]

    @task
    def fetch_response(location, request):
        print(location)
        print(request)

        date = datetime.today().strftime('%Y-%m-%d')
        endpoint = request["endpoint"]
        location_id = str(location["location_id"])

        latitude = location["latitude"]
        longitude = location["longitude"]
        url = request["url"]
        params = request["params"]
        params["latitude"] = latitude
        params["longitude"] = longitude

        try:
            resp = requests.get(url=url, params=params)

            resp.raise_for_status
            if resp.status_code != 200: 
                raise requests.exceptions.HTTPError
            content = json.loads(resp.content)
            return [date, endpoint, location_id, content]

        except requests.exceptions.HTTPError as err:
            print("API request failed. Error details: ", err)

        except Exception as err:
            print("An error occurred. Error details: ", err)
    
    @task
    def load_response_to_s3(response):
        print(response)
        path = f"raw/{response[0]}/{response[1]}/location_id={response[2]}/data.json"
        hook = S3Hook(aws_conn_id="aws_default")
        hook.load_string(
            string_data=json.dumps(response[3]),
            key=path,
            bucket_name=S3_BUCKET,
            replace=True,
        )

    @task
    def ingest_to_snowflake(file_path):
        pass

    # @task()
    # def dbt_run():
    #     pass

    locations = get_locations()
    reqs = get_requests()
    responses = fetch_response.expand(
        request=reqs,
        location=locations,
    )
    load_response_to_s3.expand(
        response=responses,
    )

weather_api_orchestrator()