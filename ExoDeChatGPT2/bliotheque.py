import tkinter as tk
from db import get_session
from models import Client



# Main interface Window

"""Ajouter un livre
Ajouter un client
Afficher les livres
Afficher les clients
Emprunter un livre
Retourner un livre
Historique des emprunts
"""



def clic_handler_ajout_client_in_db():
    # Ajout en base de donnée
    session = get_session()
    # Créer un client
    client = Client(c_nom=client_nom.get() , c_prenom=client_prenom.get() , c_localite=client_localite.get() , c_telephone=client_telephone.get() , c_email=client_mail.get())
    session.add(client)
    session.commit()
    print(f"Client ajouté : {client}")
    pass

def clic_handler_ajout_client():
    new_window = tk.Toplevel(main_window)
    new_window.title("Ajout Client")
    new_window.geometry("200x400")
    tk.Label(new_window, text="Nom du client : ").pack()
    tk.Entry(new_window, textvariable = client_nom).pack()
    tk.Label(new_window, text="Prenom du client : ").pack()
    tk.Entry(new_window, textvariable = client_prenom).pack()
    tk.Label(new_window, text="Localité du client : ").pack()
    tk.Entry(new_window, textvariable = client_localite).pack()
    tk.Label(new_window, text="Mail du client : ").pack()
    tk.Entry(new_window, textvariable=client_mail).pack()
    tk.Label(new_window, text="Telephone du client : ").pack()
    tk.Entry(new_window, textvariable=client_telephone ).pack()
    tk.Button(new_window, text="Enregistrer le client", command=lambda: clic_handler_ajout_client_in_db()).pack()

def clic_handler_ajout_livre():
    pass

main_window = tk.Tk(screenName="Bibliotheque",baseName="",useTk=True,className="Biblio" )
main_window.geometry('640x480')
main_window.resizable(False, False)

client_prenom = tk.StringVar()
client_nom = tk.StringVar()
client_localite  = tk.StringVar()
client_telephone = tk.StringVar()
client_mail = tk.StringVar()


button_ajouter_client = tk.Button(main_window, text="Ajouter un client", command=lambda:clic_handler_ajout_client())
button_ajouter_client.grid(row=0,column=0,ipadx=10, pady=2,padx=5)

button_ajouter_livre = tk.Button(main_window, text="Ajouter un livre", command=lambda:clic_handler_ajout_livre())
button_ajouter_livre.grid(row=0,column=1,ipadx=10, pady=2,padx=5)
# Machin brol qui loop
main_window.mainloop()