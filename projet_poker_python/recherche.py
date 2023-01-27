import enum
import sys
from collections import Counter

# Fichier de la classe
from card_deck import *
from fonction import *


# Main définie par la classe
# Génération d'un deck
c= Combinaison()

d= Deck()
print(d)

# Nombre de carte :
X = 7 

# Génération main
main = [d.pop() for _ in range(X)]

# affiche d'une main
print ("main")
print (main)

# Trie de la main
main.sort()
print('main triée')
print (main)


# Main manuel 

c1 = Card(Value.DEUX, Color.P)
c2 = Card(Value.SIX, Color.P)
c3 = Card(Value.NEUF, Color.P)
c4 = Card(Value.HUIT, Color.P)
c5 = Card(Value.DIX, Color.P)
c6 = Card(Value.CINQ, Color.K)
c7 = Card(Value.SIX, Color.K)

main2 = [c1, c2, c3, c4, c5, c6, c7]

 

# affichage main 
print("main2")
print(main2)
# Trie de la main
print("main2 trié")
main2.sort(reverse=True)
print(main2)


# Décomposition de la main
# liste de string pour la couleur
liste_couleur = Combinaison.decompocou(main2)
# lsite d'int pour la valeur
liste_value = Combinaison.decompolis(main2)


# recherche valeur max d'une liste
def max (int_list):
    max = 0
    for i in range(0, len(int_list)):
        if int_list[i] > max:
            max = int_list[i]
    return max

# Recherche d'une suite
# CHANGER le main2 
def Suite(int_list):
    count = 1
    result = []
    for i in range(0, 5):
        if int_list[i] - int_list[i+1] == 1:
            result.append(int_list[i])
            print (result)
            count += 1
            if count >= 5: 
                return ("suite avec comme valeur la plus haute", main2[0])
        else:
            count = 1
    return ("pas de suite")
suite = Suite(liste_value)
print(suite)

# Recherche d'une couleur
def couleur (string_list):
    count = Counter(string_list)
    for string, occurence in count.items():
        if occurence >= 5:
            for i in range (len(main2)):
                if main2[i]._color.name == string:
                    return ("couleur de ", occurence, "cartes de couleur",string, "avec comme valeur la plus haute", main2[i])
    return ("Pas de couleur")  

couleur = couleur(liste_couleur)
print(couleur)



# Cherche si il y a une quinte flush

'''
if (couleur == True and suite == True): 
    print("Quinte flush")
else: 
    print("Pas de quinte flush")
'''



## recherche des répétitions
def repetition (int_list):
    count = Counter(int_list)
    for number, occurence in count.items():
        if occurence >= 2:
            print ("la carte ", number, "se répète", occurence, "fois") 
            if occurence == 2:
                return ("Paire de ", number) and int_list
            if occurence == 3:
                return ("Brelan de ", number)
            if occurence == 4:
                return ("Carré de", number)
            if occurence == 5:
                return ("Les dés sont pipés")
    return ("Pas de répétition")


def remove_duplicates(liste_value):
    # Création d'une nouvelle liste vide pour stocker les valeurs uniques
    nv_main = []
    # Parcours de la liste originale
    for i in liste_value:
        # Si la valeur actuelle n'est pas déjà dans la nouvelle liste, on l'ajoute
        if i not in nv_main:
            nv_main.append(i)
    return nv_main

# Appel de la fonction avec la liste originale en argument
unique_list = remove_duplicates(liste_value)
print("Liste sans doublons:", unique_list)
    

print(repetition(liste_value))

