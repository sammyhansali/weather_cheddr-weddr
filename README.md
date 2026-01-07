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
2. ci/cd, first pass through (DONE)
    - github actions
        - lint SQL and python and YAML
        - run dbt parse and dbt compile
        - build images on main 
    - pre-commit hooks locally (decided not to do this, unnecessary bloat)
3. cloud deployment, rough order of operations (WIP)
    - reworking dockerfile and docker compose so that images/containers will be easier to port over to aws ECS, in terms of structure.
    - continuing off the last note, break up airflow into different components. webserver, scheduler, etc. they will use the same image though. this structure is better suited to a prod environment. where each component can be elastically scaled up or down depending on usage and need.
    - mentally (for now) seperate the airflow services into three different buckets: metadata, run-once, and always-running. 
        - metadata: these services include redis (for superset and/or airflow), postgres metadatabases (for superset and airflow), and anything else that is metadata related.
        - run-once: these services need to be run once per code update, to achieve some sort of initialization task, and not run again. Examples include the init containers (superset-init and airflow-init).
        - always-running: these services are always running (when you want to use the app). This includes all of the core containers responsible for keeping superset and airflow up and running. For airflow, this includes services like the webserver, scheduler, and triggerer.
    - how we will partition these different services on AWS.
        - metadata -> RDS or ElastiCache, depending on the type of metadata
        - run-once and always-running -> both will be on ECS (maybe ECR for some of them), but their rules on how / when they are run will be different.
    - docker images pushed to ECR (Elastic Container Registry). I think that I also have the option of pushing my images to a public docker image repository, like GHCR. Maybe it would be good practice to do both?
    - secrets set up in aws, so no need for .env files and more security.
    - setup automated dockerfile pushes in CI/CD, so that prod always has the latest updates.
    - start with AWS Fargate, so that the infra management complexity on my end is low. once things are humming along and I have a better understand of ECS, I can switch to EC2. Start managing my own VMs and learn how to predict usage for different services.
    ### NEXT STEP: Break up airflow into smaller chunks (webserver, scheduler, etc).

4. terraform for reproducible cloud
    - write infra as code for all aws services used
    - maybe have seperate dev/prod envs
5. lakehouse/alternatives
    - try duckdb locally
    - try apache iceberge on s3
6. ml model deployments




uv run --env-file ../../.env dbt run 
