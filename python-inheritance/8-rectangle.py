#!/usr/bin/python3
"""
Module qui contient la classe Rectangle héritant de BaseGeometry.
Cette classe implémente un rectangle avec validation des dimensions.
"""

# Import de la classe BaseGeometry depuis le module 7-base_geometry
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Classe Rectangle qui hérite de BaseGeometry.

    Cette classe représente un rectangle avec une largeur et une hauteur.
    Les dimensions sont validées à l'initialisation et stockées en privé.

    Attributes:
        __width (int): Largeur du rectangle (attribut privé)
        __height (int): Hauteur du rectangle (attribut privé)
    """

    def __init__(self, width, height):
        """
        Initialise un rectangle avec largeur et hauteur.

        Args:
            width (int): Largeur du rectangle (doit être un entier positif)
            height (int): Hauteur du rectangle (doit être un entier positif)

        Note:
            - Utilise integer_validator() héritée pour valider les paramètres
            - Les attributs sont privés (name mangling avec __)
            - La validation se fait AVANT l'assignation des attributs
        """
        # Valider les paramètres avec la méthode héritée
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        # Stocker les valeurs en attributs privés
        self.__width = width
        self.__height = height
