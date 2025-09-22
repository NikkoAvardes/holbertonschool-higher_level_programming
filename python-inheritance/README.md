# Python - Inheritance

Ce projet couvre les concepts fondamentaux de l'héritage en Python, incluant la création de classes, l'héritage de classes, la surcharge de méthodes et la validation d'objets.

## Objectifs d'apprentissage

À la fin de ce projet, vous devriez être capable d'expliquer à quiconque, sans l'aide de Google :

### Général
- Pourquoi Python est génial
- Qu'est-ce qu'une superclasse, classe de base ou classe parent
- Qu'est-ce qu'une sous-classe
- Comment lister tous les attributs et méthodes d'une classe ou d'une instance
- Quand une instance peut avoir de nouveaux attributs
- Comment hériter d'une classe d'une autre
- Comment définir une classe avec plusieurs classes de base
- Quelle est la classe par défaut dont hérite chaque classe
- Comment surcharger une méthode ou un attribut hérité d'une classe de base
- Quels attributs ou méthodes sont disponibles par héritage pour les sous-classes
- Quel est le but de l'héritage
- Quelles sont et comment utiliser les fonctions built-in `isinstance`, `issubclass`, `type` et `super`

## Exigences

### Python Scripts
- Éditeurs autorisés : `vi`, `vim`, `emacs`
- Tous vos fichiers seront interprétés/compilés sur Ubuntu 20.04 LTS en utilisant python3 (version 3.8.5)
- Tous vos fichiers doivent se terminer par une nouvelle ligne
- La première ligne de tous vos fichiers doit être exactement `#!/usr/bin/python3`
- Un fichier `README.md`, à la racine du dossier du projet, est obligatoire
- Votre code doit utiliser le style pycodestyle (version 2.8.*)
- Tous vos fichiers doivent être exécutables
- La longueur de vos fichiers sera testée en utilisant `wc`

### Python Test Cases
- Éditeurs autorisés : `vi`, `vim`, `emacs`
- Tous vos fichiers doivent se terminer par une nouvelle ligne
- Tous vos fichiers de test doivent être dans le dossier `tests`
- Tous vos fichiers de test doivent être des fichiers texte (extension : `.txt`)
- Tous vos tests doivent être exécutés en utilisant cette commande : `python3 -m doctest ./tests/*`
- Tous vos modules doivent avoir une documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- Toutes vos classes doivent avoir une documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- Toutes vos fonctions (à l'intérieur et à l'extérieur d'une classe) doivent avoir une documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` et `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)

## Liste des tâches

### 0. Lookup
**Fichier :** `0-lookup.py`

Écrivez une fonction qui retourne la liste des attributs et méthodes disponibles d'un objet :
- Prototype : `def lookup(obj):`
- Retourne un objet liste
- Vous n'êtes pas autorisé à importer de module

### 1. My list
**Fichiers :** `1-my_list.py`, `tests/1-my_list.txt`

Écrivez une classe `MyList` qui hérite de `list` :
- Méthode d'instance publique : `def print_sorted(self):` qui imprime la liste, mais triée (tri croissant)
- Vous pouvez supposer que tous les éléments de la liste seront de type `int`
- Vous n'êtes pas autorisé à importer de module

### 2. Exact same object
**Fichier :** `2-is_same_class.py`

Écrivez une fonction qui retourne `True` si l'objet est exactement une instance de la classe spécifiée ; sinon `False`.
- Prototype : `def is_same_class(obj, a_class):`
- Vous n'êtes pas autorisé à importer de module

### 3. Same class or inherit from
**Fichier :** `3-is_kind_of_class.py`

Écrivez une fonction qui retourne `True` si l'objet est une instance de, ou si l'objet est une instance d'une classe qui a hérité de, la classe spécifiée ; sinon `False`.
- Prototype : `def is_kind_of_class(obj, a_class):`
- Vous n'êtes pas autorisé à importer de module

### 4. Only sub class of
**Fichier :** `4-inherits_from.py`

Écrivez une fonction qui retourne `True` si l'objet est une instance d'une classe qui a hérité (directement ou indirectement) de la classe spécifiée ; sinon `False`.
- Prototype : `def inherits_from(obj, a_class):`
- Vous n'êtes pas autorisé à importer de module

### 5. Geometry module
**Fichier :** `5-base_geometry.py`

Écrivez une classe vide `BaseGeometry`.
- Vous n'êtes pas autorisé à importer de module

### 6. Improve Geometry
**Fichier :** `6-base_geometry.py`

Écrivez une classe `BaseGeometry` (basée sur `5-base_geometry.py`).
- Méthode d'instance publique : `def area(self):` qui lève une Exception avec le message `area() is not implemented`
- Vous n'êtes pas autorisé à importer de module

### 7. Integer validator
**Fichiers :** `7-base_geometry.py`, `tests/7-base_geometry.txt`

Écrivez une classe `BaseGeometry` (basée sur `6-base_geometry.py`).
- Méthode d'instance publique : `def area(self):` qui lève une Exception avec le message `area() is not implemented`
- Méthode d'instance publique : `def integer_validator(self, name, value):` qui valide `value`
- Vous n'êtes pas autorisé à importer de module

### 8. Rectangle
**Fichier :** `8-rectangle.py`

Écrivez une classe `Rectangle` qui hérite de `BaseGeometry` (`7-base_geometry.py`).
- Instanciation avec width et height : `def __init__(self, width, height):`
- `width` et `height` doivent être privés. Pas de getter ou setter
- `width` et `height` doivent être des entiers positifs, validés par `integer_validator`

### 9. Full rectangle
**Fichier :** `9-rectangle.py`

Écrivez une classe `Rectangle` qui hérite de `BaseGeometry` (`7-base_geometry.py`). (tâche basée sur `8-rectangle.py`)
- La méthode `area()` doit être implémentée
- `print()` devrait imprimer, et `str()` devrait retourner, la description du rectangle suivante : `[Rectangle] <width>/<height>`

### 10. Square #1
**Fichier :** `10-square.py`

Écrivez une classe `Square` qui hérite de `Rectangle` (`9-rectangle.py`) :
- Instanciation avec size : `def __init__(self, size):`
- `size` doit être privé. Pas de getter ou setter
- `size` doit être un entier positif, validé par `integer_validator`
- La méthode `area()` doit être implémentée

### 11. Square #2
**Fichier :** `11-square.py`

Écrivez une classe `Square` qui hérite de `Rectangle` (`9-rectangle.py`). (tâche basée sur `10-square.py`).
- `print()` devrait imprimer, et `str()` devrait retourner, la description du carré : `[Square] <width>/<height>`

## Utilisation

Pour tester vos implémentations, utilisez les fichiers de test fournis :

```bash
# Exemple pour tester la fonction lookup
./0-main.py

# Exemple pour tester MyList
./1-main.py

# Pour exécuter les tests doctests
python3 -m doctest ./tests/*
```

## Auteur

Projet réalisé dans le cadre du cursus Holberton School.
