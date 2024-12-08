import tkinter as tk
from tkinter import messagebox

def calculer_age_100_ans():
    try:
        # Récupérer les entrées utilisateur
        nom_utilisateur = entry_nom.get().strip()
        age_utilisateur = int(entry_age.get().strip())
        annee_actuelle = int(entry_annee.get().strip())

        if not nom_utilisateur:
            raise ValueError("Le nom ne peut pas être vide.")
        if age_utilisateur <= 0:
            raise ValueError("L'âge doit être un nombre positif.")
        if annee_actuelle <= 0:
            raise ValueError("L'année doit être un nombre positif.")

        # Calculer l'année où l'utilisateur aura 100 ans
        annee_100_ans = annee_actuelle + (100 - age_utilisateur)

        # Afficher le résultat
        messagebox.showinfo("Résultat", f"{nom_utilisateur}, vous atteindrez 100 ans en {annee_100_ans}.")
    except ValueError as e:
        # Gérer les erreurs
        messagebox.showerror("Erreur", f"Erreur dans les saisies : {e}")

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Calcul de l'âge à 100 ans")

# Dimensions de la fenêtre
fenetre.geometry("400x300")
fenetre.resizable(False, False)

# Titre principal
titre = tk.Label(fenetre, text="Bienvenue !", font=("Arial", 16))
titre.pack(pady=10)

# Nom
label_nom = tk.Label(fenetre, text="Votre nom :")
label_nom.pack(pady=5)
entry_nom = tk.Entry(fenetre, width=30)
entry_nom.pack(pady=5)

# Âge
label_age = tk.Label(fenetre, text="Votre âge :")
label_age.pack(pady=5)
entry_age = tk.Entry(fenetre, width=30)
entry_age.pack(pady=5)

# Année actuelle
label_annee = tk.Label(fenetre, text="Année actuelle :")
label_annee.pack(pady=5)
entry_annee = tk.Entry(fenetre, width=30)
entry_annee.pack(pady=5)

# Bouton pour calculer
bouton_calculer = tk.Button(fenetre, text="Calculer", command=calculer_age_100_ans, bg="blue", fg="white")
bouton_calculer.pack(pady=20)

# Lancer la fenêtre
fenetre.mainloop()