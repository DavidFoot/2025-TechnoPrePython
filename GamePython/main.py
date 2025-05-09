import os
import random
import unicodedata
import sys
from termcolor import colored

def clear_screen():
    if 'win' in sys.platform:
        os.system('cls')
    else:
        os.system('clear')

def strip_accents(s):
   return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')

def verify_proposition(proposition,word_to_find ):

    word_to_find = list(word_to_find)
    current_word_state = word_to_find.copy()
    for i in range(len(word_to_find)):
        if i == 0:
            current_word_state[i] = colored(word_to_find[i], 'red')
            word_to_find[i] = '.'
        elif proposition and word_to_find[i] == proposition[i]:
            current_word_state[i] = colored(proposition[i], 'red')
            word_to_find[i] = '.'
        elif len(proposition) == len(word_to_find):
            current_word_state[i] = proposition[i]
        else:
            current_word_state[i] = '*'
    for i in range(len(word_to_find)):
        if  i != 0 and proposition :
            index = ''.join(word_to_find).find(proposition[i])
            if index >=0:
                current_word_state[i] = colored(proposition[i], 'yellow')
                word_to_find[index] = '.'
    return ''.join(current_word_state)

# Example string
clear_screen()
print(f"On va essayer de faire un {colored("Motus",'red')} {colored("Motus",'yellow')}")
mots_francais = [
    "amour", "bonté", "courage", "dévotion", "étoile", "famille", "grâce", "honneur", "idée", "joie",
    "kilos", "légende", "merveille", "nuage", "opinion", "paix", "quête", "rêve", "saison", "tendresse",
    "unité", "victoire", "wouah", "xylophone", "yoga", "zénith", "ami", "bleu", "chat", "doute", "énergie",
    "fleur", "générosité", "horizon", "innovation", "jouer", "kermesse", "lumière", "magie", "nourriture",
    "oublier", "plage", "quitter", "réussir", "soleil", "toujours", "univers", "village", "voix", "yonder",
    "zoo", "arc", "bonté", "chaleur", "dévotion", "éclat", "fragile", "grâce", "herbe", "idée", "jardin",
    "kinder", "légende", "même", "noir", "observation", "poids", "question", "répondre", "silence", "temps",
    "utile", "violon", "weekend", "xénon", "yoga", "zone", "allumer", "brise", "cerise", "détente", "élan",
    "facile", "granit", "heureux", "ilôt", "jambe", "kilo", "léger", "moisson", "nuit", "œuvre", "plume",
    "quarantaine", "réflexion", "savon", "toit", "utiliser", "vraiment", "voler", "wok", "xenophile", "zéro",
    "abondance", "beauté", "calme", "douceur", "espoir", "flamme", "gratitude", "harmony", "irrésistible",
    "joie", "klaxon", "lisse", "mélange", "nuage", "oracle", "patience", "quiche", "risque", "semaine", "temps",
    "utile", "vision", "éternité", "xylophone", "yogourt", "zodiaque", "aborder", "bénéfice", "courir", "dépôt",
    "étoile", "fée", "garde", "harpe", "innocence", "jour", "kinder", "liberté", "monde", "néon", "océan",
    "partager", "quai", "rire", "savoir", "temps", "usine", "voler", "waterloo", "xénon", "yogi", "zodiaque",
    "avion", "brise", "ciel", "détour", "éclat", "fin", "génial", "horizon", "illusion", "joli", "kaléidoscope",
    "lueur", "métier", "nébuleuse", "outil", "paradis", "quartier", "revue", "sieste", "téléphone", "utilisation",
    "vif", "voyage", "wagon", "xenon", "yogiste", "zebre", "adresse", "bande", "champ", "délire", "elle", "flotte",
    "garçon", "herbe", "image", "jaune", "kiwi", "légende", "magnifique", "nez", "oiseau", "plage", "quitter",
    "rester", "solaire", "télé", "unique", "voir", "vaisseau", "xenodochial", "yogis", "zone", "aile", "bougie",
    "collier", "demander", "escargot", "famille", "gâteau", "hôte", "insister", "jouer", "kiwi", "lune", "maison",
    "nouvelle", "oeil", "pain", "quitter", "repasser", "semaine", "tendresse", "unité", "vendre", "wok", "xénon",
    "zazou", "abattre", "banane", "champion", "danser", "éclater", "fier", "gagner", "harmonie", "inspirer", "jouer",
    "kermesse", "lire", "montrer", "nez", "océan", "plaisir", "quitter", "réussir", "sieste", "tendre", "union",
    "vérité", "vitesse", "worm", "xenon", "yann", "zoothérapie", "apprécier", "battre", "courir", "détendre", "énigme",
    "flotter", "gagner", "houle", "idée", "jeter", "kilos", "lire", "mouvement", "naviguer", "ouvrir", "passion",
    "quitter", "risque", "sommeil", "tout", "utiliser", "voyage", "xénon", "yoga", "zoo", "automne", "battre", "chaos",
    "détente", "espace", "fantôme", "garde", "honneur", "inconnu", "jour", "klaxon", "lune", "magnifique", "neige",
    "offrir", "pouvoir", "quête", "rire", "semaine", "tendre", "unité", "vitesse", "wagon", "xenophobe", "yoga", "zéro"
]

pick_a_word = random.randrange(0,len(mots_francais))
word_to_find = strip_accents(mots_francais[pick_a_word].upper())
nbr_life = 10
char_already_found = {}
proposition = ""

print(verify_proposition('',word_to_find))
game_try = 1
placeholder=""
for i in range(len(word_to_find) - 1):
    placeholder += '*'
placeholder+='|'
while True:
    # ok j ajoute la premiere lettre du mot a touver avec le input de l utilisateur diminué de la premiere lettre

    #proposition = word_to_find[0]
    print(f"Essai {game_try}/{nbr_life} - Votre proposition: \n{word_to_find[0]}{placeholder}", end='\r')
    proposition = input()
    #print(f"Votre proposition: \n{word_to_find[0]}{pla}", end='\r')

    if len(proposition) != len(word_to_find) :
        print("C'est pas le meme nombre de caractere, recommencez")
        continue
    game_try+=1
    if proposition.upper() == word_to_find:
        print("Bravo Bravo, vous avez trouvé le mot recherché")
        break
    print(verify_proposition(proposition.upper(),word_to_find))
    if game_try >= nbr_life:
        print("Looser")
        print(f"Le mot a trouver etait : {word_to_find}")
        break
