Le but de ce projet est d'avant tout de récupérer et préparer les données disponible. 
 Nous sommes donc passé par plusieurs étapes : 
 La premiere était de récupérer un jeu de donnée, nous avons donc choisit les élections régionales de 2010 en fichier csv, car le csv est très utilisé et facilement maniable.
 Une fois ce jeu de donnée récupérer nous avons décider de le faire passer avec un flux Nifi et le lire dans un topic Kafka. On a donc en premier lieu créer un topic Kafka avec la commande suivante : 
 
bin/kafka-topics.sh --create --topic Elections --create --partition 3 --replication-factor 1 bootstrap-server localhost:9092
 
![Topic](https://user-images.githubusercontent.com/94440244/146551412-c9d8c29f-ebae-48db-8fa3-a91e04b28e16.png)

Apres avoir créer ce topic nous devions faire le lien entre nifi et nifi registry pour pouvoir versionner le flux vers ce repo github par la suite. 
Pour cela on a lancés nifi et nifi registry avec les commandes suivantes : 

![nifi connect](https://user-images.githubusercontent.com/94440244/146552529-c62eef8e-4022-46fc-b617-37360ea78af3.png)

Après avoir démarré nifi et nifi registry on devait créer un bucket avec nifi registry et connecter nifi grâce au registryclient (ici en l'occurence on est sur le port par défaut de nifi registry localhost:18080).

![bucket](https://user-images.githubusercontent.com/94440244/146553199-5dac1549-056c-4d71-81e3-1567bee64925.png)
![registryclient](https://user-images.githubusercontent.com/94440244/146553167-2d66f29a-77ec-4272-ac62-463b2bf445f1.png)

A la suite de cela, on devait versionner le flux nifi sur github, pour se faire on a créer le repo et recuperer le token. 
Dans le terminal, nous avons effectué la commande : git clone https://github.com/lucas8585/Pipeline_ECE.git

Lorsque le repo a été cloner nous avons accédé aux fichiers providers.xml de nifi registry et ajouter le token et les données suivantes : 

