def renvoi_age_plus_5(_mon_age):
    return _mon_age + 5

def affiche_nom_age(_nom,_annee):
    print(f"Votre nom est {_nom} et votre age est {2025-_annee} ans")

mon_age = 40
print("Mon age +5 est : " + str(renvoi_age_plus_5(mon_age)))

affiche_nom_age("David", 1982)