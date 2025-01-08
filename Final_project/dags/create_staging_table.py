from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator

from py.MySQL import create_staging


with DAG(
    dag_id="create_staging",
    start_date=datetime(2025, 1, 1),
    catchup=False,
    schedule_interval=None,
    tags=["staging"],
) as dag:

    msql_mart = PythonOperator(
        task_id="create_staging_table",
        python_callable=create_staging
    )

create_staging_table
