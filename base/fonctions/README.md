# Fonctions

## [Index](/README.md)

## Sommaire

1. [Définir une fonction.](#définir-une-fonction)
2. [Annotation de type.](#annotation-de-type)
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

----------------------------------------------------------------------------

## Annotation de type

[Lien cours: greet_user.py.](/base/fonctions/greeter.py)

C'est quelque chose de bien connu : sous Python, pas besoin de spécifier les types des variables. Cette flexibilité permet de convertir très facilement des variables, ce qui est souvent le cas lorsque l'on manipule des données.

En revanche, lorsque l'on défini des fonctions, on aimerait insister sur le fait que certains paramètres soient d'un certain type, pour éviter des incohérences, voir des erreurs dans la suite du programme. Pour faciliter la lecture et la documentation des fonctions, la PEP 3107 autorise l'annotation des types des paramètres d'une fonction. Voyons en détail comment cela fonctionne.

### Les annotations de fonctions

Prenons la fonction longueur qui va calculer la longueur d'une chaîne de caractère.

```python
def longueur(x):
  return len(x)

longueur("Hello !")
```

Cette fonction requiert le paramètre x *qui est une chaîne de caractères*, et retourne un entier qui correspond à la longueur de cette même chaîne.

Comment spécifier ces deux types ? C'est là que les **annotations de fonctions** interviennent. Chaque paramètre va être suivi de son type, et la nous allons pouvoir spécifier la type retourné par la fonction avec ```->```.

```python
def longueur(x: str) -> int:
  return len(x)

longueur("Hello !")
```

Cette fonction se lit : on s'attends à avoir un x de type chaîne de caractères, et retourne un entier.

