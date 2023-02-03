from collections import Counter
from card_deck import *
from fonction import *
from combinaison import *

def repetition (int_list, deck):
    # liste de stockage des valeurs des paires et des brelans
    paire = []
    brelan = []
    # Comptage des répétitions
    count = Counter(int_list)
    for number, occurence in count.items():
        #Si il y a plus de deux répétitions
        if occurence >= 2:
            
            # Si égal à 2, on ajoute la valeur à la liste des paires
            if occurence == 2:
                paire.append(number)
                # On supprime les deux valeurs de la liste
                for i in range (occurence):
                    int_list.remove(number)
            
            # Si égal à 3, on ajoute la valeur à la liste des brelans
            if occurence == 3:
                brelan.append(number)
                # On supprime les trois valeurs de la liste
                for i in range (occurence):
                    int_list.remove(number)

            # Si égal à 4
            if occurence == 4:
                # On supprime les quatre valeurs de la liste
                for i in range (occurence):
                    int_list.remove(number)
                # On cherche la valeur max dans le reste
                final = []
                result= []
                # On appelle la fonction max pour trouver la valeur max
                maxi = max(int_list)
                # On ajoute la valeur max à la liste final
                final.append(maxi)
                # On supprime la valeur max de la liste
                int_list.remove(maxi)
                # Affichage de la combinaison sous forme de carte
                for i in range (len(deck)):
                    if deck[i]._value.value == final[0]:
                        result.append(deck[i])
                        return (Combinaison.CARRE.name, number, "avec", result)
           
            # Si égal à 5, alors il y a un problème
            if occurence == 5:
                return ("Les dés sont pipés")

    # Si il y a une paire et un brelan alors on a un full
    if len(paire) == 1 and len(brelan) == 1:
        #Affichage de la combinaison sous forme de string
        for i in range (len(deck)):
            if deck[i]._value.value == paire[0]:
                nom = deck[i]._value.name
            if deck[i]._value.value == brelan[0]:
                nom2 = deck[i]._value.name
        return (Combinaison.FULL.name, "de", nom, "et", nom2)

    # Si il y a une paires
    if len(paire) == 1:
        final = []
        result= []
        # On appelle la fonction max pour trouver les trois valeurs max
        for i in range(3):
            maxi = max(int_list)
            final.append(maxi)
            int_list.remove(maxi)
        # Affichage des valeurs max sous forme de carte
        for i in range (len(deck)):
            if deck[i]._value.value == final[0] or deck[i]._value.value == final[1] or deck[i]._value.value == final[2]:
                result.append(deck[i])
        # Affichage de la combinaison sous forme de string
        for i in range (len(deck)):
            if deck[i]._value.value == paire[0]:
                nom = deck[i]._value.name
        return (Combinaison.PAIRE.name, "de", nom, "avec", result, "comme reste")
    
    # Si il y a un brelan
    if len(brelan) == 1:
        final = []
        result= []
        # On appelle la fonction max pour trouver les deux valeurs max
        for i in range(2):
            maxi = max(int_list)
            final.append(maxi)
            int_list.remove(maxi)
        # Affichage des valeurs max sous forme de carte
        for i in range (len(deck)):
            if deck[i]._value.value == final[0] or deck[i]._value.value == final[1]:
                result.append(deck[i])
        # Affichage de la combinaison sous forme de string
        for i in range (len(deck)):
            if deck[i]._value.value == brelan[0]:
                nom = deck[i]._value.name
        return (Combinaison.BRELAN.name, brelan[0], result)
    
    # Si il y a deux paires
    if len(paire) == 2:
        final = []
        result= []
        # On appelle la fonction max pour trouver les deux valeurs max
        maxi = max(int_list)
        final.append(maxi)
        int_list.remove(maxi)
        # Affichage des valeurs max sous forme de carte
        for i in range (len(deck)):
            if deck[i]._value.value == final[0]:
                result.append(deck[i])
        # Affichage de la combinaison sous forme de string
        for i in range (len(deck)):
            if deck[i]._value.value == paire[0]:
                nom = deck[i]._value.name
            if deck[i]._value.value == paire[1]:
                nom2 = deck[i]._value.name
        
        return (Combinaison.DOUBLE_PAIRES.name, nom, "et", nom2, "avec", result, "comme reste")
    
    # S'il n'y a rien
    if len(paire) == 0 and len(brelan) == 0:
        final = []
        # On affiche les 5 cartes les plus hautes
        for i in range (5):
            final.append(deck[i])
        return(Combinaison.RIEN.name, final)