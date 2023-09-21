# Le projet 

## Membres :

+ Ambroise Adams
+ Paul Cislini
+ Clément Szewczyk

## les fichiers

+ card_deck.py : fichier obligatoire
+ combinaison.py : fichier obligatoire
+ couleur.py : fichier contenat notre fonction pour la couleur pour faire nos test
+ fonction.py : fichier contenant notre classe avec toutes les fonctions qui permettent de chercher les combinaisons 
+ Poker Python.pdf : Fichier que l'on a du rendre en classe
+ main.py : Fichier principal (à lancer pour avoir le résultat d'une main aléatoire)
+ mainpoker.py : Fichier contenant des exemples de mains pour faires des tests.
+ repetition.py : Fichier contenant notre fonction pour trouver les répétition (pour nos test)
+ suite.py : Fichier contenant notre fonction pour trouver la suite (pour nos test)
+ test_card_deck.py : Fichier exemple
+ test2.py : Fichier de test des combinaisonsa
+ affichage_couleur : Fichier de test pour afficher la couleur


# Fonctionnement du code : 

Dans le fichier fonction.py, nous avons une classe "test_combinaison" qui permet de regrouper les fonctions de recherches de combinaison. 

Dnas le fichier main.py, nous appellons notre classe ainsi que les classe pour créer nos carte. Nous appelons aussi la librairie Collections pour utiliser la fonction "Counter". 

Pour avoir le résultat, nous avon une fonction principale stocké dans fonction.py du nom de "resolution". 

Pour afficher le résultat d'une main aléatoire (fichier main.py) générer avec la fichier card_deck. 
on "print" la fonction resolution avec en paramêtre la main. 

Avec fichier test2.py, quand vous exécuté le programme, cela lance un boucle infini qui demande qu'elle main on veut tester. Voici ce que vous pouvez mettre pour avoire un résulat,
+ rien
+ paire
+ brelan
+ 2paire
+ suite
+ couleur
+ carre
+ full
+ flush
+ manuel

Si vous voulez remplire vos propre valeur, vous pouvez utiliser la main manuel pour pouvoir remplire vos propre valeur: 