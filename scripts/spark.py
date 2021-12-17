#lancer pyspark avec la commande 

./bin/pyspark


from pyspark.sql.session import SparkSession
from pyspark.context import SparkContext
import pandas as pd

sc=SparkContext.getOrCreate()
spark=SparkSession(sc)

df= spark.read.option("header", "True").option("delimiter", ";").option('inferSchema','True').csv('/Users/mugeozdin/Desktop/projet/elections.csv')

df.printSchema()
df.show()

df1=df.drop('Code du département', 'Nuance Liste', 'Libellé Etendu Liste')
df1.show()

#On a décidé de supprimer ses colonnes car elle ne nous semblait pas pertinente.


#enlever les valeurs null


df2=df1.dropna()

df2.show()


#supprimer les redondances 

df3= df2.dropDuplicates()

df3.show()



df3.write.csv('/home/')

