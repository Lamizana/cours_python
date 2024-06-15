# ------------------------------------------------- #
# PRÉSENTATION ET UTILISATION DES BOUCLES FOR:      #
#               Alex LAMIZANA      08/09/2021.      #
# ------------------------------------------------- #



# Création de la liste:
magicians = ["majax", "alice", "david", "caroline"]

# Affichage en brut:
print(magicians)

# Affichage avec la boucle for:
for magician in magicians:              # Création de la variable temporaire magician:
    print(magician)                     # Affiche les valeurs de ma liste un par un.
    
for magician in magicians: 
    print(f"\n{magician.title()} vous êtes le meilleur!")     # Affiche les valeurs de ma liste dans un msg.
    print(f"Ce tour etait génial {magician.title()}.")        # Faire gaffe à l'indentation.

print("Merci a tous. C'était un super tour de magie.")        # Message après la boucle.


# -----------------------------------------------------------------------------------------------

# Fonction range():
print(f"\nFonction range():")
print("------------------")
for i in range (1, 6):                                        # Permet d'afficher un série de nombres (ici de 1 à 5):
    print(i)


# Créer un liste de nombres avec range():
nombres = list(range(1, 6))                                   # On stocke la liste dans la variable nombres:
print(nombres)                                                # Affichage de la liste en brut.


# Obtenir une liste des nombres pairs entre 1 et 10:
# Ajout  d'un troisième argument.
nombres_pairs = list(range(2, 11, 2))                         # la liste commence à 2, puis ajoute 2 à cet valeur (troisième argument):
print("\nObtenir une liste des nombres pairs entre 1 et 10:")
print(nombres_pairs)


# Créer une liste des 10 premiers nombres au carré:
# 2 asterisques (**) représente les exposants.
squares = []                                                  # Création de la liste vide:
for i in range(1, 11):                                        # Mise en place de la boucle (de 1 à 10):
    carre = i**2                                              # On met notre valeur au carré:
    squares.append(carre)                                     # On l'ajoute dans la liste.

print("\nAffichage des 10 premiers nombres au carré:")        # On est plus dans la boucle.
print(squares)                                                # Affichage des 10 premiers nombres au carré.

# Compréhension de liste:
# Combine boucle for et création d'éléments en une ligne.
squares =[i**2 for i in range(1, 11)]                         # Genère la même liste en une ligne de code:        
print(squares)


