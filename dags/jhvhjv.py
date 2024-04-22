"""
jhvhjv
DAG auto-generated by Astro Cloud IDE.
"""

from airflow.decorators import dag
from astro import sql as aql
from astro.table import Table, Metadata
import pandas as pd
import pendulum


@aql.run_raw_sql(conn_id="duckdb_default", task_id="sql_1", results_format="pandas_dataframe")
def sql_1_func():
    return """
    
    """

@aql.dataframe(task_id="python_1")
def python_1_func():
    return

default_args={
    "owner": "dolece9181@adstam.com,Open in Cloud IDE",
}

@dag(
    default_args=default_args,
    schedule="0 0 * * *",
    start_date=pendulum.from_format("2024-04-22", "YYYY-MM-DD").in_tz("UTC"),
    catchup=False,
    owner_links={
        "dolece9181@adstam.com": "mailto:dolece9181@adstam.com",
        "Open in Cloud IDE": "https://cloud.astronomer.io/clul8ja4c01q201kwopb4u18u/cloud-ide/clul8ntr201t301ivb2a8z64z/clvarsl9w03fp01p4gvv2yd70",
    },
)
def jhvhjv():
    sql_1 = sql_1_func()

    python_1 = python_1_func()

dag_obj = jhvhjv()
