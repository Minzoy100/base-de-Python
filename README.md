 Salut, Aujourd’hui je vais vous montrer les bases du python avec un code pour calculer en quelle année quelqu’un aura 100 ans, tout vous sera expliqué dans les lignes après les #(les # sont des bouts de texte dans le code qui n’est pas exécuté, pour par exemple expliquer votre code ou simplement retiré des lignes de code pour tester votre code différemment.)
Ce code est disponible en fichier python dans ce repo.

 On demande le nom de notre utilisateur, "nom_utilisateur" est la valeur qu'on va donner 
(cette valeur n'est pas utile pour notre calcul juste pour rendre notre code un peu plus 
sympa), input définie une question (ou une entrée de valeur comme vous voulez) suivie de 
("") le ("") permet de mettre le texte avant la réponse, par exemple si on prend ça :
 ababa = input("Qui est tu ? ") quand le programme va être lancer on à ceci qui va
être affiché dans le terminal "Qui est tu ?" et après notre "?" on va pouvoirs saisir #du texte, texte qui va être "stocker" dans la valeur "ababa" ensuite on va pouvoirs réutilisé cette valeur dans la suite de notre programme
nom_utilisateur = input("Quel est votre nom ? ")

On l'accueil (pour ajouter un peu d'interaction) et c'est ici que notre valeur #précédemment nommé "ababa" va être utiliser car ici avec notre print (print #permet d'écrire du texte dans le terminale) on va pouvoirs affiché une valeur avec #le f un simple message dans le terminale peut être écrit comme ça #"print("Coucou")" cependant ici on à une valeur donc on va ajouter un f pour avoir #notre valeur.
print(f"Bonjour, {nom_utilisateur}!")

On demande cette fois-ci l'âge de l'utilisateur, cette valeur va être utile pour notre #calcul, on utilise notre int pour dire que la valeur est un nombre
age_utilisateur = int(input("Quel est votre âge ? "))

On demande l'année pour ne pas que le code devienne obsolète ou l'adapté a #n'importe quelle époque on utilise encore le int pour dire que notre valeur est un #nombre.
année = int(input("En quelle année somme nous ? "))


Et on calcul en quelle année il va avoir 100ans, avec un simple calcul, donc la on va dire que
notre valeur annee_100_ans est égal a l'année + l'âge - 100 de l'utilisateur
annee_100_ans = année + (100 - age_utilisateur)

Et on donne l'année a la quelle l'utilisateur va avoir 100ans dans le terminale
print(f"Vous atteindrez 100 ans en {annee_100_ans}.")
