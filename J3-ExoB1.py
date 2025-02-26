"""
Créer un programme dans lequel le système choisira un nombre aléatoire entre 1 et 100

On demande à l'utilisateur de deviner un nombre
Chaque fois que l’utilisateur se trompe, on lui donne un indice (trop haut ou trop bas)
L'utilisateur a un nombre d'essais maximum de 10 pour trouver le bon nombre
"""
import random

nbr_life = 10
nbr_to_find = random.randint(1,100)
print(f"Nombre a trouver {nbr_to_find}")
current_life = nbr_life
user_nbr = -1

while current_life > 0 and  user_nbr != nbr_to_find :
    try:
        user_nbr = int(input("Entrez votre proposition entre 1 et 100 : "))
    except ValueError:
        user_nbr = -1
        continue
    if user_nbr == nbr_to_find :
        print("Bravo vous avez trouvé le nombre magique")
    else:
        if user_nbr < nbr_to_find :
            print("Le nombre a trouver est plus grand")
        else:
            print("Le nombre a trouver est plus petit")
        current_life-=1
        if current_life > 0:
            print(f"Il vous reste {current_life} vies ")
    if current_life == 0:
        print(f"You lose, le nombre a trouver etait {nbr_to_find}")