############################################################
# PRÉSENTATION ET UTILISATION DES CHAINES DE CARACTÈRES:   #
#               Alex LAMIZANA 02/09/2021.                  # 
############################################################


# Affiche le nom utilisateur.
name = "alex Lamizana"
name = name.strip()     # supprime les espaces en trop.
print(f"Bonjour {name}, voudrais-tu apprendre un peu de python aujourd'hui?")

name = name.upper()     # Met le nom en majuscule (de facon définitif).
print(name)

name = name.lower()     # Met le nom en minuscule (de facon définitif).
print(name)

name = name.title()     # Met le nom en majuscule initiale (de facon définitif).
print(name)

# Affichage d'un texte avec prise en compte de apostrophes et des guillemets:
print('\tAlbert Einstein a dit: "Qui' " n'a jamais fait d'erreur n'a jamais rien essayé de nouveau."'"')

# Même chose avec cet fois un variable "famous_person" et une variable "message":
famous_person = "Albert Einstein"
message = f'\t{famous_person} a dit: "Qui' " n'a jamais fait d'erreur n'a jamais rien essayé de nouveau."'"'
print(message)

# Affiche le type de la variable:
print(type(famous_person))