"""Ascenseur
Un employé arrive dans l'ascenceur (on ne connait pas son étage il doit l'introduire) (16 étages max)
Il doit aller au 13 ème étage
Il doit ensuite descendre au -2
(-2 à 13)

Combien d'étages a-t-il parcouru entre son entrée et l'étage 13
Combien d'étages a-t-il parcouru au total

BONUS : Combien d'étages peut-il parcourir au maximum en 3 aller-retour en partant de l'étage 3, 7, 9"""

MAX = 16
FIRSTSTOP = 13
SECONDSTOP = -2
currentFloor = int(input("Introduire l'Etage De depart : " ))
print("Total Parcouru pour arriver a l etage 13 : " + str(abs(FIRSTSTOP - currentFloor)))
print("Total Parcouru au total : " + str(abs(FIRSTSTOP - currentFloor) + (FIRSTSTOP - SECONDSTOP)))

