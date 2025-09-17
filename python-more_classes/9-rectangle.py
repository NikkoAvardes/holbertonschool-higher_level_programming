#!/usr/bin/python3
"""
Module définissant une classe Rectangle complète avec les fonctionnalités.

Ce module contient la définition d'une classe Rectangle avec des propriétés
pour la largeur et la hauteur, ainsi que des méthodes pour calculer l'aire,
le périmètre, l'affichage, et des méthodes statiques et de classe complètes.
"""


class Rectangle:
    """
    Classe représentant un rectangle géométrique avec les fonctionnalités.

    Cette classe permet de créer des rectangles avec une largeur et hauteur,
    et offre des méthodes pour calculer l'aire, le périmètre, l'affichage
    avec un symbole personnalisable, compte le nombre d'instances et propose
    des méthodes pour créer des carrés et comparer des rectangles.

    Attributes:
        number_of_instances (int): Compteur du nombre d'instances de Rectangle
        print_symbol (any): Symbole utilisé pour l'affichage (par défaut '#')
        width (int): La largeur du rectangle (valeur privée)
        height (int): La hauteur du rectangle (valeur privée)
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Initialise un nouveau rectangle.

        Incrémente le compteur d'instances lors de la création.

        Args:
            width (int, optional): La largeur du rectangle. Par défaut 0.
            height (int, optional): La hauteur du rectangle. Par défaut 0.
        """
        Rectangle.number_of_instances += 1
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

    def __str__(self):
        i = str(self.print_symbol)
        """
        Retourne une représentation string du rectangle.

        Le rectangle est dessiné avec le symbole défini dans print_symbol.
        Si la largeur ou la hauteur est 0, retourne une chaîne vide.

        Returns:
            str: Représentation visuelle du rectangle ou chaîne vide.
        """
        if (self.__width == 0 or self.__height == 0):
            return ""
        else:
            return (i * self.__width) + ("\n" + i *
                                         self.__width) * (self.__height - 1)

    def __repr__(self):
        """
        Retourne une représentation officielle du rectangle.

        Cette représentation peut être utilisée pour recréer l'objet
        avec eval().

        Returns:
        str: Représentation du rectangle sous forme Rectangle(width, height).
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Destructeur de la classe Rectangle.

        Décrémente le compteur d'instances et affiche un message
        de goodbye lorsque l'instance est détruite.
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @classmethod
    def square(cls, size=0):
        """
        Méthode de classe pour créer un carré.

        Crée un rectangle carré avec la même largeur et hauteur.

        Args:
            size (int, optional): La taille du côté du carré. Par défaut 0.

        Returns:
        Rectangle: Une nouvelle instance de Rectangle représentant un carré.
        """
        return cls(size, size)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Méthode statique pour comparer deux rectangles.

        Compare l'aire de deux rectangles et retourne le plus grand
        ou égal. En cas d'égalité, retourne le premier rectangle.

        Args:
            rect_1 (Rectangle): Le premier rectangle à comparer.
            rect_2 (Rectangle): Le second rectangle à comparer.

        Returns:
        Rectangle: Le rectangle avec la plus grande aire.

        Raises:
        TypeError: Si l'un des arguments n'est pas une instance de Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
