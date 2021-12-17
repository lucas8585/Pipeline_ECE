from pyspark.sql import SparkSession

from pyspark.sql.types import IntegerType

from pyspark.ml.feature import StringIndexer

from datetime import datetime, timedelta

from airflow import DAG

from airflow.operators.bash_operator import BashOperator

from airflow.operators.dummy import DummyOperator

from airflow.operators.python_operator import PythonOperator

from airflow.utils.dates import days_ago

import pandas as pd

 

default_args = {

    'owner' : 'airflow',

    'start_date' : datetime(2021, 12, 17)

}

 

def myFunction():

    df = pd.read_csv('df3.csv')

    df.to_parquet('elections2022.parquet')

 

with DAG(

    dag_id = 'pipeline',

    default_args = default_args,

    description = 'project',

    schedule_interval = None,

) as dag:

 

    task_1 = BashOperator(

     task_id = 'extract_csv',

     bash_command = '/Users/mugeozdin/Desktop/projet/df3.csv',

    )

 

    task_2 = PythonOperator(

     task_id = 'transformer_parquet',

     python_callable = myFunction,

    )

 

task_1.set_downstream(task_2)