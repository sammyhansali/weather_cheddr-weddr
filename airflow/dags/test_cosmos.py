import os
from datetime import datetime
from cosmos import DbtDag, ProjectConfig, ProfileConfig, ExecutionConfig
from cosmos.profiles import SnowflakeUserPasswordProfileMapping

DBT_PROJECT_PATH = "/opt/airflow/dags/dbt/cheddr_weddr"

# _project_config = ProjectConfig()
# _profile_config = ProfileConfig()
# _execution_config = ExecutionConfig()


# test_cosmos_dag = DbtDag(
#     dag_id="test_cosmos_dag",
#     schedule="@daily",
#     start_date=datetime(2025,1,1),
#     catchup=False,
#     max_active_tasks=1,
    
#     project_config=_project_config,
#     profile_config=_profile_config,
#     execution_config=_execution_config,
# )