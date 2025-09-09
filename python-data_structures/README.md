# Python - Data Structures: Lists, Tuples

Ce projet fait partie du cursus **Holberton School** et se concentre sur l'apprentissage et la manipulation des structures de données fondamentales en Python : les **listes** et les **tuples**.

## 📚 Objectifs d'apprentissage

À la fin de ce projet, vous devriez être capable d'expliquer sans aide :

### Général
- Pourquoi Python est génial
- Qu'est-ce que les listes et comment les utiliser
- Quelles sont les différences et similitudes entre les chaînes et les listes
- Quelles sont les méthodes les plus communes des listes et comment les utiliser
- Comment utiliser les listes comme piles et files
- Qu'est-ce que les list comprehensions et comment les utiliser
- Qu'est-ce que les tuples et comment les utiliser
- Quand utiliser les tuples vs les listes
- Qu'est-ce qu'une séquence
- Qu'est-ce que le tuple packing
- Qu'est-ce que le sequence unpacking
- Qu'est-ce que l'instruction `del` et comment l'utiliser

## 🛠 Exigences

### Général
- Éditeurs autorisés : `vi`, `vim`, `emacs`
- Tous vos fichiers seront interprétés/compilés sur Ubuntu 20.04 LTS en utilisant python3 (version 3.8.5)
- Tous vos fichiers doivent se terminer par une nouvelle ligne
- La première ligne de tous vos fichiers doit être exactement `#!/usr/bin/python3`
- Un fichier `README.md`, à la racine du dossier du projet, est obligatoire
- Votre code doit utiliser le style pycodestyle (version 2.8.*)
- Tous vos fichiers doivent être exécutables
- La longueur de vos fichiers sera testée avec `wc`

## 📋 Liste des tâches

| Fichier | Description |
|---------|-------------|
| `0-print_list_integer.py` | Fonction qui affiche tous les entiers d'une liste |
| `1-element_at.py` | Fonction qui récupère un élément d'une liste comme en C |
| `2-replace_in_list.py` | Fonction qui remplace un élément d'une liste à une position spécifique |
| `3-print_reversed_list_integer.py` | Fonction qui affiche tous les entiers d'une liste, en ordre inverse |
| `4-new_in_list.py` | Fonction qui remplace un élément dans une liste à une position spécifique sans modifier la liste originale |
| `5-no_c.py` | Fonction qui supprime tous les caractères 'c' et 'C' d'une chaîne |
| `6-print_matrix_integer.py` | Fonction qui affiche une matrice d'entiers |
| `7-add_tuple.py` | Fonction qui additionne 2 tuples |
| `8-multiple_returns.py` | Fonction qui retourne un tuple avec la longueur d'une chaîne et son premier caractère |
| `9-max_integer.py` | Fonction qui trouve le plus grand entier d'une liste |
| `10-divisible_by_2.py` | Fonction qui trouve tous les multiples de 2 dans une liste |
| `11-delete_at.py` | Fonction qui supprime l'élément à une position spécifique dans une liste |
| `12-switch.py` | Programme qui échange la valeur de deux variables |

## 🚀 Utilisation

### Exécution des tests

Chaque fichier principal (`*-main.py`) contient des tests pour la fonction correspondante.

```bash
# Exemple d'exécution
./0-main.py
./1-main.py
./2-main.py
# ... etc
```

### Exemples d'utilisation

#### 0. Afficher une liste d'entiers
```python
#!/usr/bin/python3
print_list_integer = __import__('0-print_list_integer').print_list_integer

my_list = [1, 2, 3, 4, 5]
print_list_integer(my_list)
```

#### 1. Accès sécurisé à un élément de liste
```python
#!/usr/bin/python3
element_at = __import__('1-element_at').element_at

my_list = [1, 2, 3, 4, 5]
idx = 3
print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))
```

#### 7. Addition de tuples
```python
#!/usr/bin/python3
add_tuple = __import__('7-add_tuple').add_tuple

tuple_a = (1, 89)
tuple_b = (88, 11)
new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)
```

## 🔧 Fonctionnalités principales

### Manipulation de listes
- Affichage formaté d'éléments
- Accès sécurisé aux indices
- Remplacement d'éléments
- Création de nouvelles listes modifiées
- Suppression d'éléments

### Manipulation de tuples
- Addition de tuples avec gestion des tailles différentes
- Unpacking et packing de tuples
- Retour de valeurs multiples

### Algorithmes utiles
- Recherche du maximum dans une liste
- Filtrage par condition (multiples de 2)
- Manipulation de chaînes de caractères

## 📖 Concepts Python abordés

- **Listes** : structures mutables, méthodes intégrées
- **Tuples** : structures immutables, unpacking
- **Indexing** : accès aux éléments par position
- **Slicing** : extraction de sous-séquences
- **List comprehensions** : création concise de listes
- **String formatting** : formatage avec `.format()`
- **Error handling** : gestion des indices invalides

## 📝 Style et bonnes pratiques

- Utilisation de `pycodestyle` pour le respect des conventions PEP 8
- Gestion des cas d'erreur (indices négatifs, listes vides)
- Documentation claire des fonctions
- Tests complets avec fichiers main

## 🏫 À propos

Ce projet fait partie du programme **Holberton School** dans le cursus de programmation Python niveau supérieur. Il vise à maîtriser les structures de données fondamentales qui sont essentielles pour tout développement Python.
