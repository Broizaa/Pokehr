
from card_deck import *
from fonction import *

d = Deck()

# Extraction de X cartes
X = 7
mainal = [d.pop() for _ in range(X)]


print(test_combinaison.resolution(mainal))
