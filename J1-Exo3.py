"""Conversion de Celsius en Fahrenheit
    Demander à l'utilisateur de saisir une température en degrés Celsius, puis afficher la conversion en Fahrenheit.
    Demander à l'utilisateur de saisir une température en degrés Fahrenheit, convertir cette température en Celsius,
    lui ajouter 5° et ensuite l'afficher."""

def AskFloat(question):
    isCorrectFloat = False
    value = 0
    while not isCorrectFloat:
        try:
            value = float(input(question))
        except ValueError:
            isCorrectFloat = False
            print("La valeur entrée n'est pas une valeur float correcte")
        else:
            isCorrectFloat = True
    return value

def ConversionCelcToFar(value):
    print("La temperature en °F : " + str(value * 1.8 + 32))

def ConversionFarToCelc(value):
    print("La temperature en °C : " + str((value - 32) / 1.8) )


ConversionCelcToFar(AskFloat("Veuillez introduire une temperature en °C: "))
ConversionFarToCelc(AskFloat("Veuillez introduire une temperature en °F : "))