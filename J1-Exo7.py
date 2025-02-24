"""Calculer la moyenne de x nombres
Demander à l'utilisateur de saisir x nombres, puis afficher la moyenne de ces x nombres.
"""
somme = 0
compteur = 0
while True :
    nbrToAsk = input("Entrez un nombre ou STOP pour arreter et calculer la moyenne : ")
    try:
        nbrToAsk = float(nbrToAsk)
    except ValueError :
        if nbrToAsk.lower() == "stop" :
            break
        else:
            print("Valeur incorrecte, recommencez")
            continue
    compteur += 1
    somme += nbrToAsk
if compteur > 0 :
    print("La moyenne de tout les nombre est de : " + str(somme/compteur))
else:
    print("Pas de moyenne à afficher")

