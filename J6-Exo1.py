""""
Boîte à outils

Supposez que vous ayez une boîte à outils avec plusieurs outils différents. Chaque outil est simplement représenté par son nom.
Voici ce que vous devez faire :

Définissez une liste appelée boite_outils qui contiendra les noms des outils. Par exemple, ["Tournevis", "Marteau", "Clé à molette"].

Ajoutez un nouvel outil à la liste boite_outils.

Retirez un outil de la liste boite_outils. Assurez-vous que si l'outil n'est pas présent dans la boîte à outils, le programme affiche un message approprié.

Affichez tous les outils présents dans la boîte à outils.

Affichez quel est l'outil à la 3 eme position

"""

boite_outils = [
    "Marteau",
    "Tournevis",
    "Scie",
    "Perceuse",
    "Pince",
    "Clé à molette",
    "Niveau à bulle",
    "Ruban à mesurer",
    "Mètre laser",
    "Ciseaux à bois"
]
outil_to_remove = "Tournevis"
boite_outils.append("Truelle")

if  outil_to_remove in boite_outils:
    boite_outils.remove(outil_to_remove)
    print(f"L'outil {outil_to_remove} a disparu de la boite a outils")
else:
    print("Cet outil n'est pas présent dans la boite a outils")

print("Voici la liste des éléments de ma liste : ", ' - '.join(boite_outils))

print("Le troisieme outil de ma boite est : " + boite_outils[2])