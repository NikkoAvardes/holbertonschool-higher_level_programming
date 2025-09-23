#!/usr/bin/python3
"""
Module qui contient la classe BaseGeometry complète.
Cette classe inclut la validation des entiers pour les sous-classes.
"""


class BaseGeometry:
    """
    Classe de base pour les objets géométriques avec validation.

    Cette classe fournit :
    1. Une méthode area() abstraite à implémenter dans les sous-classes
    2. Une méthode integer_validator() pour valider les paramètres entiers
    """

    def area(self):
        """
        Méthode abstraite pour calculer l'aire.

        Raises:
            Exception: Toujours, car cette méthode doit être implémentée
                      dans les sous-classes.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Valide qu'une valeur est un entier positif.

        Args:
            name (str): Le nom de la valeur (pour les messages d'erreur)
            value: La valeur à valider

        Raises:
            TypeError: Si value n'est pas un entier
            ValueError: Si value est <= 0

        Note:
            Utilise type() au lieu d'isinstance() pour exclure les booléens
            car en Python, bool hérite de int mais on veut des entiers stricts.
        """
        # Vérifier le type exact (exclut les booléens)
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")

        # Vérifier que la valeur est positive
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
