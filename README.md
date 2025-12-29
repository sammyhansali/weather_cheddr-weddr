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
- create a website for this portfolio project
    - see live bi dashboard
    - link to my code
    - detailed explanation with great visuals of what i did
- move compute to a cloud service
- create a deployment environment instead of just a dev environment
- CI / CD (github actions)
- terraform for cloud services
- look into dlthub for ingestion
- duckdb!!! its coming up so often now
- ml model deplyments!

# Roadmap
1. robust data quality / validation layer (DONE)
    - (a) model contracts (done)
    - (b) data tests
    - (c) unit tests
    - try dbt-expectations and dbt-utils for added tests
    - make sure that cosmos-dbt runs dbt build instead of dbt run
    - dev / prod split
2. ci/cd
    - github actions
        - lint SQL and python and YAML
        - run dbt parse and dbt compile
        - build images on main 
    - pre-commit hooks locally
3. cloud deployment
    - docker containers pushed to ECR and ran in ECS
    - superset in ECS + fargate
    - airflow can be tried in MWAA
4. terraform for reproducible cloud
    - write infra as code for all aws services used
    - maybe have seperate dev/prod envs
5. lakehouse/alternatives
    - try duckdb locally
    - try apache iceberge on s3
6. ml model deployments




uv run --env-file ../../.env dbt run