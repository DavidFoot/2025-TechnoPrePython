import book
import Library
import os

def newbook(titre="", auteur="", annee=0):
    if titre == "" and auteur == "" and annee == 0:
        titre = askstring("Quel est le titre: ")
        auteur = askstring("Quel est l'auteur du livre: ")
        annee = askint("Quel est l'année de parution: ")
    currentbook = book.Book(titre,auteur,annee)
    return  currentbook

def askstring(question):
    response = ""
    while response == "":
        response = input(question)
        if response == "":
            print("Vous devez rentrer une valeur correcte, veuillez recommencer !")
    return response

def askint(question):
    response = ""
    while response == "" :
        try:
            response = int(input(question))
        except ValueError:
            response = ""
            print("Veuillez recommencer en entrant une valeur entiere correcte !")
    return response

def clear_screen():
    os.system('cls')

def prompt_before_menu():
    input("Appuyez sur une touche pour revenir au menu principal")

def displaymainmenu():
    clear_screen()
    choice = 0
    while choice == 0 :
        print("Que voulez-vous faire : ")
        print("1: Voir la liste des livres disponibles ")
        print("2: Rendre un livre emprunté")
        print("3: Emprunter un livre")
        print("4: Ajouter un nouveau  livre")
        print("5: Quitter le programme")
        try:
            choice = int(input("Votre choix : "))
        except ValueError:
            choice = 0
            displaymainmenu()
        if choice == 4 :
            clear_screen()
            myLibrary.addbook(newbook())
            prompt_before_menu()
        if choice == 5 :
            exit()
        if choice == 1 :
            clear_screen()
            myLibrary.displayavailablebooks()
            prompt_before_menu()
        if choice == 2 :
            clear_screen()
            myLibrary.display_gone_books()
            myLibrary.return_gone_book()
            prompt_before_menu()
        if choice == 3 :
            clear_screen()
            myLibrary.displayavailablebooks()
            myLibrary.take_a_book()
            prompt_before_menu()

        displaymainmenu()


# Initialisation

myLibrary = Library.Library()
myLibrary.addbook(newbook("Toto","Tata", 1983))
myLibrary.addbook(newbook("Dada","PaPa", 1998))
myLibrary.addbook(newbook("Zozo","LoLo", 1990))


displaymainmenu()



