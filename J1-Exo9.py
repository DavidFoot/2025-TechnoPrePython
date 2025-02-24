"""
Mélangeur de mots
Demande trois mots à l’utilisateur.
Affiche-les dans un ordre aléatoire ou avec un effet rigolo :
Exemple 1 : Répète chaque mot deux fois : "chat chat chien chien souris souris".
Exemple 2 : Affiche-les en majuscules inversées : "TAHC NEIHC SIURIS" """
from ntpath import split

from random import shuffle

def MuliplyEachItem(list,x):
    listCopy = []
    for item in list:
        for i in range(0,x):
            listCopy.append(item)
    return listCopy

def UpperRevertStringJoined(myList):
    listCopy = []
    for item in myList:
        listCopy.append(''.join(reversed((item).upper())))
    return listCopy

wordList = []
for i in range(0,3):
    wordList.append(input(f"Entrez le mot {i+1}: "))
shuffle(wordList)
print(wordList)
print(MuliplyEachItem(wordList,5))
[print(x,end="-") for x in wordList]
print()
#[print(x,end="-") for x in UpperRevertStringJoined(wordList)]
[print(x[::-1].upper(),sep=' ',end='') for x in wordList]




