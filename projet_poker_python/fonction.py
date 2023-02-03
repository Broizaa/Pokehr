from card_deck import Card, Value, Color
from combinaison import Combinaison
from collections import Counter


# Fichier qui regroupe les fonctions de recherche de combinaison

class test_combinaison:

    '''

        #########################  SEPARATION VALEUR ET COULEUR  #########################

    '''
    # Sépare les valeurs
    def decompolis(liste2):
        value = []

        for i in range(len(liste2)):
            value.append(liste2[i]._value.value)

        # retourne couleur et valeur
        return value

    # Sépare les couleurs
    def decompocou(liste3):
        # Séparation du tuple
        color = []

        for i in range(len(liste3)):
            color.append(liste3[i]._color.name)

        # retourne couleur et valeur
        return color

    '''

        #########################  RECHERCHE CARRE OU FULL #########################

    '''

    # recherche valeur max d'une liste
    def max(int_list):
        max = 0
        for i in range(0, len(int_list)):
            if int_list[i] > max:
                max = int_list[i]
        return max

    '''

        #########################  RECHERCHE CARRE OU FULL #########################

    '''

    def Carrefull(int_list, deck):
        # liste de stockage des valeurs des paires et des brelans
        paire = []
        brelan = []
        # Comptage des répétitions
        count = Counter(int_list)
        for number, occurence in count.items():
            # Si il y a plus de deux répétitions
            if occurence >= 2:

                # Si égal à 2, on ajoute la valeur à la liste des paires
                if occurence == 2:
                    paire.append(number)
                    # On supprime les deux valeurs de la liste
                    for i in range(occurence):
                        int_list.remove(number)

                # Si égal à 3, on ajoute la valeur à la liste des brelans
                if occurence == 3:
                    brelan.append(number)
                    # On supprime les trois valeurs de la liste
                    for i in range(occurence):
                        int_list.remove(number)

                # Si égal à 4
                if occurence == 4:
                    # On supprime les quatre valeurs de la liste
                    for i in range(occurence):
                        int_list.remove(number)
                    # On cherche la valeur max dans le reste
                    final = []
                    result = []
                    # On appelle la fonction max pour trouver la valeur max
                    maxi = max(int_list)
                    # On ajoute la valeur max à la liste final
                    final.append(maxi)
                    # On supprime la valeur max de la liste
                    int_list.remove(maxi)
                    # Affichage de la combinaison sous forme de carte
                    for i in range(len(deck)):
                        if deck[i]._value.value == final[0]:
                            result.append(deck[i])
                            return [True, (Combinaison.CARRE.name, number, "avec", result)]

                # Si égal à 5, alors il y a un problème
                if occurence == 5:
                    return ("Les dés sont pipés")

        # Si il y a une paire et un brelan alors on a un full
        if len(paire) == 1 and len(brelan) == 1:
            # Affichage de la combinaison sous forme de string
            for i in range(len(deck)):
                if deck[i]._value.value == paire[0]:
                    nom = deck[i]._value.name
                if deck[i]._value.value == brelan[0]:
                    nom2 = deck[i]._value.name
            return [True, (Combinaison.FULL.name, "de", nom2, "et", nom)]

        if len(brelan) == 2:
            # Affichage de la combinaison sous forme de string
            for i in range(len(deck)):
                if deck[i]._value.value == brelan[0]:
                    nom = deck[i]._value.name
                if deck[i]._value.value == brelan[1]:
                    nom2 = deck[i]._value.name
            return [True, (Combinaison.FULL.name, "de", nom2, "et", nom)]

        else:
            return [False]

    '''

        #########################  RECHERCHE PAIRE OU BRELAN #########################

    '''

    def pairebrelan(int_list, deck):
        # liste de stockage des valeurs des paires et des brelans
        paire = []
        brelan = []
        # Comptage des répétitions
        count = Counter(int_list)
        for number, occurence in count.items():
            # Si il y a plus de deux répétitions
            if occurence >= 2:

                # Si égal à 2, on ajoute la valeur à la liste des paires
                if occurence == 2:
                    paire.append(number)
                    # On supprime les deux valeurs de la liste
                    for i in range(occurence):
                        int_list.remove(number)

                # Si égal à 3, on ajoute la valeur à la liste des brelans
                if occurence == 3:
                    brelan.append(number)
                    # On supprime les trois valeurs de la liste
                    for i in range(occurence):
                        int_list.remove(number)

                # Si égal à 5, alors il y a un problème
                if occurence == 5:
                    return ("Les dés sont pipés")

        # Si il y a une paires
        if len(paire) == 1:
            final = []
            result = []
            # On appelle la fonction max pour trouver les trois valeurs max
            for i in range(3):
                maxi = max(int_list)
                final.append(maxi)
                int_list.remove(maxi)
            # Affichage des valeurs max sous forme de carte
            for i in range(len(deck)):
                if deck[i]._value.value == final[0] or deck[i]._value.value == final[1] or deck[i]._value.value == final[2]:
                    result.append(deck[i])
            # Affichage de la combinaison sous forme de string
            for i in range(len(deck)):
                if deck[i]._value.value == paire[0]:
                    nom = deck[i]._value.name
            return (Combinaison.PAIRE.name, "de", nom, "avec", result, "comme reste")

        # Si il y a un brelan
        if len(brelan) == 1:
            final = []
            result = []
            # On appelle la fonction max pour trouver les deux valeurs max
            for i in range(2):
                maxi = max(int_list)
                final.append(maxi)
                int_list.remove(maxi)
            # Affichage des valeurs max sous forme de carte
            for i in range(len(deck)):
                if deck[i]._value.value == final[0] or deck[i]._value.value == final[1]:
                    result.append(deck[i])
            # Affichage de la combinaison sous forme de string
            for i in range(len(deck)):
                if deck[i]._value.value == brelan[0]:
                    nom = deck[i]._value.name
            return (Combinaison.BRELAN.name, nom, result)

        # Si il y a deux paires
        if len(paire) == 2:
            final = []
            result = []
            # On appelle la fonction max pour trouver les deux valeurs max
            maxi = max(int_list)
            final.append(maxi)
            int_list.remove(maxi)
            # Affichage des valeurs max sous forme de carte
            for i in range(len(deck)):
                if deck[i]._value.value == final[0]:
                    result.append(deck[i])
            # Affichage de la combinaison sous forme de string
            for i in range(len(deck)):
                if deck[i]._value.value == paire[0]:
                    nom = deck[i]._value.name
                if deck[i]._value.value == paire[1]:
                    nom2 = deck[i]._value.name

            return (Combinaison.DOUBLE_PAIRES.name, nom, "et", nom2, "avec", result, "comme reste")

        if len(paire) == 3:

            # Affichage de la combinaison sous forme de string
            for i in range(len(deck)):
                if deck[i]._value.value == paire[0]:
                    nom = deck[i]._value.name
                if deck[i]._value.value == paire[1]:
                    nom2 = deck[i]._value.name
                if deck[i]._value.value == paire[2]:
                    nom3 = deck[i]._value.name

            return (Combinaison.DOUBLE_PAIRES.name, nom, "et", nom2, "avec", nom3, "comme reste")

        # S'il n'y a rien
        if len(paire) == 0 and len(brelan) == 0:
            final = []
            # On affiche les 5 cartes les plus hautes
            for i in range(5):
                final.append(deck[i])
            return (Combinaison.RIEN.name, final)

    '''

        #########################  RECHERCHE SUITE #########################

    '''
    # On cercher s'il y a une couleur
    def Suite(int_list, main):
        # Compteur
        count = 0
        # liste des cartes de la suite
        result = []
        # On parcourt la main
        for i in range(0, 6):
            # Si la valeur de la carte est égale à la valeur de la carte suivante ou si la valeur de la carte est égale à la valeur de la carte suivante
            if int_list[i] - int_list[i+1] == 1 or int_list[i] == int_list[i+1]:
                # On ajoute la carte à la liste des cartes de la suite à résult si elle n'y est pas déjà
                if int_list[i] not in result:
                    result.append(int_list[i])
                # On incrémente le compteur
                    count += 1
                # Si le compteur est égal ou supérieur à 5
                if count >= 5:
                    # On trie la liste des cartes de la suite dans l'ordre décroissant
                    result.sort(reverse=True)
                    # On transforme la liste des cartes de la suite en liste de string
                    for i in range(len(main)):
                        if main[i]._value.value == result[0]:
                            nom = main[i]._value.name
                    return [True, ("avec comme carte la plus haute", nom)]
            else:
                count = 1
        if count < 5:
            return [False]

    '''

        #########################  RECHERCHE COULEUR #########################

    '''

    def couleur(string_list, main):
        # main de couleur
        maincou = []
        # On compte le nombre d'occurence de chaque couleur
        count = Counter(string_list)
        for string, occurence in count.items():
            # Si il y a 5 occurences de la même couleur
            if occurence >= 5:
                for i in range(len(main)):
                    # On  utilise que les cartes de la couleur
                    if main[i]._color.name == string:
                        # Recherche carte la plus haute
                        valmax = main[i]
                        # on ajoute les cartes de la couleur à la maincou
                        for i in range(len(main)):
                            if main[i]._color.name == string:
                                maincou.append(main[i])
                        maincou.sort(reverse=True)
                        # On prend les 5 cartes les plus hautes
                        if len(maincou) > 5:
                            maincou = maincou[:5]
                        return [True, (main[0]._color.name, "avec comme carte la plus haute", valmax), (string, "avec comme valeur", maincou)]
            return [False]

    '''

        #########################  Résolution #########################

    '''

    def resolution(main):
        main3 = main
        print("MAIN :")
        print(main3)
        main3.sort(reverse=True)
        print("MAIN trié:")
        print(main3)
        print("")
        print("COMBINAISON la plus forte:")
        # Décomposition de la main
        # liste de string pour la couleur
        liste_couleur = test_combinaison.decompocou(main3)
        # liste d'int pour la valeur
        liste_value = test_combinaison.decompolis(main3)
        suite = test_combinaison.Suite(liste_value, main3)
        #suite = Suite(liste_value, main3)
        color = test_combinaison.couleur(liste_couleur, main3)
        carrefull = test_combinaison.Carrefull(liste_value, main3)
        # Résultat bool de la suite et de la couleur
        # print(carrefull[0])
        # Résolution de la main

        # s'il y a une suite et une couleur alors il y a une quinte flush
        if color[0] == True and suite[0] == True:
            return (Combinaison.SUITE_COULEUR.name, color[1])
        # On regarde s'il y a un carre ou un full
        elif carrefull[0] == True:
            return (carrefull[1])

        # on regarde s'il y a une suite
        elif suite[0] == True:
            return (Combinaison.SUITE.name, suite[1])

        # on regarde s'il y a une couleur
        elif color[0] == True:
            return (Combinaison.COULEUR.name, color[2])

        # on regarde s'il y a un brelan ou une paire. Si rien alors on renvoie la carte la plus haute
        else:
            liste_value = test_combinaison.decompolis(main3)
            return (test_combinaison.pairebrelan(liste_value, main3))
