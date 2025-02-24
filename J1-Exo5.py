"""Multiplication de deux nombres
Demander à l'utilisateur de saisir deux nombres, puis afficher leur produit.
"""

def Multiply(x,y):
    print("Le produit est de " + str(x * y))

def AskFloat(question):
    isCorrectFloat = False
    value = 0
    while not isCorrectFloat:
        try:
            value = float(input(question))
        except ValueError:
            isCorrectFloat = False
            print("La valeur entrée n'est pas une valeur float correcte")
        else:
            isCorrectFloat = True
    return value

Multiply(AskFloat("Valeur de x: "),AskFloat("Valeur de y: "))