#!/usr/bin/python3
"""Module qui définit une classe Square avec position"""


class Square:
    """Classe qui définit un carré avec position"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialise un carré avec une taille et position données

        Args:
            size: La taille du carré (défaut: 0)
            position: La position du carré (défaut: (0, 0))
        """
        self.size = size
        self.position = position

    @property
    def position(self):
        """Getter pour la position du carré

        Returns:
            La position du carré
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Setter pour la position du carré

        Args:
            value: La nouvelle position du carré

        Raises:
            TypeError: Si value n'est pas un tuple de 2 entiers positifs
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
        """Imprime le carré avec le caractère # en tenant compte de la position

        Si size est égal à 0, imprime une ligne vide
        La position détermine où imprimer le carré
        """
        if self.__size == 0:
            print()
            return

        for i in range(self.__position[1]):
            print()

        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
