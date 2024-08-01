# cours_python/base/fonctions/greet_user.py
###############################################################################
# Présentation des fonction.    source:"Petite lecon de python"               
# Compréhesion et gestion des fonctions                                
#                                                            - 01/aout/2024 - 
###############################################################################

def greet_user() -> None:
    """Affiche un message d'accueil simple"""
    
    print("Bonjour !")
    
    
# x est une str et retourne un int.
def longueur(x: str) -> int:
    """Retourne la longueur d'une chaine de caractère"""
    
    return len(x)

len = longueur("Hello !")
print(f"longueur de la chaine {len}")
greet_user()