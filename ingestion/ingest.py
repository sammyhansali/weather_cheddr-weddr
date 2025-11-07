import os
import json
import pathlib
from dotenv import dotenv_values

import snowflake.connector

def create_conn():
    config = dotenv_values(".env")
    conn = snowflake.connector.connect(
        user=config["SNOWFLAKE_USER"],
        password=config["SNOWFLAKE_PASSWORD"],
        account=config["SNOWFLAKE_ACCOUNT"],
    )
    return conn

def ingest_setup():
    conn = create_conn()
    try:
        with open('ingestion/setup_ingestion_tables.sql', 'r') as f:
            for cur in conn.execute_stream(f):
                print(cur)
    finally:
        conn.close()

def ingest():
    dir = os.listdir("test_data/")

    conn = create_conn()
    try:
        cs = conn.cursor()
        cs.execute("use database RAW;")
        cs.execute("use schema CHEDDR_WEDDR;")
        cs.execute("use warehouse LOADING;")

        for fp in dir:
            location_id, date, endpoint = fp.split("-")
            endpoint = endpoint.replace(".json", "").upper()
            with open(os.path.join("test_data/",fp), "r") as f:
                payload = json.load(f)
            params = json.dumps(payload)
            
            query = f"""
                insert into {endpoint} (payload, location_id, date, load_ts)
                select 
                    parse_json(%s),
                    {location_id},
                    {date},
                    current_timestamp(),
                ;
            """
            cs.execute(query, params)
    finally:
        cs.close()
        conn.close()