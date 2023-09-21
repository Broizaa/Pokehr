
from card_deck import *
from fonction import *
from time import sleep

while True:
    d = Deck()

    # Extraction de X cartes
    X = 7

    mainal = [d.pop() for _ in range(X)]
    print(mainal)

    print(test_combinaison.resolution(mainal))
    sleep(5)
