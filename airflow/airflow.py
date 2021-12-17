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

 #On a crée un dag qui va nous permettre d'executer des tâches 

with DAG(

    dag_id = 'pipeline',

    default_args = default_args,

    description = 'project',

    schedule_interval = None,

) as dag:

 # Ici on a crée le dag et on va ensuite lui attribuer des tâches, ici en l'ocurrence on a décider de faire un ETL (Extract, Transform, Load)
  # en tâche 1 on va récuperer la donnée précédemment traiter avec pyspark 
  # en tâche 2 on va transformer cette donnée en parquet afin de la charger par la suite 

    task_1 = BashOperator(

     task_id = 'extract_csv',

     bash_command = '/Users/mugeozdin/Desktop/projet/df3.csv',

    )

 

    task_2 = PythonOperator(

     task_id = 'transformer_parquet',

     python_callable = myFunction,

    )

 
# le .set_downstream nous permet ici de donner l'orde à laquel les tâches vont fonctionner. Par exemple ici la task_1 va s'executer 
# et quand elle aura fini cela lancera l'éxecution de la task_2 on peut aussi remplacer le .set_downstream par >>
task_1.set_downstream(task_2)

#Malheureusement, on a eu un soucis avec airflow qui n'a pas afficher notre dag, on ne pouvait donc pas obtenir notre fichier résultat en .parquet
