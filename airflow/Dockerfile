FROM apache/airflow:3.1.3

USER root

# install dbt into a virtual environment to avoid dependency clashes
RUN python -m venv dbt_venv && source dbt_venv/bin/activate && \
    pip install --no-cache-dir dbt-snowflake && deactivate

USER airflow
RUN pip install "astronomer-cosmos"
