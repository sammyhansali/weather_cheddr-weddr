import json
from datetime import datetime, timedelta

import requests
from airflow.models import Variable
from airflow.providers.amazon.aws.hooks.s3 import S3Hook
from airflow.providers.snowflake.hooks.snowflake import SnowflakeHook
from airflow.sdk import dag, task
from cosmos import DbtTaskGroup

# Constants
# ENV: either DEV or PROD allowed. set in admin > variables
ENV = Variable.get("env", default_var="DEV")
S3_BUCKET = "weather-cheddr-weddr"
DBT_PROJECT_PATH = "/opt/airflow/dags/dbt/cheddr_weddr"
DBT_PROFILES_PATH = "/opt/airflow/dags/dbt/cheddr_weddr/profiles.yml"
DBT_EXECUTABLE_PATH = "/opt/airflow/dbt_venv/bin/dbt"


def project_config():
    from cosmos import ProjectConfig

    _project_config = ProjectConfig(
        dbt_project_path=DBT_PROJECT_PATH,
        project_name="cheddr_weddr",
    )
    return _project_config


def profile_config():
    from cosmos import ProfileConfig
    from cosmos.profiles import SnowflakeUserPasswordProfileMapping

    _profile_config = ProfileConfig(
        profile_name="cheddr_weddr",
        target_name=ENV,
        profile_mapping=SnowflakeUserPasswordProfileMapping(
            conn_id="snowflake_default",
            profile_args={"database": ENV, "warehouse": "TRANSFORMING", "threads": 8},
        ),
    )
    return _profile_config


def execution_config():
    from cosmos import ExecutionConfig, ExecutionMode

    _execution_config = ExecutionConfig(
        execution_mode=ExecutionMode.WATCHER, dbt_executable_path=DBT_EXECUTABLE_PATH
    )
    return _execution_config


# DAG logic
@dag(
    dag_id="fetch_load_ingest_build",
    description="",
    start_date=datetime(2025, 1, 1),
    schedule=timedelta(days=1),
    catchup=False,
)
def fetch_load_ingest_build():
    @task
    def get_locations():
        fp = "json/locations.json"
        with open(fp) as f:
            locations = json.load(f)
        return locations

    @task
    def get_requests():
        fp = "json/requests.json"
        with open(fp) as f:
            requests = json.load(f)
        return requests

    @task
    def fetch_and_load_to_s3(locations, request):
        print(locations)
        print(request)

        date = datetime.today().strftime("%Y-%m-%d")
        endpoint = request["endpoint"]

        # 12/01/2025 - OpenMeteo API does not support satellite-radiation endpoint for locations in the USA.
        if endpoint == "satellite-radiation":
            locations = [loc for loc in locations if loc["country"] != "US"]

        loc_ids = [loc["location_id"] for loc in locations]

        url = request["url"]
        params = request["params"]
        params["latitude"] = [loc["latitude"] for loc in locations]
        params["longitude"] = [loc["longitude"] for loc in locations]

        try:
            resp = requests.get(url=url, params=params)

            if resp.status_code != 200:
                raise requests.exceptions.HTTPError
            content = json.loads(resp.content)

        except requests.exceptions.HTTPError as err:
            print("API request failed. Error details: ", err)
            raise

        except Exception as err:
            print("An error occurred. Error details: ", err)
            raise

        # print(content)
        key = f"raw/{endpoint}/{date}/data.json"
        data = {
            "date": date,
            "endpoint": endpoint,
            "location_ids": loc_ids,
            "payload": content,
        }
        hook = S3Hook(aws_conn_id="aws_default")
        hook.load_string(
            string_data=json.dumps(data),
            key=key,
            bucket_name=S3_BUCKET,
            replace=True,
        )
        return key

    @task
    def truncate_snowflake_target_tables():
        hook = SnowflakeHook(snowflake_conn_id="snowflake_default")
        for table_name in ["WEATHER", "AIR_QUALITY", "SATELLITE_RADIATION", "FLOOD"]:
            truncate_raw_sql = f"truncate table {table_name};"
            hook.run(truncate_raw_sql)

    @task
    def ingest_from_s3_to_snowflake(s3_key):
        print(s3_key)
        endpoint = s3_key.split("/")[1]
        today = s3_key.split("/")[2]
        table_name = endpoint.upper().replace("-", "_")
        copy_into_raw_sql = f"""
            copy into {table_name} (payload, location_ids, date, load_ts)
            from (
                select 
                    $1:payload,
                    $1:location_ids,
                    $1:date,
                    current_timestamp()
                from @my_s3_stage/{endpoint}/{today}
            )
            on_error = abort_statement
            ;
        """
        hook = SnowflakeHook(snowflake_conn_id="snowflake_default")
        hook.run(copy_into_raw_sql)

    dbt_build = DbtTaskGroup(
        group_id="dbt_build",
        project_config=project_config(),
        profile_config=profile_config(),
        execution_config=execution_config(),
    )

    locations = get_locations()
    reqs = get_requests()
    keys = fetch_and_load_to_s3.partial(locations=locations).expand(request=reqs)
    truncate = truncate_snowflake_target_tables()
    ingest = ingest_from_s3_to_snowflake.expand(s3_key=keys)

    truncate >> ingest >> dbt_build


fetch_load_ingest_build()
