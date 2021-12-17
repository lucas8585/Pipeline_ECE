Pour installer Spark il faut télécharger la dernière version sur le site https://spark.apache.org/downloads.html puis lancer l'extraction avec la commande :

tar -xvf spark-3.1.2-bin-hadoop3.2.tgz


Renommer le fichier extrait par spark avec la commande suivante :

mv spark-3.1.2-bin-hadoop3.2.tgz spark



Supprimer l'archive extrait précédemment avec la commande :

rm spark-3.1.2-bin-hadoop3.2.tgz


Vérifier si spark fonctionne avec la commande suivante pour lancer spark-shell :

./spark/bin/spark-shell

![sparkshell](https://user-images.githubusercontent.com/94440244/146572102-bcbcecb9-eb72-4a92-a7bb-ab650ff8eb82.png)

Vérifier si spark fonctionne avec la commande suivante pour lancer pyspark :

./spark/bin/pyspark 


![pyspark](https://user-images.githubusercontent.com/94440244/146572115-535829fb-a6c3-4072-9557-645f436e7da9.png)
