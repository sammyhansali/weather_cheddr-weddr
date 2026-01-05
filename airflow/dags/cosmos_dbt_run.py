from datetime import datetime

from airflow.models import Variable
from cosmos import DbtDag

ENV = Variable.get("env", default_var="DEV")
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


cosmos_dbt_run = DbtDag(
    dag_id="cosmos_dbt_run",
    schedule="@daily",
    start_date=datetime(2025, 1, 1),
    catchup=False,
    # max_active_tasks=1,
    project_config=project_config(),
    profile_config=profile_config(),
    execution_config=execution_config(),
)
