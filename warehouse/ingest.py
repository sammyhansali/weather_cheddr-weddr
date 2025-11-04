import json
import pathlib
from dotenv import dotenv_values

import snowflake.connector

def ingest_payload():
    fp = pathlib.Path("C:/Users/sammy/projects/portfolio/weather_cheddr-weddr/test_data/payload.json")
    with open(fp, "r") as f:
        payload = json.load(f)

    config = dotenv_values(".env")
    conn = snowflake.connector.connect(
        user=config["SNOWFLAKE_USER"],
        password=config["SNOWFLAKE_PASSWORD"],
        account=config["SNOWFLAKE_ACCOUNT"],
        warehouse=config["SNOWFLAKE_WAREHOUSE"],
        database=config["SNOWFLAKE_DATABASE"],
        schema=config["SNOWFLAKE_SCHEMA"],
        session_parameters={
            "QUERY_TAG": "weather"
        },
    )

    cs = conn.cursor()
    cs.execute("""
        insert into RAW_CAMBRIDGE_FORECAST (payload)
        select parse_json(%s)
    """, params=json.dumps(payload))

    cs.close()
    conn.close()