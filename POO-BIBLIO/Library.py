import book
class Library :
    def __init__(self):
        self.bookavailable = []
        self.book_unavailable = []

    def addbook(self, book_item: book.Book):
        self.bookavailable.append(book_item)

    def displayavailablebooks(self):
        i=0
        if not self.bookavailable:
            print("Aucun livre de disponible")
        else:
            print("Nombre de Livres : " + str(len(self.bookavailable)))
            for book_item in self.bookavailable:
                i+=1
                book_item: book.Book
                print(f"{i}: " + str(book_item))

    def display_gone_books(self):
        if not self.book_unavailable:
            print("Aucun livre a rendre actuellement")
        else:
            i = 0
            print("Nombre de Livres : " + str(len(self.book_unavailable)))
            for book_item in self.book_unavailable:
                book_item: book.Book
                i+=1
                print(f"{i}: " + str(book_item))

    def return_gone_book(self):
        if len(self.book_unavailable) > 0 :
            choice = 0
            while choice == 0 :
                try:
                    choice = int(input("Entrez le numero de livre a rendre parmi la liste: "))
                except ValueError:
                    choice = "quit"
                    continue
                if choice-1 not in range(len(self.book_unavailable)):
                    choice = 0
                    print("Valeur incorrecte, numero non reconnu")
                else:
                    self.bookavailable.append(self.book_unavailable.pop(choice-1))

    def take_a_book(self):
        if len(self.bookavailable) > 0 :
            choice = 0
            while choice == 0 :
                try:
                    choice = int(input("Entrez le numero du livre que vous désirez emprunter: "))
                except ValueError:
                    choice = "quit"
                    continue
                if choice-1 not in range(len(self.bookavailable)):
                    print("Valeur incorrecte, numero non reconnu")
                else:
                    self.book_unavailable.append(self.bookavailable.pop(choice-1))
                    print("Merci d'emprunter le livre, n'oubliez pas de venir le restituer")