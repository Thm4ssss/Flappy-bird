# Projet CodingWeeks 2048: Codage d'un clone de Flappy Bird
## Présentation du projet
L'objectif de notre projet est de coder, via le module pygame, un *clone* du célèbre __jeu flappy bird.__ Nous utiliserons la __programmation orientée objet__ pour mener à bien ce projet et obtenir un code final __propre__ et bien __structuré__.

## Guide d'installation
#### Pour accéder à notre jeu et y jouer, il faut suivre les instructions suivantes:
* Cloner le dépôt dans votre explorateur de fichier à l'aide de la commande bash: git clone https://gitlab-cw1.centralesupelec.fr/thomas.banzet/projet-2048-cw.git
* __Installer les bibliothèques__ nécessaires pour le fonctionnement du jeu. Pour cela, tapez la commande bash : *pip install -r requirements.txt*. Il se peut que celle-ci __renvoie une erreur__ si pip n'est pas reconnu en tant que variable d'environnement. Dans ce cas, tapez: *py-m pip install -r requirements.txt*
* Ouvrir le fichier __game_loop.py__ dans votre éditeur de code, puis __executez le__. Une fenêtre pygame devrait s'ouvrir, et vous vous retrouverez alors dans le menu de démarrage du jeu. C'est fait, le jeu est lancé et *vous pouvez vous amuser !*

## Les différents Jalons à atteindre
#### Voici les Jalons de notre projet :
1. Recherche et modification des différentes __images__ permettant l'affichage des éléments du jeu
2. La création d'une __première fenêtre de jeu__ (affichant seulement un ecran noir) que l'on peut *fermer au clic*, avant de bien assimiler la gestion des événements avec pygame
3. Création des différentes __classes bird__ et __pipe__ pour gérer les événements du jeu avec les *différentes méthodes d'affichage* et de *déplacement* (gravité, vitesse des tuyaux...)
4. Mise en place du __système de collisions__ pour détecter la *défaite du joueur*
5. Création d'une __première boucle de jeu fonctionnelle__, où le jeu se *ferme à chaque défaite* du jeu et se *lance directement* à l'ouverture de la fenêtre 
6. Création des différents __menus de début__ et de __fin de partie__ pour avoir une boucle de jeu *stable*
7. Implémentation de la fonctionnalité permettant le __décompte et l'affichage du score__, puis de la gestion du __score max__
8. Ajouts de différents __éléments esthétiques__ dans le jeu pour permettre à l'utilisateur d'avoir __un choix libre__, et permettre la gestion de ces différents éléments *via le menu de début de partie*
9. Création de différents __"power-up"__ permettant de rendre le jeu *plus amusant*, permettant de jouer des parties où la gravité est inversée
10. __Implémentation__ de ces ajouts dans le jeu, sous forme __d'objets__ apparaissant de *manière aléatoire*

## L'avancement final du projet
Au cours de cette semaine de travail, nous avons réaliser complètement les __Jalons 1,2,3,4,5,6,7,8.__ Nous avons pu commencer le travail sur les jalons 9 et 10, mais *nous n'avons pas eu le temps* de les terminer complétement.

## Comment le projet est-il structuré ?
##### La programmation orientée objet nous a permis d'obtenir un code clair et bien structuré. Le découpage en plusieurs fichiers python nous a également été utile pour alléger le code. Ainsi, vous trouverez différents fichiers python qui ont chacun une fonctionnalité bien spécifique:
* Le fichier __game_loop.py__ abrite la classe Game, en appellant la méthode run d'une instance de cette classe, le jeu se lance
* Les différents fichiers pipe.py, ground.py, bird.py contiennent les classes permettant de définir les différents éléments du jeu.Toute l'importance de la Programmation Orientée Objet s'illustre parfaitement dans la gestion des tuyaux. En effet, les tuyaux à faire apparaître possèdent tous des caractéristiques communes, et seul l'écart entre les tuyaux et leur taille varie. La création d'une classe tuyaux simplifie donc grandement leur création
* Les autres fichiers python offrent à l'utilisateur une expérience plus immersive et dynamique, avec nottament les __menus de début et de fin de partie__ mais aussi la __gestion du score__ !
* Enfin, les autres fichiers regroupent les ressources graphiques qui ont permis la bonne réalisation du jeu, avec nottament les __images de fond__, __des oiseaux__ ou encore des __tuyaux__ !
