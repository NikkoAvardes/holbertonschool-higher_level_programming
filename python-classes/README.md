# Python - Classes et objets

Ce répertoire contient les exercices sur les classes et objets en Python.

## Exercices

### 0. My first square
**Fichier:** `0-square.py`
- Écrit une classe `Square` vide qui définit un carré
- Aucun module ne doit être importé

### 1. Square with size
**Fichier:** `1-square.py`
- Classe `Square` qui définit un carré avec :
- Attribut d'instance privé : `size`
- Instantiation avec size (pas de vérification de type/valeur)

### 2. Size validation
**Fichier:** `2-square.py`
- Classe `Square` qui définit un carré avec :
- Attribut d'instance privé : `size`
- Instantiation avec size optionnel : `def __init__(self, size=0):`
- `size` doit être un entier, sinon lever une exception `TypeError`
- Si `size` est inférieur à 0, lever une exception `ValueError`

### 3. Area of a square
**Fichier:** `3-square.py`
- Basé sur `2-square.py`
- Méthode d'instance publique : `def area(self):` qui retourne l'aire actuelle du carré

### 4. Access and update private attribute
**Fichier:** `4-square.py`
- Basé sur `3-square.py`
- Attribut d'instance privé : `size` avec :
  - Propriété `def size(self):` pour le récupérer
  - Setter de propriété `def size(self, value):` pour le définir
- Validation du type et de la valeur dans le setter

### 5. Printing a square
**Fichier:** `5-square.py`
- Basé sur `4-square.py`
- Méthode d'instance publique : `def my_print(self):` qui imprime le carré avec le caractère `#`
- Si size est égal à 0, imprimer une ligne vide

### 6. Coordinates of a square
**Fichier:** `6-square.py`
- Basé sur `5-square.py`
- Attribut d'instance privé : `position` avec :
  - Propriété `def position(self):` pour le récupérer
  - Setter de propriété `def position(self, value):` pour le définir
- `position` doit être un tuple de 2 entiers positifs
- Instantiation avec size et position optionnels : `def __init__(self, size=0, position=(0, 0)):`
- La position doit être utilisée en utilisant des espaces lors de l'impression

## Repository
- **GitHub repository:** holbertonschool-higher_level_programming
- **Directory:** python-classes
