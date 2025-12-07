# Data definitions

- RAW: weather api data directly ingested into snowflake
- SRC: raw data that was processed from json to a real table
- STG: src data with modifications and materialized as view
- INT: (optional) acts as intermediate between stg views and marts tables
- MARTS
    - FCT - fact table
    - DIM - dimension table

# Other resources
- How to setup snowflake for dbt best practices: https://www.getdbt.com/blog/how-we-configure-snowflake

# General plan

what will the app do when fully orchestrated and built out:

every day at midnight, for location in locations, it will:
- fetch forecast data for the next day
    - types of forecast data: (1) weather, (2) air quality, (3) satellite radiation, (4) flood
- update the respective tables with new data
- update the BI models

PK for fact tables: location_id, ts, field

# Ideas
- more dbt tests (constraints/schema tests, biz logic tests, unit tests)
- great expectations tests
- once metabase good, swap it out for superset
- create a website for this portfolio project
    - see live bi dashboard
    - link to my code
    - detailed explanation with great visuals of what i did
- move compute to a cloud service
- CI / CD (github actions)
- terraform for cloud services
- look into dlthub for ingestion
- duckdb!!! its coming up so often now