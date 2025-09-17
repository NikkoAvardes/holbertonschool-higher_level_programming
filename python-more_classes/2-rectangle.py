#!/usr/bin/python3
"""
Module définissant une classe Rectangle avec aire et périmètre.
Ce module contient la définition d'une classe Rectangle avec des propriétés
pour la largeur et la hauteur, ainsi que des méthodes pour calculer l'aire
et le périmètre.
"""


class Rectangle:
    """
    Classe représentant un rectangle géométrique.

    Cette classe permet de créer des rectangles avec une largeur et
    une hauteur, et offre des méthodes pour calculer l'aire et le périmètre.

    Attributes:
        width (int): La largeur du rectangle (valeur privée)
        height (int): La hauteur du rectangle (valeur privée)
    """
    def __init__(self, width=0, height=0):
        """
        Initialise un nouveau rectangle.

        Args:
            width (int, optional): La largeur du rectangle. Par défaut 0.
            height (int, optional): La hauteur du rectangle. Par défaut 0.
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        Getter pour la largeur du rectangle.

        Returns:
            int: La largeur actuelle du rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter pour la largeur du rectangle.

        Args:
            value (int): La nouvelle largeur du rectangle.

        Raises:
            TypeError: Si la valeur n'est pas un entier.
            ValueError: Si la valeur est négative.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter pour la hauteur du rectangle.

        Returns:
            int: La hauteur actuelle du rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter pour la hauteur du rectangle.

        Args:
            value (int): La nouvelle hauteur du rectangle.

        Raises:
            TypeError: Si la valeur n'est pas un entier.
            ValueError: Si la valeur est négative.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calcule l'aire du rectangle.

        Returns:
            int: L'aire du rectangle (largeur × hauteur).
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        Calcule le périmètre du rectangle.

        Returns:
            int: Le périmètre du rectangle (2 × (largeur + hauteur)).
        """
        return 2 * (self.__width + self.__height)
