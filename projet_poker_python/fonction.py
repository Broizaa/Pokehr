from card_deck import Card, Value, Color

class Combinaison :

    #Sépare les valeurs 
    def decompolis(liste2):
        value = []

        for i in range (len(liste2)):
            value.append(liste2[i]._value.value)

        print("main valeur")
        print(value)
        ## retourne couleur et valeur
        return  value

    #Sépare les couleurs 
    def decompocou (liste3):
        # Séparation du tuple
        color = []

        for i in range (len(liste3)):
            color.append(liste3[i]._color.name)

        print("main couleur")
        print(color)
        ## retourne couleur et valeur
        return color
    
    # Recherche si c'est une liste
    def suite (liste):
        a = liste[0]
        for i in range (1, len(liste)):
            if liste[i] != a+1:
                return False
            a = liste[i]
        return True

    # recherche si c'est une couleur
    def couleur (liste2):
        return True    
    
    # recherche s'il y a un brelan
    def brelan (liste3):
        return True
    
    # recherche s'il y a une paire
    def paire (liste4):
        return True

    # recherche s'il y a un carre
    def carre (liste5):
        return True