# Semaine 2 2048
## Présentation du projet
L'objectif de notre projet est de coder, via le module pygame, un *clone* du célèbre __jeu flappy bird.__ Nous utiliserons la __programmation orientée objet__ pour mener à bien ce projet et obtenir un code final __propre__ et bien __structuré__.

## Guide d'installation
#### Pour accéder à notre jeu et y jouer, il faut suivre les instructions suivantes:
* Cloner le dépôt dans votre explorateur de fichier à l'aide de la commande bash: git clone https://gitlab-cw1.centralesupelec.fr/thomas.banzet/projet-2048-cw.git
* Ouvrir le fichier game_loop.py dans votre éditeur de code, puis executez le. Une fenêtre pygame devrait s'ouvrir, et vous vous retrouverez alors dans le menu de démarrage du jeu. C'est fait, le jeu est lancé et vous pouvez vous amuser !

## Les différents Jalons à atteindre
###### Voici les Jalons de notre projet :
1. Recherche et modification des différentes images permettant l'affichage des éléments du jeu
2. La création d'une première fenêtre de jeu (affichant seulement un ecran noir) que l'on peut fermer au clic, avant de bien assimiler la gestion des événements avec pygame
3. Création des différentes classes bird et pipe pour gérer les événements du jeu avec les différentes méthodes d'affichage et de déplacement (gravité, vitesse des tuyaux...)
4. Mise en place du système de collisions pour détecter la défaite du joueur
5. Création d'une première boucle de jeu fonctionnelle, où le jeu se ferme à chaque défaite du jeu et se lance directement à l'ouverture de la fenêtre 
6. Création des différents menus de début et de fin de partie pour avoir une boucle de jeu stable
7. Implémentation de la fonctionnalité permettant le décompte et l'affichage du score, puis de la gestion du score max
8. Ajouts de différents éléments esthétiques dans le jeu pour permettre à l'utilisateur d'avoir un choix libre, et permettre la gestion de ces différents éléments via le menu de début de partie
9. Création de différents "power-up" permettant de rendre le jeu plus amusant, permettant de jouer des parties où l'inversion de la gravité
10. Implémentation de ces ajouts dans le jeu, sous forme d'objets apparaissant de manière aléatoire

## L'avancement final du projet
Au cours de cette semaine de travail, nous avons réaliser complètement les __Jalons 1,2,3,4,5,6,7,8.__ Nous avons pu commencer le travail sur les jalons 9 et 10, mais *nous n'avons pas eu le temps* de les terminer complétement.

## Comment le projet est-il structuré ?
#### La programmation orientée objet nous a permis d'obtenir un code clair et bien structuré. Le découpage en plusieurs fichiers python nous a également été utile pour alléger le code. Ainsi, vous trouverez différents fichiers python qui ont chacun une fonctionnalité bien spécifique:
* Le fichier game_loop.py abrite la classe Game, en appellant la méthode run d'une instance de cette classe, le jeu se lance
* Les différents fichiers pipe.py, ground.py, bird.py contiennent les classes permettant de définir les différents éléments du jeu.Toute l'importance de la Programmation Orientée Objet s'illustre parfaitement dans la gestion des tuyaux. En effet, les tuyaux à faire apparaître possèdent tous des caractéristiques communes, et seul l'écart entre les tuyaux et leur taille varie.
* Les autres fichiers python offrent à l'utilisateur une expérience plus immersive et dynamique, avec nottament les menus de début et de fin de partie mais aussi la gestion du score !
* Enfin, les autres fichiers regroupent les ressources graphiques qui ont permis la bonne réalisation du jeu, avec nottament les images de fond, des oiseaux ou encore des tuyaux !
