# Présentation des listes

## [Index](/README.md)

## Sommaire

1. [Definition d'une liste.](#definition-dune-liste)
2. [Modifier, ajouter , supprimer des éléments.](#chaines-de-caractères)
3. [Organiser une liste.](#nombres)
4. [Erreur indexation de listes.](#commentaires)

----------------------------------------------------------------------------

## Definition d'une liste

[Lien cours: bicycles.py.](/base/listes/bicycles.py)
Une **liste** est une ***collection d'éléments dans un ordre particulier***.

- Elle peut contenir:
  - Les lettres de l'alphabet.
  - les chiffres et les nombres.
  - des chaines de carctères.

On peut intégrer **ce que l'on veut** dans une liste. De plus, comme une liste contient plusieurs éléments il vaut mieux lui **donner un nom au pluriel**.
Exemple: `letters`.

Dans ***Python***, les crochets `[]` *délimitent* une liste, et chaque élément est séparéé par un virgule.

```python
bicycle.py

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
```

Si l'on demande à Python d'afficher une liste, il renvoie **sa représentation de la liste**, notamment les crochets:

```python
['trek', 'cannondale', redline', 'specialized']
```

### Accéder aux éléments d'une liste

Les listes étant des *ensemble ordonnés*, on peut accéder a l'un des éléments d'une liste en indiquant à Python sa position, ou son ***index***.

Pour acceder à un élément d'une liste, écrire le nom de la liste suivie de l'index de l'élément entre crochet.

- Par exemple, extraire le premier vélo de la liste bicycle:

```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycle[0])
$> trek
```

Lorsque nous demandons un élément d'une liste, Python le renvoie ***sans crochet***.

On peux également applquer les méthodes de chaines à un élément de cette liste.

```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycle[0].tittle())
$> Trek
```

### Les positions d'index commence à 0, pas à 1

Python considère que le premier élément d'une liste occupe ***la postion 0***, pas la position 1.
Il en est ainsi pour la plupart des langages de programmation. La raison tient à la facon dont les opérations sont effectuées à un niveau inférieur. si l'on recoit des résultats innatendus, verifier si l'erreur ne vient pas d'une mauvaise indexation.

Le deuxiéme élément d'une liste à l'index 1. Grace à ce systéme de comptage, on peux accéder à l'élément souhaité dans une liste, en soustrayant 1 de sa position dans la liste.
Ainsi, pour accéder au quatrième élément d'une liste, demander l'élément situé à l'index 3

- Le code suivant demande les vélos à l'index 1 et 3:
  
```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycle[1])
print(bicycle[3])

$> cannondale
$> specialized
```

> le code renvoie les deuxième et quatrième vélos de la liste.

Python utilise une syntaxe particulière pour accéder au ***dernier élément*** d'une liste.
Si l'on demende l'élément à l'index -1, python renvoie toujours le dernier élément de la liste:

```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycle[-1])

$> specialized
```


----------------------------------------------------------------------------

## Utilisations des listes

[Sommaire.](#sommaire)

- A faire...

----------------------------------------------------------------------------
