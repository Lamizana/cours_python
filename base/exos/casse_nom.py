# cours/base/exos/casse_nom.py
###############################################################################
# Exercices: 2.3 à 2.7  source:"Petite lecon de python"                       #
# Gestion de la casse avec une chaine de caractères.         - 15/juin/2024 - #
###############################################################################

###############################################################################
# Exos 2-3: Messages personnel.
"""
Utiliser une variable pour representer le nom d'une personne et l'afficher.
Le msg doit etre: "Bonjour <name>, voudrais-tu apprendre un peu de python?"
"""
print("---------------------------------------------------------------------")
print("Exos 2-3: Message personnel.")

name = "Alex"
message = f"Bonjour {name}, voudrais-tu apprendre un peu de python?"
print(message)
print("---------------------------------------------------------------------")

###############################################################################
# Exos 2-4: Casse d'un nom.
"""
- Utiliser une variable pour representer le nom d'une personne.
- Afficher le nom:
    - En majuscule
    - En minuscule.
    - En majuscule initial.
"""
print("---------------------------------------------------------------------")
print("Exos 2-4: Casse d'un nom.")

name = "alex"
print(f"Nom en minuscule: {name.lower()}.")
print(f"Nom en majuscule: {name.upper()}.")
print(f"Nom en majuscule initiale: {name.title()}.")
print("---------------------------------------------------------------------")

###############################################################################
# Exos 2-5:Célèbre citation.
"""
Touver une citation d'une personne célèbre.
- L'afficher ainsi que le nom de l'auteur.
- La sortie doit ressembler à ca:
    - Albert Einstein a dit "Qui n'a jamais fait d'erreur n'a jamais rien essayer de nouveau..."
"""
print("---------------------------------------------------------------------")
print("Exos 2-5: Célèbre citation.")

name = "Mere Theresa"
citation = " La vie est une opportunité, profitez-en. \nLa vie est belle, admirez la. \nLa vie est un rêve, réalisez-la. \nLa vie est un devoir, complètez-la. \nLa vie est un jeu, jouez-la."

print(f'{name} a dit "{citation}"')
print("---------------------------------------------------------------------")

###############################################################################
# Exos 2-7 Supprimer des espaces dans un nom.
"""
Utiliser une variable pour représenter le nom d'une personne avec des espace au début et à la fin du nom.
- Utiliser chaque combinaison de caractères: "\t" et "\n" au moins une fois.
- Afficher le nom une fois, de sorte que les espaces avant et après soient visibles.
- Afficher le nom en utilisant chacune des 3 fonctions de suppression:
    - lstrip(): Supprime les espaces à gauche.
    - rstrip(): Supprime les espaces à droite.
    - strip(): Supprime les espaces à gauche et à droite.
"""
print("---------------------------------------------------------------------")
print("Exos 2-7: Supprimer des espaces dans un nom.")

name = "  \t \n Alex  \n\t"
print(f"Nom initial (avec espaces): {name} .")
print(f"Nom sans espace à gauche: {name.lstrip()} .")
print(f"Nom sans espace à droite: {name.rstrip()} .")
print(f"Nom sans espace: {name.strip()} .")
print("---------------------------------------------------------------------")
