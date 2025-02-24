"""Calculer l'aire d'un rectangle
        Demander à l'utilisateur la longueur et la largeur d'un rectangle, puis afficher l'aire."""

def AskInt(question):
    isCorrectInt = False
    value = 0
    while not isCorrectInt:
        try:
            value = int(input(question))
        except ValueError:
            isCorrectInt = False
            print("La valeur enrée n'est pas une valeur entière correcte")
        else:
            isCorrectInt = True
    return value

longueur = AskInt("Entrez la longueur du rectangle : ")
largeur = AskInt("Entrez la largeur du rectangle : ")

print("L'aire de votre rectangle est de : " + str(longueur*largeur))