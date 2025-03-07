# models.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db import Base

"""
Classe Client
Créez une classe Client qui représente un emprunteur :
id (entier) : identifiant unique du client (généré par la base de données).
nom (chaîne de caractères) : nom du client.
email (chaîne de caractères) : email du client.
telephone (chaîne de caractères) : numéro de téléphone du client.
Ajoutez un constructeur pour initialiser ces attributs.
Ajoutez une méthode afficher_info() qui retourne les informations du client.
"""

class Client(Base):
    __tablename__ = 'clients'

    id_client = Column(Integer, primary_key=True)
    c_nom = Column(String, nullable=False)
    c_prenom  = Column(String, nullable=False)
    c_localite  = Column(String, nullable=False)
    c_email = Column(String, nullable=False, unique=True)
    c_telephone  = Column(String, nullable=True)

    def __repr__(self):
        return f"{self.c_nom} {self.c_prenom} {self.c_localite} {self.c_email} {self.c_telephone}"
