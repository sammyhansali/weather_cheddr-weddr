FROM apache/airflow:3.1.3

USER root

# bake airflow and dbt data into the image for ease of use
COPY ./airflow/dags/   /opt/airflow/dags/
COPY ./airflow/common/ /opt/airflow/common/
COPY ./airflow/config/ /opt/airflow/config/
COPY ./airflow/json/   /opt/airflow/json/
COPY ./dbt/            /opt/airflow/dags/dbt/

# install dbt into a virtual environment to avoid dependency clashes
RUN python -m venv dbt_venv && source dbt_venv/bin/activate && \
    pip install --no-cache-dir dbt-snowflake==1.11.0 dbt-core==1.11.2 && deactivate

USER airflow
RUN pip install "astronomer-cosmos==1.11.3"
