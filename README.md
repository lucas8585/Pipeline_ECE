Le but de ce projet est avant tout de récupérer et préparer les données disponibles pour un cabinet de conseil en stratégie politique.
 Nous sommes donc passé par plusieurs étapes : 
 La premiere était de récupérer un jeu de donnée, nous avons donc choisit les élections régionales de 2010 en fichier csv, car le csv est très utilisé et facilement maniable.
 Une fois la donnée collectée nous avons décidé de le faire passer avec un flux Nifi et le lire dans un topic Kafka. On a donc en premier lieu téléchargé kafka avec ce lien https://www.apache.org/dyn/closer.cgi?path=/kafka/3.0.0/kafka_2.13-3.0.0.tgz . 
 
Puis on l'a installé avec les commandes suivantes : 

tar -xzf kafka_2.13-3.0.0.tgz

cd kafka_2.13-3.0.0.tgz

On a ensuite lancer zookeeper : 

![zookeeper](https://user-images.githubusercontent.com/94440244/146580037-d62da2af-8847-4e37-9b5e-bfbc99b08182.png)

Puis kafka :

![kafka](https://user-images.githubusercontent.com/94440244/146580068-c9bb63ba-c424-4afb-abe0-df53530da94f.png)

A la suite de cela nous avons crée un topic Kafka avec la commande suivante : 
 
bin/kafka-topics.sh --create --topic Elections --create --partition 3 --replication-factor 1 bootstrap-server localhost:9092
 
![Topic](https://user-images.githubusercontent.com/94440244/146551412-c9d8c29f-ebae-48db-8fa3-a91e04b28e16.png)

Apres avoir créé ce topic, nous devions faire le lien entre nifi et nifi registry afin de versionner le flux vers un repo github par la suite. 
Pour cela, on a lancé nifi et nifi registry avec les commandes ci-contre : 

![nifi connect](https://user-images.githubusercontent.com/94440244/146552529-c62eef8e-4022-46fc-b617-37360ea78af3.png)

Après avoir démarré nifi et nifi registry on devait créer un bucket avec nifi registry et connecter nifi grâce au registryclient (ici en l'occurence on est sur le port par défaut de nifi registry localhost:18080).

![bucket](https://user-images.githubusercontent.com/94440244/146553199-5dac1549-056c-4d71-81e3-1567bee64925.png)





![registryclient](https://user-images.githubusercontent.com/94440244/146553167-2d66f29a-77ec-4272-ac62-463b2bf445f1.png)

A la suite de cela, on devait versionner le flux nifi sur github, pour se faire on a crée le repo et récupéré le token. 
Dans le terminal, nous avons effectué la commande : git clone https://github.com/lucas8585/Pipeline_ECE.git

Lorsque le repo a été cloné nous avons accédé aux fichiers providers.xml de nifi registry et ajouté le token et les données suivantes : 

![provider](https://user-images.githubusercontent.com/94440244/146554725-3f93a24a-07b9-4f3a-b7fe-f69f453f19b6.png)

Le repo github à présent versionné à Nifi on devait créer un flux. Nous avons donc établis cette template ci-dessous : 

![template](https://user-images.githubusercontent.com/94440244/146555337-15b4e902-4ad7-44db-b960-8e45bc008cf5.png)
![config1](https://user-images.githubusercontent.com/94440244/146555938-f5a73c42-a5ba-419c-869f-f5c55080d184.png)
![config2](https://user-images.githubusercontent.com/94440244/146556112-a54deb30-a033-4430-840d-0c409df783fc.png)
![config3](https://user-images.githubusercontent.com/94440244/146555943-7c0c8cc5-fccb-4076-ac2d-5e8628223a92.png)

Cependant on a constaté que le fichier csv était trop lourd et ne pouvait donc pas être traiter dans le topic kafka. (même en changeant la capacité maximum, la max request size était a 1MB de base) 

![error](https://user-images.githubusercontent.com/94440244/146556387-1456db68-286e-4402-9d02-c67495c97a98.png)

![taille](https://user-images.githubusercontent.com/94440244/146583700-1fde1c5f-9a6e-4a19-92ee-0a0a0f2cfc69.png)

Selon nous, si le fichier était trop lourd on devait donc faire en sorte de le réduire au maximum. Pour cela nous avons utilisé pyspark afin de traiter la donnée.

Comment évaluer la pertinence des données ? 

En l'occurence un cabinet de conseil en stratégie politique à besoin surtout des chiffres clés ; des résultats de vote, le pourcentage d'absentéisme... On a donc enlevé les colonnes qui ne nous semblait pas pertinentes, car il y avait beaucoup de texte. 
On a également retiré les données Null ainsi que les redondances. 

Une fois le fichier traité nous devions l'orchestrer, pour cela on a lancé airflow avec la commande suivante : airflow standalone

<img width="1263" alt="airflow" src="https://user-images.githubusercontent.com/94440244/146565217-531ed911-17f0-45a0-a1bc-431a97361e9b.png">

Lorsque le mot de passe a été généré on a pu se connecter avec Airflow

<img width="1266" alt="localhost" src="https://user-images.githubusercontent.com/94440244/146565205-09150d89-13f6-4633-855f-9786efb17c47.png">

L'objectif étant de transformer le csv en .parquet afin de faciliter davantage le traitement. Car le .parquet permet le stockage de fichier volumineux mais pas seulement. L'avantage du .parquet c'est aussi de réduire le temps de lecture, mais surtout elle permet une capacité d'évolution ce qui n'est clairement pas négligeable pour le client. 
En effet, il arrive fréquemment qu'une source de donnée soit changeante, en particulier les données politiques. Il faut donc permettre une évolution du shéma. 

Une fois que les données ont été rendues significatives, elles sont donc prêtes à être exploitées. 
