# ------------------------------------------------- #
# PRÉSENTATION ET UTILISATION DES BOUCLES IF:       #
#               Alex LAMIZANA      13/09/2021.      #
# ------------------------------------------------- #

# INSTRUCTION IF: permet d'analyser l'état actuel d'un programme 
# et d'apporter une réponse en fonction de l'état:

# -----------------------------------------------------------------------------
# Exemple: En tant que concessionnaire, j'ai une liste de voitures 
# que je peux proposer au client:

# Ma variable correspond au nombres de voitures que je possède:
cars = ["audi", "bmw", "subaru", "toyota"]
print(cars)

# Je défile la liste ( i étant la valeur de ma variable):
for i in cars:
    # Vérifie si la valeur i est bmw:
    if i == "bmw":
        print(i.upper())       # Affiche BMW (en majuscule):
    # Sinon:
    else:
        print(i.title())       # Affiche le reste.
   
   
# -----------------------------------------------------------------------------
# Vérifier si une valeur est dans une liste:
print("\n--Vérifier si une valeur est dans une liste--")

ingredients = ["chamignons", "oignons", "ananas"]
# Mot-clé in:
if "oignons" in ingredients:
    print("Vrai")
else:
    print("Faux")

# --------------------------------------------------------------------------    
# Vérifier si une valeur n'est pas dans une liste:
ingredients = ["chamignons", "oignons", "ananas"]
# Mot-clé not in:
if "ananas" not in ingredients:
    print("il n'y a pas d'ananas dans la liste")
else:
    print("il ya de l'ananas dans la liste")


# -----------------------------------------------------------------------------
# Instruction "if" simple:
# Etre agé de plus de 18 ans pour pouvoir voter:
print("\n--Age pour voter--")

age = 19
# Si mon âge est supérieur ou égal a 18 alors:
if age >= 18:
    print(age >=18)
    print("Vous avez l'âge de voter.")


# -----------------------------------------------------------------------------
# Instruction if-else:
# Permet de définir une action ou séquence d'actions lorsque le test 
# conditionnel échoue:
print("\n--Age pour voter--")

age = 17
# Si mon âge est supérieur ou égal a 18 alors:
if age >= 18:
    print(age >= 18)                    # renvoie True.
    print("Vous avez l'âge de voter.")
# Sinon:
else:
    print(age >= 18)                    # renvoie False.
    print("Vous êtes encore mineur")
    

# -----------------------------------------------------------------------------
# Instruction if-elif-else:
print("\n--Instruction if-elif-else--")

print("Affiche les prix d'entrées du parc en fonction de l'âge:")
age = 12
if age < 4:
    print("le prix d'entrée est de 0 €.")
# Si age est compris entre 4 et 18:
elif 4 < age < 18:
    print("le prix d'entrée est de 25 €.")
else:
    print("le prix d'entrée est de 40 €.")
    
# Peux aussi s'écrire:
if age < 4:
    price = 0
elif 4 < age < 18:
    price = 25
else:
    price = 40
# On affiche le résultat:
print(f"Le prix d'entrée est de {price} €.")


# -----------------------------------------------------------------------------
# Tester plusieurs conditions (sans bloc if-elif-else):
print("\n--Tester plusieurs conditions--")

garnitures = ["champignons", "supplément de fromages"]

# Permet de vérifier chaque condition:
if garnitures[0] in garnitures:
    print("Ajout de champignons.")
if "supplément de fromages" in garnitures:
    print("Ajout de supplément de fromages.")
    
print("Votre pizza est prête.")


# -----------------------------------------------------------------------------
# Tester de conditions utilisant les mots-clé "and" et "or":
print("\nTest utilisant les mots-clé and et or:")

amis =["alex", "hervé", "benoit", "ben"]

# "and" permet de déterminer si 2 conditions sont vrais:
if "alex" in amis and "hervé" in amis:
    print("ce sont mes amis")

user_1 = "ALEX"
user_2 = "paul"

# On vérifie si user_1 est dans la liste:
# lower() met tout en minuscule.
if user_1.lower() in amis:
    print(f"{user_1.title()} est mon ami.")

# On vérifie si user_2 n'est pas dans la liste:
if user_2 not in amis:
    print(f"{user_2.title()} n'est pas mon ami.")

# "or" permet de vérifier si au moins une condition est vrai; alors true:
if user_1 or user_2 in amis:
    print("Au moins un des 2 est mon ami, true.")
    

# -----------------------------------------------------------------------------
# INSTRUCTION IF avec des listes:
print("\n--liste garniture--")

# création de la liste
garnitures_pizza =["champignons", "poivrons verts", "suppléments de fromages"]

# On boucle la liste et on affiche sa valeur:
for i in garnitures_pizza:
    print(f"Ajout de {i}")
print("Votre pizza est prète.")
    

# -----------------------------------------------------------------------------
# Vérifier qu'une liste n'est pas vide:
print("\n--liste garniture--")

garnitures_pizza = []

# renvoie true si la liste contient au moins 1 élément:
if garnitures_pizza:     
    for i in garnitures_pizza:
        print(f"Ajout de {i}")
    print("Votre pizza est prète.")
# sinon la liste est vide, renvoie false:
else:
    print("Voulez vous une pizza sans garnitures?")
    

# -----------------------------------------------------------------------------
# Utiliser plusieurs listes:
print("\n--liste inhabituel garniture--")   

garnitures_disponibles = ["champigons", "olives", "poivrons verts",
                          "pepperoni", "ananas", "fromages"]

garnitures_clients = ["champigons", "frites", "fromages"]

# on boucle sur la liste client:
for i in garnitures_clients:
    # si la garniture est dans la liste garniture_disponible:
    if i in garnitures_disponibles:
        print(f"Ajout de {i}")
    # sinon:   
    else:
        print(f"Désolé, nous n'avons plus de {i}")