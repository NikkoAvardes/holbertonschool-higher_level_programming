# Python - If/Else, Loops, Functions

Ce projet fait partie du curriculum Holberton School et couvre les concepts fondamentaux de Python : les conditions, les boucles et les fonctions.

## 📚 Objectifs d'apprentissage

À la fin de ce projet, vous devriez être capable d'expliquer :

- Pourquoi Python est génial
- Pourquoi l'indentation est si importante en Python
- Comment utiliser les conditions `if`, `if ... else`
- Comment utiliser les commentaires
- Comment affecter des valeurs aux variables
- Comment utiliser les boucles `while` et `for`
- Comment utiliser les instructions `break` et `continue`
- Comment utiliser les clauses `else` sur les boucles
- À quoi sert la fonction `pass` et quand l'utiliser
- Comment utiliser `range`
- Qu'est-ce qu'une fonction et comment l'utiliser
- Qu'est-ce qu'une fonction qui ne retourne pas d'instruction return
- Portée des variables
- Qu'est-ce qu'un traceback
- Quelles sont les fonctions arithmétiques

## 🗂️ Structure du projet

| Fichier | Description |
|---------|-------------|
| `0-positive_or_negative.py` | Détermine si un nombre aléatoire est positif, négatif ou zéro |
| `1-last_digit.py` | Affiche le dernier chiffre d'un nombre aléatoire |
| `2-print_alphabet.py` | Affiche l'alphabet en minuscules |
| `3-print_alphabt.py` | Affiche l'alphabet en minuscules sauf 'q' et 'e' |
| `4-print_hexa.py` | Affiche les nombres de 0 à 98 en décimal et hexadécimal |
| `5-print_comb2.py` | Affiche les nombres de 00 à 99 |
| `6-print_comb3.py` | Affiche toutes les combinaisons possibles de deux chiffres |
| `7-islower.py` | Fonction qui vérifie si un caractère est en minuscule |
| `8-uppercase.py` | Fonction qui affiche une chaîne en majuscules |
| `9-print_last_digit.py` | Fonction qui affiche le dernier chiffre d'un nombre |
| `10-add.py` | Fonction qui additionne deux entiers |
| `11-pow.py` | Fonction qui calcule a à la puissance b |
| `12-fizzbuzz.py` | Fonction FizzBuzz |

## 🚀 Utilisation

### Exécution des scripts

```bash
# Exemple avec le script 0-positive_or_negative.py
python3 0-positive_or_negative.py

# Exemple avec les fonctions (utilise les fichiers main)
python3 7-main.py
```

### Tests des fonctions

Chaque fonction a un fichier de test correspondant (`*-main.py`) :

```bash
# Tester la fonction islower
python3 7-main.py

# Tester la fonction uppercase
python3 8-main.py

# Tester la fonction print_last_digit
python3 9-main.py
```

## 📋 Exigences

- **OS** : Ubuntu 20.04 LTS
- **Interpréteur Python** : python3 (version 3.8.5)
- **Style de code** : pycodestyle (version 2.8.*)
- Tous les fichiers doivent être exécutables
- Tous les fichiers doivent se terminer par une nouvelle ligne
- La première ligne de tous les fichiers doit être exactement `#!/usr/bin/python3`

## 🔧 Installation et configuration

1. **Cloner le repository** :
```bash
git clone <repository-url>
cd python-if_else_loops_functions
```

2. **Vérifier la version Python** :
```bash
python3 --version
```

3. **Installer pycodestyle pour la vérification du style** :
```bash
pip3 install pycodestyle
```

4. **Vérifier le style de code** :
```bash
pycodestyle *.py
```

## 📝 Exemples d'utilisation

### Fonction islower
```python
#!/usr/bin/python3
islower = __import__('7-islower').islower

print("a is {}".format("lower" if islower("a") else "upper"))
print("H is {}".format("lower" if islower("H") else "upper"))
print("A is {}".format("lower" if islower("A") else "upper"))
print("3 is {}".format("lower" if islower("3") else "upper"))
print("g is {}".format("lower" if islower("g") else "upper"))
```

### Fonction uppercase
```python
#!/usr/bin/python3
uppercase = __import__('8-uppercase').uppercase

uppercase("best")
uppercase("Best School 98 Battery street")
```

### FizzBuzz
```python
#!/usr/bin/python3
fizzbuzz = __import__('12-fizzbuzz').fizzbuzz

fizzbuzz()
```

## 🎯 Concepts clés appris

- **Conditions** : `if`, `elif`, `else`
- **Boucles** : `for`, `while`
- **Fonctions** : définition, paramètres, valeur de retour
- **Manipulation de chaînes** : `ord()`, `chr()`, formatage
- **Nombres aléatoires** : module `random`
- **Bonnes pratiques** : PEP 8, documentation, tests

## 👤 Auteur

Projet réalisé dans le cadre de la formation Holberton School.

---

*Ce projet fait partie du curriculum de Holberton School pour apprendre les fondamentaux de Python.*
