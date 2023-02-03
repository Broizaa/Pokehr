import enum
import sys
from collections import Counter

# Fichier de la classe
from card_deck import *
from fonction import *
from combinaison import *



# Main définie par la classe
# Génération d'un deck


d= Deck()

# Extraction de X cartes
X = 7
mainal = [d.pop() for _ in range(X)]

 


## MAIN DE TEST ##

## SUITE ##

c1 = Card(Value.DEUX, Color.K)
c2 = Card(Value.DIX, Color.T)
c3 = Card(Value.UN , Color.P)
c4 = Card(Value.TROIS, Color.P)
c5 = Card(Value.UN, Color.T)
c6 = Card(Value.QUATRE, Color.P)
c7 = Card(Value.CINQ, Color.P)

mainsuite = [c1, c2, c3, c4, c5, c6, c7]



## FLUSH ##

c1 = Card(Value.DEUX, Color.P)
c2 = Card(Value.DIX, Color.P)
c3 = Card(Value.UN , Color.P)
c4 = Card(Value.TROIS, Color.P)
c5 = Card(Value.UN, Color.T)
c6 = Card(Value.QUATRE, Color.P)
c7 = Card(Value.CINQ, Color.P)

mainflush = [c1, c2, c3, c4, c5, c6, c7]



## COULEUR ##

c1 = Card(Value.DEUX, Color.P)
c2 = Card(Value.DIX, Color.P)
c3 = Card(Value.UN , Color.P)
c4 = Card(Value.VALET, Color.P)
c5 = Card(Value.UN, Color.T)
c6 = Card(Value.DAME, Color.P)
c7 = Card(Value.CINQ, Color.P)

maincou = [c1, c2, c3, c4, c5, c6, c7]


## PAIRE // CARRE // BRELAN // FULL // DOUBLE PAIRE ##

c1 = Card(Value.DEUX, Color.P)
c2 = Card(Value.DEUX, Color.C)
c3 = Card(Value.UN , Color.T)
c4 = Card(Value.VALET, Color.K)
c5 = Card(Value.NEUF, Color.T)
c6 = Card(Value.DAME, Color.K)
c7 = Card(Value.HUIT, Color.T)

mainpaire = [c1, c2, c3, c4, c5, c6, c7]
maincarre = [c1, c1, c1, c1, c5, c6, c7]
mainbrelan = [c1, c1, c1, c4, c5, c6, c7]
mainfull = [c1, c1, c1, c3, c3, c6, c7]
main2paire = [c1, c1, c3, c3, c5, c6, c7]


## RIEN ##

c1 = Card(Value.UN, Color.P)
c2 = Card(Value.TROIS, Color.C)
c3 = Card(Value.CINQ , Color.P)
c4 = Card(Value.SEPT, Color.K)
c5 = Card(Value.NEUF, Color.T)
c6 = Card(Value.VALET, Color.P)
c7 = Card(Value.ROI, Color.P)

mainrien = [c1, c2, c3, c4, c5, c6, c7]





while True:
    # Main définie par la classe
    # Génération d'un deck
    d= Deck()
    # Extraction de X cartes
    X = 7
    mainal = [d.pop() for _ in range(X)]

    # Choix de la main à tester
    choix = input("type de main ? ")
    if choix == "suite":
        print(test_combinaison.resolution(mainsuite))
    elif choix == "flush":
        print(test_combinaison.resolution(mainflush))
    elif choix == "couleur":
        print(test_combinaison.resolution(maincou))
    elif choix == "paire":
        print(test_combinaison.resolution(mainpaire))
    elif choix == "carre":
        print(test_combinaison.resolution(maincarre))
    elif choix == "brelan":
        print(test_combinaison.resolution(mainbrelan))
    elif choix == "full":
        print(test_combinaison.resolution(mainfull))
    elif choix == "2paire":
        print(test_combinaison.resolution(main2paire))
    elif choix == "rien":
        print(test_combinaison.resolution(mainrien))
    elif choix == "al":
        print(test_combinaison.resolution(mainal))
    elif choix == "exit":
        sys.exit()
    else:
        print("Erreur")