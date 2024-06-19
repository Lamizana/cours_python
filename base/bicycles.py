# cours_python/base/bicycles.py
###############################################################################
# Présentation des listes.      source:"Petite lecon de python"               #
# Compréhesion et gestion de bases des listes.               - 19/juin/2024 - #
###############################################################################

# Initialisation et assignation d'une liste:
bicycles = ["treck", "cannondale", "redline", "bmx"]

# différents affichages:
'''
print(bycicles)                     # Renvoie la la représentation de la liste.
print(bycicles[0])                  # Affiche le premier éléments de la liste.
print(bycicles[1].title())          # Pareil mais avec la méthode title().
print(bycicles[2].upper())          # Pareil mais avec la méthode upper().
print(bycicles[-1])                 # Affiche le dernier éléments de la liste.
'''

print(bicycles)
print(bicycles[0].upper())

# ------------------------------------------------------------------------------
# Stocker des nom dans une liste:
potes = ["alex", "hugo", "benjamin", "yoann", "jack", "pierre"]
print(potes)
# on peut mettre plusieurs variable dans un print.           
print(potes[2].title(), potes[-1].title())                     

# Créer un msg avec le nom de chacun de mes potes:
msg_0 = f"Salutation {potes[0].title()}, comment vas-tu aujourd'hui?"
msg_1 = f"Salutation {potes[1].title()}, comment vas-tu aujourd'hui?"
msg_2 = f"Salutation {potes[2].title()}, comment vas-tu aujourd'hui?"
# on peut mettre des print à la suite avec ",".
print(msg_0), print(msg_1), print(msg_2)       

# Modifier un élément de la liste:
# remplace l'ancienne valeur à l'index 0 par "hervé" .                    
potes[0] = "hervé"                             
print(potes)

# Ajouter un élément à la fin de la liste :
print("\n--Append()--")
# Ajoute un pote dans la liste avec "append":
potes.append("nicolas")                         
print(potes)

# insérer un élément dans la liste:
print("\n--Insert()--")
# Marie est inséré à la position 2 avec "insert":
# cela décale les autres valeurs vers la droite.
potes.insert(2, "marie")                        
print(potes)                                  

# Supprimer définitivement les éléments d'une liste:
print("\n--Del--")
del potes[0]                        # Efface la valeur en position 0 avec "del":
print(potes)                        # supprime définitivement la valeur.

# Supprimer les éléments d'une liste avec pop():
print("\n--Pop()--")
popped_potes = potes.pop()      # Stocke la valeur supprimé dans une variable:
print(potes)                    # Affiche les valeurs sans la variable supprimé.
print(popped_potes)             # Affiche la valeur supprimé.  

# Supprimer des éléments à une position donnée:
popped_potes = potes.pop(3)     # Choisi et stocke la valeur supprimé.
print(potes)                    # Affiche les valeurs sans la variable supprimé 
print(popped_potes)             # Affiche la valeur supprimé.  

# Supprimer un élément par sa valeur avec remove():
print("\n--Remove()--")                 
potes.remove("jack")             # Supprime l'élément indiqué par sa valeur:
print(potes)                     # on peut stocker sa valeur comme pop().

# ------------------------------------------------------------------------------
# ORGANISER UNE LISTE.

# Trier définitivement une liste avec sort():
print("\n--Sort()--")   
potes.sort()                     # classe par ordre alphabétique: définitif.
print(potes)
# inverse l'ordre alphabétique avec l'argument revers=True:
potes.sort(reverse=True)                       
print(potes)

# Trier provisoirement une liste avec sorted():
print("\n--Sorted()--") 
# affiche la liste initial.
print(f"Voici la liste initial:, {potes}")  
# classe par ordre alphabétique: provisoire.            
print(f"Voici la liste final:, {sorted(potes)}")          

# Afficher une liste dans l'odre inverse avec reverse():
print("\n--Reverse()--") 
print(potes)
potes.reverse()                    # inverse définitivement l'odre de la liste.
print(potes)
potes.reverse()                    # inverse une seconde fois l'odre.
print(potes)

# Obtenir la longueur d'une liste avec len():
print("\n--len()--") 
print(len(potes))

# ------------------------------------------------------------------------------
# LISTE DE NOMBRES:

# Créer des statistiques simples avec une liste de nombres:
print("\n--Statistiques simples avec une liste de nombres--")
list_nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list_nombres)

# Affiche la valeur minimal de la liste:
print(f"Valeur minimal: {min(list_nombres)}")
# Affiche la valeur maximal de la liste:     
print(max(list_nombres))
# Affiche la somme des valeurs de la liste:                          
print(sum(list_nombres))                          

# ------------------------------------------------------------------------------
# MANIPULER UNE PARTIE DE LISTE:

# Créer une tranche de liste (slice):
print("\n--Tranche de liste (slice)--")
# Création de la liste:
players = ["charles","martine", "éric", "alex", "ito"] 

# Affichage des différents éléments de la liste:
# Affiche les 3 premier joueurs.
print(players[0:3])                      
# Sans le premier index, pyhton commence au début:
print(players[:4])
# Affiche les joueurs de 2(compris) à 5(non-compris):   
print(players[2:5])
# Affiche les joueurs à partir de l'index 3:                            
print(players[3:])
# Affiche les deux derniers joueurs.                              
print(players[-2:])                               

# Créer une boucle sur une tranche:
print("\n--Boucle sur une tranche--")
print(f"Voici les 3 premiers joueurs:")
# Éxecute la boucle sur les 3 premiers noms.
for i in players[:3]:                             
    print(i.title())

# Copier une liste avec slice:
print("\n--Copier une liste avec slice:--")
my_food = ["jambon", "riz", "fromage", "pizza"]   # Créer ma liste:

# La copier sur la liste amis (sans index, la liste est recopier entièrement):
friends_food = my_food[:]                       
print(f"Ma liste: {my_food}")                     # Affichage de ma liste.
print(f"Liste amis: {friends_food}")              # Affichage de la liste ami.

# Ajout d'un élément dans la liste.
friends_food.append("pâtes") 
# Affichage de la nouvelle liste ami.                    
print(f"Liste amis: {friends_food}")     
