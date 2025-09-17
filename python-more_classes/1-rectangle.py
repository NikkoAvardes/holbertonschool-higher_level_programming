#!/usr/bin/python3
"""Module définissant une classe Rectangle."""


class Rectangle:
    """Classe Rectangle avec largeur et hauteur."""

    def __init__(self, width=0, height=0):
        """Initialise un rectangle."""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Getter pour la largeur."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter pour la largeur avec validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter pour la hauteur."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter pour la hauteur avec validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
