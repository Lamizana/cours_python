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
    
    # isistance retourne Faux si le paramètre x n'est pas une chaîne de caractère
    if not isinstance(x, str):  
        return "Erreur ! Pas un str"
    return len(x)


greet_user()
len = longueur("hello !")
print(f"- Longueur de la chaine: {len}")
