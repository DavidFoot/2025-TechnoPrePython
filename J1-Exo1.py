yourAge = 0
while yourAge == 0:
    try:
        yourAge = int(input("Quel est votre année de naissance ? : "))
    except ValueError :
        print("La valeur entrée est incorrecte")
        yourAge = 0
alreadyGetBirthdayThisYear = False
getCorrectAnswer = False
while not getCorrectAnswer :
    answer = input("Avez vous deja eu votre anniversaire cette année (oui/non) : ").lower()
    if answer == "oui" :
        alreadyGetBirthdayThisYear = True
        getCorrectAnswer = True
    elif answer == "non" :
        alreadyGetBirthdayThisYear = False
        getCorrectAnswer = True
    else:
        print("Veuillez répondre correctement à la question...")
        getCorrectAnswer = False
currentYear = 2025
currentAge = currentYear - yourAge
if not alreadyGetBirthdayThisYear :
    currentAge-=1
print(f"Votre age actuel doit etre de {currentAge}")
