from J8_Exo1 import Person
class Employee(Person):
    def __init__(self,prenom,age,annif, salary):
        self.__salary = salary
        super().__init__(prenom,age,annif)

    def get_salary(self):
        return self.__salary

    def get_anual_salary(self):
        return 12 * self.__salary

eric = Employee("eric", 25,"12/12/2012", 2500)
eric.bonjour_prenom()
print(f"Le salaire annuel de {eric.get_prenom()} est de : {eric.get_anual_salary()}")
