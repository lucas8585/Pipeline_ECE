Le but de ce projet est d'avant tout de récupérer et préparer les données disponible. 
 Nous sommes donc passé par plusieurs étapes : 
 La premiere était de récupérer un jeu de donnée, nous avons donc choisit les élections régionales de 2010 en fichier csv, car le csv est très utilisé et facilement maniable.
 Une fois ce jeu de donnée récupérer nous avons décider de le faire passer avec un flux Nifi et le lire dans un topic Kafka. On a donc en premier lieu créer un topic Kafka avec la commande suivante : 
 
bin/kafka-topics.sh --create --topic Elections --create --partition 3 --replication-factor 1 bootstrap-server localhost:9092
 
![Topic](https://user-images.githubusercontent.com/94440244/146551412-c9d8c29f-ebae-48db-8fa3-a91e04b28e16.png)

Apres avoir créer ce topic nous devions faire le lien entre nifi et nifi registry pour pouvoir versionner le flux vers ce repo github par la suite. 
Pour cela on a lancés nifi et nifi registry avec les commandes suivantes : 

![nifi connect](https://user-images.githubusercontent.com/94440244/146552529-c62eef8e-4022-46fc-b617-37360ea78af3.png)

Après avoir démarré nifi et nifi registry on devait créer un bucket avec nifi registry et connecter nifi dans le bucket créé.
