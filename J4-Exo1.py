"""
    MINI RPG
"""
import random

current_level = 1
current_pv = 5

while current_pv > 0:
    current_ennemi_level = random.randint(current_level-1,current_level+1)
    if current_ennemi_level <= current_level  :
        current_level +=1
        print("YOuhou je gagne un level :D")
        continue
    elif current_ennemi_level > current_level:
        current_pv -= 1
        print(f"Aarrgh, je meurs... (Pv restant:{current_pv})")
        if current_pv > 0 :
            continue
        else:
            print("Vous etes mort au niveau " + str(current_level))