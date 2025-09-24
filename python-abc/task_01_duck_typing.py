#!/usr/bin/env python3
"""
Shapes, Interfaces, and Duck Typing

Ce module démontre le concept de "duck typing" en Python et l'utilisation
des classes abstraites pour créer une interface commune pour les formes.

Le duck typing signifie : "Si ça marche comme un canard et que ça fait
coin-coin comme un canard, alors c'est probablement un canard."
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Classe abstraite Shape qui définit l'interface pour les formes.

    Cette classe sert de contrat que toutes les formes doivent respecter
    en implémentant les méthodes area() et perimeter().
    """

    @abstractmethod
    def area(self):
        """
        Méthode abstraite pour calculer l'aire de la forme.

        Returns:
            float: L'aire de la forme
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Méthode abstraite pour calculer le périmètre de la forme.

        Returns:
            float: Le périmètre de la forme
        """
        pass


class Circle(Shape):
    """
    Classe Circle qui représente un cercle.

    Hérite de Shape et implémente les méthodes area() et perimeter()
    pour un cercle.
    """

    def __init__(self, radius):
        """
        Initialise un cercle avec un rayon donné.

        Args:
            radius (float): Le rayon du cercle
        """
        self.__radius = radius

    def area(self):
        """
        Calcule l'aire du cercle.

        Returns:
            float: L'aire du cercle (π * r²)
        """
        return math.pi * self.__radius ** 2

    def perimeter(self):
        """
        Calcule le périmètre (circonférence) du cercle.

        Returns:
            float: Le périmètre du cercle (2 * π * r)
        """
        return 2 * math.pi * self.__radius


class Rectangle(Shape):
    """
    Classe Rectangle qui représente un rectangle.

    Hérite de Shape et implémente les méthodes area() et perimeter()
    pour un rectangle.
    """

    def __init__(self, width, height):
        """
        Initialise un rectangle avec une largeur et une hauteur données.

        Args:
            width (float): La largeur du rectangle
            height (float): La hauteur du rectangle
        """
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calcule l'aire du rectangle.

        Returns:
            float: L'aire du rectangle (largeur * hauteur)
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calcule le périmètre du rectangle.

        Returns:
            float: Le périmètre du rectangle (2 * (largeur + hauteur))
        """
        return 2 * (self.__width + self.__height)


def shape_info(shape):
    """
    Fonction qui utilise le duck typing pour afficher les infos d'une forme.

    Cette fonction ne vérifie pas le type de l'objet passé en paramètre.
    Elle fait confiance au fait que l'objet a les méthodes area() et
    perimeter() (duck typing).

    Args:
        shape: Un objet qui implémente les méthodes area() et perimeter()
    """
    area = shape.area()
    perimeter = shape.perimeter()
    print(f"Area: {area}")
    print(f"Perimeter: {perimeter}")
