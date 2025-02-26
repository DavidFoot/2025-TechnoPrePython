class Book :
     def __init__(self,bname, bauthor, bparutiondate):
         self.bname = bname
         self.bauthor = bauthor
         self.bparutiondate = bparutiondate

     def __str__(self):
        return f"Titre: {self.bname} Auteur: {self.bauthor} Parution: {self.bparutiondate}"
