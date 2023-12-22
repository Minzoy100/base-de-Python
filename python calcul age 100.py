# On demande le nom de notre utilisateur
nom_utilisateur = input("Quel est votre nom ? ")

# On l'accueil (pour ajouter un peu d'intéraction)
print(f"Bonjour, {nom_utilisateur}!")

# On demande cette fois-ci l'âge de l'utilisateur
age_utilisateur = int(input("Quel est votre âge ? "))

# On demande l'année pour ne pas que le code devienne obsolète
année = int(input("En quelle année somme nous ? "))

# Code à debug : faire en sorte de vérifié si il s'agit bien d'un numéro, il n'est pas possible de mettre de nombre a virgule

# Et on calcul en quelle année il va avoir 100ans
annee_100_ans = année + (100 - age_utilisateur)

# Et on donne l'année a la quelle l'utilisateur va avoir 100ans
print(f"Vous atteindrez 100 ans en {annee_100_ans}.")
