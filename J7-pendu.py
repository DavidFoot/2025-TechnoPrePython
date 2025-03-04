from randomwordfr import *
from unidecode import unidecode

class DuplicateError(LookupError):
    pass
class NotCharacter(LookupError):
    pass

def validate_input(input_word, already_played):
    if not len(input_word) == 1 or not input_word.isalpha():
        raise NotCharacter()
    if input_word in already_played:
        raise DuplicateError()
    return input_word,True

def get_random_fr_word(min_length, max_length):
    while True:
        w = RandomWordFr().get()["word"]
        if min_length <=  len(w) <= max_length:
            return w

def check_word(word,already_played, propal=''):
    word_to_display = ""
    already_played.append(propal)
    for i in range(0,len(word)):
        if word[i].lower() in already_played or not word[i].isalpha() :
            word_to_display += word[i]
        else:
            word_to_display += '*'
    if propal == '' or propal in word.lower():
        lose_life = False
    else:
        lose_life = True
    return word_to_display, lose_life


min_word_lenght = 10
max_word_lenght = 15
current_life = max_life = 60
proposition = ''
char_already_played = []
x = unidecode(get_random_fr_word(10,15).lower())
print("Bienvenue dans le jeu du pendu !")
print(f"Vous disposez de {max_life} essais pour trouver un mot")
while True:
    returned_word_check = check_word(x,char_already_played,proposition)
    if returned_word_check[0] == x :
        print(f"Bravo, tu as trouvé le mot \"{x}\" avant d'être pendu, a +")
        break
    if returned_word_check[1]:
        current_life -= 1
        if current_life <= 0:
            print(f"Tu as perdu, le mot à trouver était : {x}")
            break
        print(f"Nope, y'a pas cette lettre dans le mot, il te reste {current_life} essais")
    print("=> " + returned_word_check[0])
    proposition = ''
    returned_check = ('',False)
    while not returned_check[1]:
        try:
            returned_check = validate_input(input(f"Quelle lettre voulez vous proposer ({current_life} essais restant) ? "), char_already_played)
        except NotCharacter:
            print("On a demandé une lettre...pas un faceroll sur le clavier")
        except DuplicateError:
            print("Lettre deja proposée")
        proposition = returned_check[0]
