import enum
import sys
from collections import Counter

# Fichier de la classe
from card_deck import *
from fonction import *





# Main défini par la classe
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

# Triage de la main
main.sort()
print('main trié')
print (main)


# Main manuel 

c1 = Card(Value.CINQ, Color.P)
c2 = Card(Value.SIX, Color.P)
c3 = Card(Value.NEUF, Color.P)
c4 = Card(Value.HUIT, Color.P)
c5 = Card(Value.VALET, Color.P)
c6 = Card(Value.SIX, Color.K)
c7 = Card(Value.SEPT, Color.K)

main2 = [c1, c2, c3, c4, c5, c6, c7]

print("main2")
print(main2)
print("main2 trié")
main2.sort()
print(main2)


def Suite(int_list):
    count = 1
    for i in range(1, len(int_list)):
        if int_list[i] - int_list[i-1] == 1:
            count += 1
            if count >= 5:
                return ("suite de ", count+1, "cartes de suite") and True
        else:
            count = 1
    return False and ("pas de suite")



def couleur (string_list):
    count = Counter(string_list)
    for string, occurence in count.items():
        if occurence >= 5:
            return ("couleur de ", occurence, "cartes de couleur", string) and True
    return ("Pas de couleur") and False


dd = Combinaison.decompocou(main)
d = couleur(dd)


ss = Combinaison.decompolis(main2)
s = Suite(ss)

print(ss)
print(s)
print(dd)
print(d)

if (s == True and d == True): 
    print("Quinte flush")
else: 
    print("Pas de quinte flush")


def rep (int_list):
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
    return ("Pas de répétition")

rr = rep(ss)
print(rr)

def max (int_list):
    max = 0
    for i in range(0, len(int_list)):
        if int_list[i] > max:
            max = int_list[i]
    return max

m = max(ss)
print(m)



