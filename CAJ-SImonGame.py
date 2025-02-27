""""
Vous allez demander à l'utilisateur de mémoriser une séquence de chiffres de plus en plus longue.
La séquence sera aléatoire, et commencera avec 4 chiffres. L'utilisateur à 3 secondes pour la mémoriser.
Si il donne la bonne réponse, on rajoute un nouveau chiffre à la suite de la séquence on la redemande à l'utilisateur...
et ainsi de suite, jusqu'à ce que l'utilisateur se trompe.

- Remarques :
La séquence sera affichée pendant 3 secondes, puis effacée de l'écran pour que l'utilisateur donne sa réponse.
Pour effacer l'écran, vous allez copier dans votre code cette fonction :

import os
def clear_screen():
    if(os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')


Pour bloquer l'execution de votre programme pendant "x" secondes, vous utiliserez la fonction :

import time
time.sleep(x)

Vous devez aussi gérer un score, initialement égal à 0, et qui s'incrémente de 1 à chaque bonne réponse.

Quand l'utilisateur donne une mauvaise réponse, le programme s'arrête directement et affiche (exemple) :
Mauvaise réponse, la séquence était : 77686
Votre score final : 1




- Voici le déroulement exact de votre programme :

0 - Générer une chaine de caractère qui contient 4 chiffres aléatoires, c'est votre séquence initiale.

1 - Ajouter un nouveau nombre aléatoire à la fin de votre séquence

2 - Nettoyer l'écran et affichez "Retenez la séquence" pendant 1 seconde

3 - Afficher la séquence à mémoriser pendant 3 secondes

4 - Nettoyer n'écran et demander la réponse à l'utilisateur

5 - Si la réponse est bonne, afficher pendant 1 seconde "Bonne réponse, votre score est : xxx", puis reboucler à l'étape 1

5bis - Si la réponse n'est pas bonne, sortir du programme et afficher : "Mauvaise réponse, la séquence était : xxxx, votre score final : xxxx"

Questions pour cet exercice
Collez votre code ici au format code <>

OPTIONNEL : Dites moi ici vos remarques : avez-vous aimé cet exercice ? Est-ce que c'était difficile/facile ? Souhaitez-vous d'autres exercices de ce type ? Combien de temps ça vous a pris ?
"""

import os
import sys
import time
import random

def clear_screen():
    if "win" in sys.platform :
        os.system("cls")
    else:
        os.system("clear")

clear_screen()
time_before_launch = 3
time_before_hide_value = 2
longueur_premiere_sequence = 4


# Petit timer pour se preparer avant de demarrer
for i in range (time_before_launch,0,-1) :
    print(f"Le jeu commence dans {i} secondes")
    time.sleep(1)
    clear_screen()

# Generer la sequence originale
simon_value = ''
for i in range(longueur_premiere_sequence):
    simon_value += str(random.randint(0,9))

while True:
    print(f"La valeur a retenir est {simon_value}")
    time.sleep(time_before_hide_value)
    clear_screen()
    user_input = input("Quelle était la séquence affichée: ")
    if user_input == simon_value :
        print("Bravo on continue alors..")
        time.sleep(2)
        clear_screen()
        simon_value += str(random.randint(0, 9))
    else:
        print("You lose")
        break
