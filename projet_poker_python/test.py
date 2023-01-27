from card_deck import *
from fonction import *
from collections import Counter

c1 = Card(Value.DEUX, Color.P)
c2 = Card(Value.SIX, Color.P)
c3 = Card(Value.NEUF, Color.P)
c4 = Card(Value.HUIT, Color.P)
c5 = Card(Value.DIX, Color.T)
c6 = Card(Value.CINQ, Color.K)
c7 = Card(Value.SEPT, Color.P)

main2 = [c1, c2, c3, c4, c5, c6, c7]

# affichage main 
#print("main2")
#print(main2)
# Trie de la main
#print("main2 trié")
main2.sort(reverse=True)
print(main2)




# Décomposition de la main
# liste de string pour la couleur
liste_couleur = Combinaison.decompocou(main2)
# lsite d'int pour la valeur
liste_value = Combinaison.decompolis(main2)

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