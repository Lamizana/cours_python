# Fonctions

## [Index](/README.md)

## Sommaire

1. [Définir une fonction.](#définir-une-fonction)
2. [Transmettre des arguments.](#chaines-de-caractères)
3. [Valeurs de retour.](#nombres)
4. [Transmettre une liste.](#commentaires)
5. [Transmettre un nombre arbitraire d'éléments.](#commentaires)
6. [Stocker les fonctions dans des module.](#commentaires)
7. [Mettre en forme les fonctions.](#commentaires)

Une fonction est ***un bloc de code nommé***, créer pour effectuer une opération spécifique. Losrque l'on exécute une tache qu'on a définit dans une fonction on *appelle* la fonction qui en est responsable.
> Grace aux fonctions, les progammes sont plus facile à écrire, à tester, à corriger.
> 
On va apprendre à écrire certaines fonctions dont le rôle principal est d'afficher des informations, ainsi que d'autres fonctions conçues pour traiter des données et renvoyer une valeur ou un ensemble de valeurs.
Et enfin, on va voir comment stocker des fonctions dans des fichiers séparés, appelés ***modules***, pour organiser les fichiers de notre programme.

----------------------------------------------------------------------------

## Définir une fonction

[Lien cours: greet_user.py.](/base/fonctions/greeter.py)

Voici une fonction simple intitulée ```greet_user()``` qui affiche une formule de politesse:

```python
# greeter.py

def greet_user():
    """Affiche un message d'accueil simple"""
    print("Bonjour !")

greet_user()
```
