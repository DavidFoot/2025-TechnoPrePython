# db.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Définir la base de données et l'URL de connexion
DATABASE_URL = "postgresql://odoo:myodoo@localhost:5432/biblio"

# Créer une instance de moteur SQLAlchemy
engine = create_engine(DATABASE_URL)

# Créer une classe de base pour les modèles
Base = declarative_base()

# Créer une session
Session = sessionmaker(bind=engine)

# Fonction pour obtenir la session de base de données
def get_session():
    return Session()