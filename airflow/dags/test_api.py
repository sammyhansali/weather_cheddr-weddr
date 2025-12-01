import json
import requests
from airflow.sdk import dag, task
from datetime import datetime, timedelta
from airflow.providers.amazon.aws.hooks.s3 import S3Hook
from airflow.providers.snowflake.hooks.snowflake import SnowflakeHook

# Constants
S3_BUCKET = "weather-cheddr-weddr"

# DAG logic
@dag(
    dag_id = "test_api",
    description = "",
    start_date = datetime(2025, 1, 1),
    schedule = timedelta(days=1),
    catchup = False,
)
def test_api():

    @task
    def get_locations():
        fp = "config/locations.json"
        with open(fp, "r") as f:
            locations = json.load(f)
        return locations
    
    @task
    def get_requests():
        fp = "config/requests.json"
        with open(fp, "r") as f:
            requests = json.load(f)
        return requests

    @task
    def fetch_and_load_to_s3(locations, request):
        print(locations)
        print(request)
    
        date = datetime.today().strftime('%Y-%m-%d')
        endpoint = request["endpoint"]

        # 12/01/2025 - OpenMeteo API does not support satellite-radiation endpoint for locations in the USA.
        if endpoint == "satellite-radiation":
            locations = [loc for loc in locations if loc['country'] != 'US']
        
        loc_ids = [loc['location_id'] for loc in locations]

        url = request["url"]
        params = request["params"]
        params["latitude"] = [loc['latitude'] for loc in locations]
        params["longitude"] = [loc['longitude'] for loc in locations]

        try:
            resp = requests.get(url=url, params=params)

            resp.raise_for_status
            if resp.status_code != 200: 
                raise requests.exceptions.HTTPError
            content = json.loads(resp.content)

        except requests.exceptions.HTTPError as err:
            print("API request failed. Error details: ", err)
            raise

        except Exception as err:
            print("An error occurred. Error details: ", err)
            raise

        print(content)
        return None

    locations = get_locations()
    reqs = get_requests()
    keys = fetch_and_load_to_s3.partial(
        locations=locations
    ).expand(
        request=reqs
    )

test_api()