name = "David"
age = 42
increment = 1
futurAge = age + increment
objet = "Monster Hunter"
print(f"Hello World : {name} et pouf bientot {age+1} ans")
print("Bonjour", name, "tu as", age, "ans")
print("Coucou " + name + " tu as " + str(age) + " ans" + " et tu joues encore a " + objet)
print(age * 2)
print(futurAge)

# Test de conversion
n1 = 40
n2 = 1
test = n1 + n2
test2 = str(n1) + str(n2)
print(test)
print(test2)

# Test de conversion
n1 = "40"
n2 = "1"
test = n1 + n2
test2 = int(n1) + int(n2)
print(test)
print(test2)


# Petit Exo

lit1 = "Ciel"
lit2 = "bleue"
print(lit1 + " " + lit2)
nbr1 = 5
nbr2 = 4
print(nbr1 + nbr2)


# Résumé

print( 1 + 1 )
print("1" + "1")
# print (1 + "1")  Erreur TypeMissmatch/ ValueError
print(1 + int("1"))
# print( 1 + int("Bonjour")) Erreur TypeMissmatch/ValuError


