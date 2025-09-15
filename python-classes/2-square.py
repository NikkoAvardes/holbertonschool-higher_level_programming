#!/usr/bin/python3
"""Module qui définit une classe Square avec validation de la taille"""


class Square:
    """Classe qui définit un carré avec validation de la taille"""

    def __init__(self, size=0):
        """Initialise un carré avec une taille donnée

        Args:
            size: La taille du carré (défaut: 0)

        Raises:
            TypeError: Si size n'est pas un entier
            ValueError: Si size est négatif
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
