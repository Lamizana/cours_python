# ------------------------------------------------- #
# DICTIONNAIRES                                     #
# Alex LAMIZANA      15/09/2021.                    #
# ------------------------------------------------- #

# Il est entre des accolades {}.
# Un dictionnaire est un ensemble de couples clé-valeur.
# Le dictionnaire étant dynamique,on peut ajouter des couples clé-valeurs.


# -----------------------------------------------------------------------------
# Dictionnaire simple:

# Création d'un dictionnaire.
# Respecter la syntaxe (accolade et guillemets):
alien_0 = {"color": "vert", "points": 5}
print(alien_0)

# on affiche les valeurs de l'appel:
print(f"L'alien est {alien_0['color']}")
print(alien_0["points"])


# -----------------------------------------------------------------------------
# Rajout de couples clé-valeur:
print("\n--Rajout de couples clé-valeur:--")

# dictionnaire initial:
alien_0 = {"color": "vert", "points": 5}

alien_0["x_position"] = 0              # Rajout clé-valeur position X:
alien_0["y_position"] = 25             # Rajout clé-valeur position y:

# Affichage en brut:
print(alien_0)

# Appel une valeur précise du dictionnaire:
print(alien_0["y_position"])


# -----------------------------------------------------------------------------
# COMMENCER AVEC UN DICTIONNAIRE VIDE:
print("\n--Ajout de clé-valeur dans un dictionnaire vide--")

alien_1 = {}                        # dictionnaire vide.

alien_1["color"] = "rouge"          # Rajout clé-valeur position X:
alien_1["points"] = 10              # Rajout clé-valeur position y:

print(alien_1) 


# -----------------------------------------------------------------------------
# MODIFIER DES VALEURS DANS UN DICTIONNAIRE:
print("\n--Modification de valeur dans un dictionnaire--")

# Liste avant modification:
alien_0 = {'color': 'vert'}
print(f"Cet alien est de couleur {alien_0['color']}")

# Modification de la valeur associé à la clé:
alien_0['color'] = "jaune"                     # ATTENTION SYNTAXE (crochet).

print(f"Cet alien est maintenant {alien_0['color']}")


# -----------------------------------------------------------------------------
# SUPPRIMER DES COUPLES CLE-VALEUR (instruction "del"):
# ATTENTION: opération définitive.
print("\n--Suppression de couple clé-valeur avec del--")

# Liste initial:
alien_0 = {"color": "vert", "points": 5}
print(alien_0)

# Supprime la clé "points" ainsi que sa valeur associé:
del alien_0["points"]
print(alien_0)

# Supprime le couple clé-valeur "color":
del alien_0["color"]
print(alien_0)


# -----------------------------------------------------------------------------
# DICTIONNAIRE D'OBJET SIMILAIRE:
# Permet de stocker un même type d'information sur différents objets (sondage).
print("\n--Objets similaires--")

# Création de la liste avec objets similaires(attention indentation):
langage_favoris = {'jean': 'python',
                   'sarah': 'c',
                   'denis': 'ruby',
                   'marc': 'javasript'}

print(langage_favoris)

# Création variable avec la clé "sarah" (en majuscule initiale):
langage = langage_favoris['sarah'].title()

# On affiche sa valeur:
print(f"Le langage favoris de Sarah est {langage}.")
# Peut aussi s'écrire:
print(f"Le langage favoris de Sarah est {langage_favoris['sarah'].title()}.")


# -----------------------------------------------------------------------------
# UTILISER GET() POUR ACCEDER AU VALEURS:
print("\n--Accéder aux valeurs avec get()--")

alien_0 = {'color': 'vert', 'speed': 'lente'}

# Get() requiert 2 clés comme argument, le seconde permet d'indiquer la valeur
# à renvoyer si la clé n'existe pas:
points_value = alien_0.get('points','Aucune valeur en points définie.')

print(points_value)