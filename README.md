# Ensemble de connaissances relatives à python
>
<<<<<<< HEAD
> Created by alex Lamizana in 07/06/2024 - last update in 31/07/2024.
=======
> Created by alex Lamizana in 07/06/2024 - last update in 19/06/2024.
>>>>>>> ab22d9bbcf38c6c1be4429f62efb83c982cb216c
----------------------------------------------------------------------------

On va faire un survol global mais précis de toutes les fonctionnalitées python.

## Sommaire

1. [LES BASES.](#les-bases)
    - [[1] - Mise en route.](#mise-en-route)
    - [[2] - Variables et types de données simples.](#variables-et-types-de-données-simples)
    - [[3] - Présentation des listes.](#présentation-des-listes)

2. [PROJETS.](#projets)

----------------------------------------------------------------------------

## LES BASES

----------------------------------------------------------------------------

### Mise en route

[Sommaire.](#sommaire)

A faire...

----------------------------------------------------------------------------

### Variables et types de données simples

<<<<<<< HEAD
[Dossier Variables >>](/base/variables/README.md)
=======
[Sommaire.](#sommaire)

1. [Variables.](#variables)
2. [Chaines de caractères.](#chaines-de-caractères)
3. [Nombres.](#nombres)
    - [Nombres entiers.](#nombres-entiers)
    - [Nombres flottants.](#nombres-flottants)
    - [Nombres entiers et nombres flottants.](#nombres-entiers-et-nombres-flottants)
    - [Caractères de soulignement dans les nombres.](#caractères-de-soulignement-dans-les-nombres)
    - [Affectation multiples.](#affectation-multiples)
    - [Constantes.](#constantes)
    - [Exercices sur les nombres.](#exercices-sur-les-nombres)
4. [Commentaires.](#commentaires)
    - [Exercices commentaires.](#exercices-commentaires)

----------------------------------------------------------------------------

#### Variables

[Sommaire.](#sommaire)

Les variables sont des *étiquettes*, elles sont souvent décrites comme des **boites qui stockent des valeurs**.
> Une variable fait réference à une valeur.

----------------------------------------------------------------------------

#### Chaines de caractères

[Sommaire.](#sommaire)

A faire...

[Lien exercices sur les chaine de caractères:](base/exos/casse_nom.py): exos 2-3 à 2-7.

```bash
file: cours/base/exos/casse_nom.py
```

----------------------------------------------------------------------------

#### Nombres

[Sommaire](#sommaire)

En programmation, on utilise souvent des nombres pour mémoriser le score d'un jeu, représenter des données dans de visualisations, stocker des informations dans des applications web, etc.
Python applique **différents traitements aux nombres selon leur utilisation**.
Regardons comment il gére les nombres entiers car se sont les plus facile à utiliser.

- pour lancer le terminal python:

```bash
$ python3
>>>
```

----------------------------------------------------------------------------

##### Nombres entiers

- On peut additionner(+), soustraire(-), multiplier(*) et diviser(/) des nombres entiers dans python:

````python
>>> 2 + 3
5
>>> 3 - 2
1
>>> 2 * 3
6
>>> 3 / 2
1.5
````

Dans une session de terminal, python renvoie **le résultat de l'opération**.
Il utilise 2 symboles de multiplication pour représenter les exposants:

```python
>>> 3 ** 2
9
>>> 3 ** 3
27
>>> 10 ** 6
1000000
```

Python gére également *l'ordre de opérations* et permet d'effectuer **plusieurs opération dans la meme expression**.
On peut utiliser les parenthèses pour modifier l'ordre des opérations et lui demander d'évaluer l'expression dans l'odre souhaité.

```python
# Respecte l'ordre arithmetique de base, multiplication avant addition.
>>> 2 + 3 * 4
14
# Force les prioritées des opérations.
>>> (2 + 3) * 4
20
```

----------------------------------------------------------------------------

##### Nombres flottants

Python qualifie de *flottant* tout nombre comportant **un point comme séparateur décimal**.

```python
>>> 0.1 + .1
0.2
>>> .2 + .2
4
>>> 2 * 0.1
0.2
>>> 2.4 * 1.6
3.84
```

> [!NOTE]
> Python peut parfois obtenir un nombre arbitraire de décimales dans la réponse, cela a peu de conséquences.

----------------------------------------------------------------------------

##### Nombres entiers et nombres flottants

Lorsqu'on divise 2 nombres (meme si ce sont des nombres entiers) et que le résultat est un nombre entier, **on obtient toujours un nombre flottant**.

```python
>>> 4 / 2
2.0
```
>>>>>>> ab22d9bbcf38c6c1be4429f62efb83c982cb216c

1. Variables.
2. Chaines de caractères.
3. Nombres.
    - Nombres entiers.
    - Nombres flottants.
    - Nombres entiers et nombres flottants
    - Caractères de soulignement dans les nombres
    - Affectation multiples.
    - Constantes.
    - Exercices sur les nombres.
4. Commentaires.
    - Exercices commentaires.

----------------------------------------------------------------------------

### Présentation des listes

[Dossier Listes >>](/base/listes/README.md)

<<<<<<< HEAD
1. Definition d'une liste.
2. Modifier, ajouter , supprimer des éléments.
3. Organiser une liste.
4. Erreur indexation de listes.
=======
Les commentaires sont extrémement utile dans la majorité des langages de programmation.
Dans les programmes plus long et complexe il est recommendé d'ajouter des notes expliquant
la démarche que l'on a suivit.

> Un commentaire permet d'écrire des notes dans un programme.
>>>>>>> ab22d9bbcf38c6c1be4429f62efb83c982cb216c

----------------------------------------------------------------------------

#### Definition d'une liste

[Lien cours bicycles.py.](base/bicycles.py)
Une **liste** est une ***collection d'éléments dans un ordre particulier***.

- Elle peut contenir:
  - Les lettres de l'alphabet.
  - les chiffres et les nombres.
  - des chaines de carctères.

On peut intégrer **ce que l'on veut** dans une liste. De plus, comme une liste contiient plusieurs éléments il vaut mieux lui **donner un nom au pluriel**.
Exemple: `letters`.

Dans ***Python***, les crochets `[]` *délimitent* une liste, et chaque élément est séparéé par un virgule.

<<<<<<< HEAD
=======
----------------------------------------------------------------------------

### Présentation des listes

[Sommaire.](#sommaire)

1. [Definition d'une liste.](#définition-dune-liste)
   - [Accéder à plusieurs éléments d'une liste.](#accéder-à-plusieurs-éléments-dune-liste)
   - [Les positions d'index débutent à 0, pas à 1.](#les-positions-dindex-débutent-à-0-pas-à-1)

2. [Modifier, ajouter , supprimer des éléments.](#chaines-de-caractères)
3. [Organiser une liste.](#nombres)
4. [Erreur indexation de listes.](#commentaires)

----------------------------------------------------------------------------

#### Définition d'une liste

[Lien cours listes.](base/listes.py)
Une **liste** est une ***collection d'éléments dans un ordre particulier***.

- Elle peut contenir:
  - Les lettres de l'alphabet.
  - les chiffres et les nombres.
  - des chaines de caractères.

On peut intégrer **ce que l'on veut** dans une liste. De plus, comme une liste contiient plusieurs éléments il vaut mieux lui **donner un nom au pluriel**.
Exemple: `letters`.

Dans ***Python***, les crochets `[]` *délimitent* une liste, et chaque élément est séparéé par un virgule.

```python
# Initialisation et assignation d'une liste:
bicycles = ["treck", "cannondale", "redline", "bmx"]
print(bicycles)
```

- Si l'on demande à ***Python*** d'afficher une liste, il renvoie une **representation de la liste**:
  
```python
['treck', 'cannondale', 'redline', 'bmx']
```

Voyons comment accéder à chaque éléments d'une liste.

----------------------------------------------------------------------------

##### Accéder à plusieurs éléments d'une liste

Les listes étant **des ensemble ordonnées**, on peut acéder à l'un des éléments en indiquant à ***Python*** sa position, ou **index**.
Pour acéder à un élément d'une liste, écrire le *nom de la liste suivie de l'index de l'élément entre crochet*.

```python
>>> print(bicycles[0])
>>> treck
```

Lorsque nous demandons un élément d'une liste, Python le renvoie *sans crochet*.
On peut appliquer les **methode de chaines**  à un élément d'une liste.

----------------------------------------------------------------------------

##### Les positions d'index débutent à 0, pas à 1

Python considère que le **1er élément d'une liste commence à ***0*** et pas à 1**

----------------------------------------------------------------------------
>>>>>>> ab22d9bbcf38c6c1be4429f62efb83c982cb216c

### Utilisations des listes

[Sommaire.](#sommaire)

- A faire...

----------------------------------------------------------------------------

### Instructions if

[Sommaire.](#sommaire)

- A faire...

----------------------------------------------------------------------------

### Dictionaires

[Sommaire.](#sommaire)

- A faire...

----------------------------------------------------------------------------

## PROJETS

[Sommaire.](#sommaire)

- A faire...

----------------------------------------------------------------------------
> Pour tout Branquignols qui comprend rien à rien, je suis pareil, partageons notre détresse...
----------------------------------------------------------------------------
