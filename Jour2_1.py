# on commence les boucles

#For Loop
print("Utilisation d'une boucle FOR")
MAXREPETITION = 5
for i in range(0,MAXREPETITION):
    print(f"{i+1} - Au revoir ")
print()
# While Loop
print("Utilisation d'une boucle WHILE")
REPETIONLIMITE = 7
cpt = 0
while cpt < REPETIONLIMITE :
    print("Hello")
    cpt+=1

# Using Continue

print("Utilisation d'une boucle WHILE avec un continue")
REPETIONLIMITE2 = 7
cpt2 = 0
while cpt2 < REPETIONLIMITE2 :
    cpt2 += 1
    if cpt2 == 4 or cpt2 == 6:
        continue
    print(f"{cpt2} - Hello")
