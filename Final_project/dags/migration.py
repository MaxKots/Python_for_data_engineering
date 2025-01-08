from datetime import datetime

from airflow import DAG
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.operators.python import PythonOperator

from py.migration import postgres_migration, mysql_migration

with DAG(
    dag_id="init_and_migrate_tables",
    start_date=datetime(2025, 1, 1),
    schedule_interval=None,
    catchup=False,
    tags=["migration"],
) as dag:

    postres_migrate = PythonOperator(
        task_id="postgres_migration",
        python_callable=postgres_migration
    )

    msql_migrate = PythonOperator(
        task_id="mysql_migration",
        python_callable=mysql_migration
    )

postgres_migration >> mysql_migration
