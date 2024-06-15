################################################
# PRÉSENTATION ET UTILISATION DES TUPLES:      #
#               Alex LAMIZANA 10/09/2021.      # 
################################################


# Le tuple est comme la liste, à ceci prêt qu'il est immuable:
# on ne peux pas rajouter ou enlever des éléments.

# Création d'un tuple:
dimension = (200, 50)             # ATTENTION: le tuple est entre parenthèse:

print("dimension d'origines:")
print(dimension[0])
print(dimension[1])

dimension = (400, 100)            # On assigne des nouvelles valeurs à notre tuple:
print("dimension modifièes:")
for i in dimension:
    print(i)


# ---------------------------------------------------------------
# (4.13) Créer un tuple et le modifier:
tuple_plats = ("riz", "pates", "avocat", "endives", "salade")

# Afficher les plats du restaurant:
print("Voici la liste de plats:")
for i in tuple_plats:
    print(i.title())               # tittle() met les majuscules initiales:

# Modifier le tuple en changeant 2 plat:
tuple_plats = ("riz", "soupe", "avocat", "ragout", "salade")
print("Voici la nouvelle liste de plats:")
for i in tuple_plats:
    print(i.title())