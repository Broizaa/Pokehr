from card_deck import Card, Value, Color
from combinaison import Combinaison
from collections import Counter


def couleur(string_list, main):
    maincou = []
    count = Counter(string_list)
    for string, occurence in count.items():
        if occurence >= 5:
            for i in range(len(main)):
                if main[i]._color.name == string:
                    valmax = main[i]
                    for i in range(len(main)):
                        if main[i]._color.name == string:
                            maincou.append(main[i])
                    maincou.sort(reverse=True)
                    if len(maincou) > 5:
                        maincou = maincou[:5]
                    return [True, (string, "avec comme carte la plus haute", valmax), (string, "avec comme valeur", maincou)]
        return [False]


string = "P"

print(Combinaison.COLOR)
