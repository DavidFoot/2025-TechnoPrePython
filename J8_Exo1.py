class Person:
    species = "Homo Geekus"
    def __init__(self, prenom, age, anniversaire):
        self.__prenom = prenom
        self.age = age
        self.anniversaire = anniversaire

    def bonjour_prenom(self):
        print(f"Bonjour {self.__prenom}")

    def is_majeur(self):
        if self.age >= 18 :
            print(f"{self.__prenom} est majeur")
        else:
            print(f"{self.__prenom} est mineur")

    def get_prenom(self):
        return self.__prenom

    @staticmethod
    def test_static_method():
        print("Je suis une methode de classe " + Person.species)

    def __str__(self):
        return f"Objet de type Person : prenom => {self.__prenom} "

david = Person("David", 40, "22/20/1982" )
jean = Person("Jean", 15, "22/20/2010" )
print(david)
print(jean.get_prenom() + " est de type : " + jean.species)
print(Person.species)
david.bonjour_prenom()
jean.bonjour_prenom()
david.is_majeur()
jean.is_majeur()

# Static function
Person.test_static_method()
