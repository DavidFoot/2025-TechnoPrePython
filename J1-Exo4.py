"""Calculer le périmètre d'un cercle
Demander à l'utilisateur le rayon d'un cercle, puis afficher son périmètre.
"""

import math

def CalcPerimetreCercle(rayon):
    print(f"Le perimetre du cercle de rayon {rayon} est de : {2*math.pi*rayon}")

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

CalcPerimetreCercle(AskFloat("Veuillez entrer le rayon du cercle dont il faut calculer le périmetre : "))