#!/usr/bin/python3
"""Module qui définit une classe Square avec impression"""


class Square:
    """Classe qui définit un carré avec impression"""

    def __init__(self, size=0):
        """Initialise un carré avec une taille donnée

        Args:
            size: La taille du carré (défaut: 0)
        """
        self.size = size

    @property
    def size(self):
        """Getter pour la taille du carré

        Returns:
            La taille du carré
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter pour la taille du carré

        Args:
            value: La nouvelle taille du carré

        Raises:
            TypeError: Si value n'est pas un entier
            ValueError: Si value est négatif
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Retourne l'aire du carré

        Returns:
            L'aire du carré (size * size)
        """
        return self.__size * self.__size

    def my_print(self):
        """Imprime le carré avec le caractère #

        Si size est égal à 0, imprime une ligne vide
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
