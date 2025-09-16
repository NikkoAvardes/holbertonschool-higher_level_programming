# Python - More Classes and Objects

Ce répertoire contient les exercices sur les classes et objets avancés en Python.

## Exercices

### 0. Simple rectangle
**Fichier:** `0-rectangle.py`
- Écrit une classe `Rectangle` vide qui définit un rectangle
- Aucun module ne doit être importé

### 1. Real definition of a rectangle
**Fichier:** `1-rectangle.py`
- Classe `Rectangle` avec attributs privés `width` et `height`
- Propriétés getter et setter avec validation
- Instantiation avec largeur et hauteur optionnelles

### 2. Area and Perimeter
**Fichier:** `2-rectangle.py`
- Basé sur `1-rectangle.py`
- Méthodes publiques `area()` et `perimeter()`
- Si largeur ou hauteur = 0, périmètre = 0

### 3. String representation
**Fichier:** `3-rectangle.py`
- Basé sur `2-rectangle.py`
- `print()` et `str()` affichent le rectangle avec le caractère `#`
- Si largeur ou hauteur = 0, retourne une chaîne vide

### 4. Eval is magic
**Fichier:** `4-rectangle.py`
- Basé sur `3-rectangle.py`
- `repr()` retourne une représentation pour recréer l'instance avec `eval()`

### 5. Detect instance deletion
**Fichier:** `5-rectangle.py`
- Basé sur `4-rectangle.py`
- Affiche "Bye rectangle..." quand une instance est supprimée

### 6. How many instances
**Fichier:** `6-rectangle.py`
- Basé sur `5-rectangle.py`
- Attribut de classe `number_of_instances` pour compter les instances

### 7. Change representation
**Fichier:** `7-rectangle.py`
- Basé sur `6-rectangle.py`
- Attribut de classe `print_symbol` pour personnaliser le symbole d'affichage

### 8. Compare rectangles
**Fichier:** `8-rectangle.py`
- Basé sur `7-rectangle.py`
- Méthode statique `bigger_or_equal()` pour comparer les rectangles par aire

### 9. A square is a rectangle
**Fichier:** `9-rectangle.py`
- Basé sur `8-rectangle.py`
- Méthode de classe `square()` qui retourne un rectangle carré

## Repository
- **GitHub repository:** holbertonschool-higher_level_programming
- **Directory:** python-more_classes
