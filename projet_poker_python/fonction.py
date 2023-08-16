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

        #########################  RECHERCHE VALEUR MAX #########################

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
                        if deck[i]._value.value == number:
                            number = deck[i]._value
                        if deck[i]._value.value == final[0]:
                            result.append(deck[i])

                    return [True, (Combinaison.CARRE, str(number), str(result[0]._value))]

                # Si égal à 5, alors il y a un problème
                if occurence == 5:
                    return ("Les dés sont pipés")

        # Si il y a une paire et un brelan alors on a un full
        if len(paire) == 1 and len(brelan) == 1:
            # Affichage de la combinaison sous forme de string
            for i in range(len(deck)):
                if deck[i]._value.value == paire[0]:
                    nom = deck[i]._value
                if deck[i]._value.value == brelan[0]:
                    nom2 = deck[i]._value
            return [True, (Combinaison.FULL, str(nom2), str(nom))]

        if len(brelan) == 2:
            # Affichage de la combinaison sous forme de string
            for i in range(len(deck)):
                if deck[i]._value.value == brelan[0]:
                    nom = deck[i]._value
                if deck[i]._value.value == brelan[1]:
                    nom2 = deck[i]._value
            return [True, (Combinaison.FULL,  str(nom), str(nom2))]

        else:
            return [False]

    '''

        #########################  RECHERCHE PAIRE OU BRELAN #########################

    '''

    def pairebrelan(int_list, deck):
        # remplacer les 1 par des 14 dans la liste
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
                    nom = deck[i]._value
            return (Combinaison.PAIRE, str(nom), str(result[0]._value), str(result[1]._value), str(result[2]._value))

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
                    nom = deck[i]._value
            return (Combinaison.BRELAN, str(nom), str(result[0]._value), str(result[1]._value))

        # Si il y a deux paires
        if len(paire) >= 2:
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
                if deck[i]._value.value == paire[1]:
                    nom2 = deck[i]
                if deck[i]._value.value == paire[0]:
                    nom = deck[i]

            return (Combinaison.DOUBLE_PAIRES, str(nom._value), str(nom2._value), str(result[0]._value))

        if len(paire) == 3:

            # Affichage de la combinaison sous forme de string
            for i in range(len(deck)):
                if deck[i]._value.value == paire[0]:
                    nom = deck[i]._value
                if deck[i]._value.value == paire[1]:
                    nom2 = deck[i]._value
                if deck[i]._value.value == paire[2]:
                    nom3 = deck[i]._value

            return (Combinaison.DOUBLE_PAIRES, str(nom), str(nom2), str(nom3))

        # S'il n'y a rien
        if len(paire) == 0 and len(brelan) == 0:
            final = []
            # On affiche les 5 cartes les plus hautes
            for i in range(5):
                final.append(deck[i])
            return (Combinaison.RIEN, str(final[0]._value), str(final[1]._value), str(final[2]._value), str(final[3]._value), str(final[4]._value))

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
                            nom = main[i]._value
                    return [True, (Combinaison.SUITE, str(nom))]
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

                    if main[i]._color.name == string:
                        test = main[i]._color
                    # On  utilise que les cartes de la couleur
                    if main[i]._color.name == string:
                        # Recherche carte la plus haute
                        valmax = main[i]._value
                        # on ajoute les cartes de la couleur à la maincou
                        main.sort(reverse=True)

                        for i in range(len(main)):
                            if main[i]._color.name == string:
                                maincou.append(str(main[i]._value))

                        # On prend les 5 cartes les plus hautes
                        if len(maincou) > 5:
                            maincou = maincou[:5]
                        # [0] = vérification
                        # [1] = Résultat full
                        # [2] = Résultat couleur
                        return [True, (Combinaison.FULL, main[0]._color, str(valmax)), (Combinaison.COULEUR, test, maincou[0], maincou[1], maincou[2], maincou[3], maincou[4])]
            return [False]

    '''

        #########################  Résolution #########################
        
    '''

    def resolution(main):
        print(len(main))
        if len(main) != 7:
            raise ValueError("La main doit contenir 7 cartes")
        else:
            main3 = main
            #print("MAIN :")
            # print(main3)
            main3.sort(reverse=True)
            #print("MAIN trié:")
            # print(main3)
            # print("")
            #print("COMBINAISON la plus forte:")
            # Décomposition de la main
            # liste de string pour la couleur
            print("MAIN :" + str(main3))
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
                return (color[1])
            # On regarde s'il y a un carre ou un full
            elif carrefull[0] == True:
                return (carrefull[1])

            # on regarde s'il y a une suite
            elif suite[0] == True:
                return (suite[1])

            # on regarde s'il y a une couleur
            elif color[0] == True:
                return (color[2])

            # on regarde s'il y a un brelan ou une paire. Si rien alors on renvoie la carte la plus haute
            else:
                liste_value = test_combinaison.decompolis(main3)
                return (test_combinaison.pairebrelan(liste_value, main3))
