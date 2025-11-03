import os
from dotenv import dotenv_values

import snowflake.connector

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

conn.cursor().execute("create database test;")