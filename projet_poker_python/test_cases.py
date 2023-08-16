# test_cases.py

from card_deck import Card, Deck, Color, Value

test_cases = (
    # suite couleur
    [
        Card(Value.NEUF, Color.K),
        Card(Value.DIX, Color.K),
        Card(Value.DAME, Color.K),
        Card(Value.SEPT, Color.K),
        Card(Value.HUIT, Color.K),
        Card(Value.SIX, Color.K),
        Card(Value.CINQ, Color.K),
    ],
    # carre
    [Card(Value.AS, Color.T),
     Card(Value.AS, Color.K),
     Card(Value.QUATRE, Color.K),
     Card(Value.TROIS, Color.C),
     Card(Value.VALET, Color.K),
     Card(Value.AS, Color.P),
     Card(Value.AS, Color.C),
     ],
    # full -> 1 brelan + 1 paire
    [Card(Value.AS, Color.T),
     Card(Value.TROIS, Color.K),
     Card(Value.QUATRE, Color.K),
     Card(Value.TROIS, Color.C),
     Card(Value.QUATRE, Color.P),
     Card(Value.TROIS, Color.T),
     Card(Value.CINQ, Color.K),
     ],
    # full -> 2 brelans
    [Card(Value.AS, Color.T),
     Card(Value.TROIS, Color.K),
     Card(Value.QUATRE, Color.K),
     Card(Value.TROIS, Color.C),
     Card(Value.QUATRE, Color.C),
     Card(Value.TROIS, Color.T),
     Card(Value.QUATRE, Color.T),
     ],
    # full -> 1 brelan + 2 paires
    [
        Card(Value.CINQ, Color.T),
        Card(Value.TROIS, Color.K),
        Card(Value.QUATRE, Color.K),
        Card(Value.TROIS, Color.C),
        Card(Value.QUATRE, Color.P),
        Card(Value.TROIS, Color.T),
        Card(Value.CINQ, Color.K),
    ],

    # suite -> AS comme as
    [
        Card(Value.AS, Color.T),
        Card(Value.ROI, Color.P),
        Card(Value.DAME, Color.K),
        Card(Value.DIX, Color.C),
        Card(Value.VALET, Color.K),
        Card(Value.DEUX, Color.P),
        Card(Value.CINQ, Color.T),
    ],
    # suite -> AS comme 1
    [
        Card(Value.AS, Color.T),
        Card(Value.QUATRE, Color.P),
        Card(Value.DAME, Color.K),
        Card(Value.TROIS, Color.C),
        Card(Value.VALET, Color.K),
        Card(Value.DEUX, Color.P),
        Card(Value.CINQ, Color.T),
    ],
    # suite:  au milieu
    [Card(Value.AS, Color.T),
     Card(Value.DAME, Color.K),
     Card(Value.DIX, Color.C),
     Card(Value.VALET, Color.K),
     Card(Value.NEUF, Color.P),
     Card(Value.CINQ, Color.T),
     Card(Value.HUIT, Color.K),
     ],
    # color
    [Card(Value.AS, Color.T),
     Card(Value.TROIS, Color.K),
     Card(Value.DAME, Color.K),
     Card(Value.DIX, Color.C),
     Card(Value.VALET, Color.K),
     Card(Value.NEUF, Color.K),
     Card(Value.CINQ, Color.K),
     ],
    # brelan
    [Card(Value.AS, Color.T),
     Card(Value.TROIS, Color.K),
     Card(Value.QUATRE, Color.K),
     Card(Value.TROIS, Color.C),
     Card(Value.VALET, Color.K),
     Card(Value.TROIS, Color.T),
     Card(Value.CINQ, Color.K),
     ],
    # double paire -> 3 paires
    [Card(Value.AS, Color.T),
     Card(Value.AS, Color.K),
     Card(Value.QUATRE, Color.K),
     Card(Value.TROIS, Color.C),
     Card(Value.TROIS, Color.K),
     Card(Value.VALET, Color.P),
     Card(Value.QUATRE, Color.C),
     ],
    # double paire -> 2 paires
    [
        Card(Value.DAME, Color.T),
        Card(Value.DAME, Color.K),
        Card(Value.QUATRE, Color.K),
        Card(Value.DEUX, Color.C),
        Card(Value.TROIS, Color.K),
        Card(Value.AS, Color.P),
        Card(Value.AS, Color.C),
    ],
    # paire
    [
        Card(Value.DAME, Color.T),
        Card(Value.ROI, Color.K),
        Card(Value.QUATRE, Color.K),
        Card(Value.AS, Color.C),
        Card(Value.TROIS, Color.K),
        Card(Value.VALET, Color.P),
        Card(Value.AS, Color.C),
    ],
    # paire
    [
        Card(Value.DAME, Color.T),
        Card(Value.DIX, Color.K),
        Card(Value.QUATRE, Color.K),
        Card(Value.SIX, Color.C),
        Card(Value.TROIS, Color.K),
        Card(Value.VALET, Color.P),
        Card(Value.AS, Color.C),
    ]
)

datasets = (
    (Card(Value.NEUF, Color.P), Card(Value.VALET, Color.P), Card(Value.DEUX, Color.T), Card(Value.VALET, Color.K),
        Card(Value.DIX, Color.P), Card(Value.SEPT, Color.P), Card(Value.SIX, Color.K)),
    (Card(Value.NEUF, Color.P), Card(Value.VALET, Color.P), Card(Value.NEUF, Color.T), Card(Value.AS, Color.K),
        Card(Value.NEUF, Color.K), Card(Value.NEUF, Color.T), Card(Value.AS, Color.T)),
    (Card(Value.SEPT, Color.P), Card(Value.ROI, Color.P), Card(Value.SEPT, Color.T), Card(Value.ROI, Color.K),
        Card(Value.ROI, Color.P), Card(Value.AS, Color.P), Card(Value.SEPT, Color.K)),
    (Card(Value.TROIS, Color.P), Card(Value.ROI, Color.P), Card(Value.DIX, Color.T), Card(Value.VALET, Color.K),
        Card(Value.DAME, Color.P), Card(Value.AS, Color.P), Card(Value.AS, Color.T)),
    (Card(Value.TROIS, Color.P), Card(Value.CINQ, Color.P), Card(Value.DEUX, Color.T), Card(Value.CINQ, Color.K),
        Card(Value.QUATRE, Color.P), Card(Value.AS, Color.P), Card(Value.AS, Color.T)),
    (Card(Value.VALET, Color.K), Card(Value.SIX, Color.P), Card(Value.HUIT, Color.K), Card(Value.SIX, Color.K),
     Card(Value.QUATRE, Color.K), Card(Value.DEUX, Color.K)), Card(Value.DEUX, Color.P),
    (Card(Value.VALET, Color.K), Card(Value.VALET, Color.P), Card(Value.TROIS, Color.K), Card(Value.SIX, Color.K),
     Card(Value.QUATRE, Color.K), Card(Value.DIX, Color.K)), Card(Value.VALET, Color.P),
)
