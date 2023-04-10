from tkinter import *

import customtkinter
import sqlite3


customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("dark-blue")


def login():
    # Connexion à la base de données
    conn = sqlite3.connect('discord.db')
    cursor = conn.cursor()

    # Récupération de l'email et du mot de passe
    email = entree1.get()
    password = entree2.get()

    # Vérification de l'email et du mot de passe dans la base de données
    cursor.execute("SELECT * FROM utilisateurs WHERE email = ? AND motdepasse = ?", (email, password))
    result = cursor.fetchone()

    if result:
        # Si l'utilisateur est trouvé, afficher un message de succès
        connexion_reussie()
    else:
        # Sinon, afficher un message d'erreur
        demande_inscription()

    # Fermeture de la connexion à la base de données
    conn.close()


def connexion_reussie():
    for widget in root.winfo_children():
        widget.destroy()


def demande_inscription():
    for widget in root.winfo_children():
        widget.destroy()

    frame = customtkinter.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill="both", expand=True)
    label = customtkinter.CTkLabel(master=frame, text="Inscription System")
    label.pack(pady=12, padx=10)
    inscription1 = customtkinter.CTkEntry(master=frame, placeholder_text="nom")
    inscription1.pack(pady=12, padx=10)
    inscription2 = customtkinter.CTkEntry(master=frame, placeholder_text="prenom")
    inscription2.pack(pady=12, padx=10)
    inscription3 = customtkinter.CTkEntry(master=frame, placeholder_text="Email")
    inscription3.pack(pady=12, padx=10)
    inscription4 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
    inscription4.pack(pady=12, padx=10)
    inscription5 = customtkinter.CTkEntry(master=frame, placeholder_text="Confirmer le Password", show="*")
    inscription5.pack(pady=12, padx=10)
    button_inscription = customtkinter.CTkButton(master=frame, text="Inscription", command=lambda: inscription(inscription1.get(), inscription2.get(), inscription3.get(), inscription4.get(), inscription5.get()))
    button_inscription.pack(pady=12, padx=10)


def inscription(nom, prenom, email, mdp1, mdp2):
    if mdp1 == mdp2 and len(mdp1) != 0:
        if len(prenom) != 0 and len(email) != 0 and len(nom) != 0:
            conn = sqlite3.connect('discord.db')
            cursor = conn.cursor()
            cursor.execute("SELECT email FROM utilisateurs WHERE email = ?", (email,))
            result = cursor.fetchone()
            if result:
                print("L'email existe déjà, veuillez vous connecter")
            else:
                conn = sqlite3.connect('discord.db')
                cursor = conn.cursor()
                values = (nom, prenom, email, mdp1)
                cursor.execute("INSERT INTO utilisateurs (nom, prenom, email, motdepasse) VALUES (?, ?, ?, ?)", values)
                conn.commit()
                print("Inscription Réussie")
                # Fermer la connexion à la base de données
                conn.close()
        else:
            print("Veuillez entrer tous les informations nécessaire")
    else:
        print("Veuillez entrer le même mot de passe")


# Création de l'interface graphique
root = customtkinter.CTk()
root.geometry('600x800')
with open("discord.png", "rb") as f:
    img_data = f.read()

# Conversion des données de l'image en un objet Tkinter
photo = PhotoImage(data=img_data)
photo = photo.subsample(4)
# Création d'un widget Label pour afficher l'image
label = Label(root, image=photo)
label.pack()
# Affichage des differents elements de la fenetre
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Login System")
label.pack(pady=12, padx=10)

entree1 = customtkinter.CTkEntry(master=frame, placeholder_text="Email")
entree1.pack(pady=12, padx=10)
entree2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
entree2.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Login", command=login)
button.pack(pady=12, padx=10)

checkbox = customtkinter.CTkCheckBox(master=frame, text="Se Rappeler")
checkbox.pack(pady=12, padx=10)
button2 = customtkinter.CTkButton(master=frame, text="Inscription", command=demande_inscription)
button2.pack(pady=12, padx=10)

root.mainloop()
