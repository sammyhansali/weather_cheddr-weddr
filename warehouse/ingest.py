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
        session_parameters={
            "QUERY_TAG": "ide"
        },
    )
    return conn

def ingest_setup():
    conn = create_conn()
    try:
        with open('warehouse/ingest_setup.sql', 'r') as f:
            for cur in conn.execute_stream(f):
                print(cur)
    finally:
        conn.close()

def ingest_payload():
    fp = pathlib.Path("test_data/payload.json")
    with open(fp, "r") as f:
        payload = json.load(f)
    params = json.dumps(payload)

    conn = create_conn()
    try:
        cs = conn.cursor()
        cs.execute("use database RAW;")
        cs.execute("use schema CHEDDR_WEDDR;")
        cs.execute("use warehouse LOADING;")
        cs.execute("""
            insert into HISTORICAL_WEATHER (payload)
            select parse_json(%s);
        """, params)
    finally:
        cs.close()
        conn.close()