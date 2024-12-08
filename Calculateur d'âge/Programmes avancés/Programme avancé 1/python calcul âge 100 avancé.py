def main():
    # On demande le nom de l'utilisateur.
    nom_utilisateur = input("Quel est votre nom ? ").strip()
    if not nom_utilisateur:
        print("Vous n'avez pas saisi de nom. Veuillez réessayer.")
        return

    # # On l'accueil pour ajouter un peu d'intéraction.
    print(f"Bonjour, {nom_utilisateur}!")

    try:
        # On demande l'âge de l'utilisateur.
        age_utilisateur = int(input("Quel est votre âge ? "))
        if age_utilisateur <= 0:
            print("L'âge doit être un nombre positif. Veuillez réessayer.")
            return
    except ValueError:
        print("Veuillez entrer un nombre valide pour votre âge.")
        return

    try:
        # On demande l'année pour ne pas que le code devienne obsolète
        annee_actuelle = int(input("En quelle année sommes-nous ? "))
        if annee_actuelle <= 0:
            print("L'année doit être un nombre positif. Veuillez réessayer.")
            return
    except ValueError:
        print("Veuillez entrer une année valide.")
        return

    # On calcul en quelle année il va avoir 100ans
    annee_100_ans = annee_actuelle + (100 - age_utilisateur)

    # On donne l'année a la quelle l'utilisateur va avoir 100ans.
    print(f"{nom_utilisateur}, vous atteindrez 100 ans en {annee_100_ans}.")

if __name__ == "__main__":
    main()