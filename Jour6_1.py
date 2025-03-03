la_ptiote_liste = ["Pwet","Coucou","Hello", "World"]
for item in la_ptiote_liste:
    print(item.upper())

print(f"Il y a {len(la_ptiote_liste)} elements dans la ptiote liste")

# List Slicing
print(f"Les 2 deniers éléments sont: {' '.join(la_ptiote_liste[-2:len(la_ptiote_liste):])}" )
print(f"La liste inversée est : {' '.join(la_ptiote_liste[::-1])}")

#List comprehension
nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nombres_pairs = [nombre for nombre in nombres if nombre % 2 == 0]
print("Les nombres pair entre 1 et 10:", nombres_pairs)


la_ptiote_liste.append("Ciao")

# C'est case sensitive
la_ptiote_liste.remove("Coucou")
del la_ptiote_liste[0]

print(f"La premiere occurence de Ciao est a la position : {la_ptiote_liste.index("Ciao")}")
print(f"Le nombre de Ciao dans la liste  : {la_ptiote_liste.count("Ciao")}")

print(la_ptiote_liste)

# Tuples
tuple1 = (1,2,3)
tuple2 = tuple((1,2,3))
tuple3 = tuple(la_ptiote_liste)
print("Je suis un tuple", tuple3)

# SET
set1 = {1,2,3}

# Dictionnaires

dict1 = {"Test":1,"Prout":2,"Type":"Zobi La Mouche",3:"Elephant"}

print(dict1)

dict_voitures = {"Marque": "Renault", "Modele": "Clio", "Plaque": "1-CLB614", "Puissance": 105}
print(dict_voitures)
dict_voitures[3] = "2-RDR232"
print("Nouvelle plaque : " + dict_voitures[3])
