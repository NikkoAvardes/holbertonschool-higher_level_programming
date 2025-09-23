#!/usr/bin/python3
"""
Module qui contient la classe Rectangle complète avec area et __str__.
Cette classe implémente complètement un rectangle géométrique.
"""

# Import de la classe BaseGeometry depuis le module 7-base_geometry
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Classe Rectangle complète qui hérite de BaseGeometry.

    Cette classe implémente un rectangle avec toutes les fonctionnalités :
    - Validation des dimensions
    - Calcul de l'aire
    - Représentation sous forme de chaîne

    Attributes:
        __width (int): Largeur du rectangle (attribut privé)
        __height (int): Hauteur du rectangle (attribut privé)
    """

    def __init__(self, width, height):
        """
        Initialise un rectangle avec largeur et hauteur.

        Args:
            width (int): Largeur du rectangle
            height (int): Hauteur du rectangle
        """
        # Validation des paramètres
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        # Stockage en attributs privés
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calcule et retourne l'aire du rectangle.

        Returns:
            int: L'aire du rectangle (largeur × hauteur)

        Note:
            Cette méthode surcharge la méthode abstraite area()
            de BaseGeometry. Elle fournit une implémentation concrète
            du calcul d'aire.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Retourne une représentation textuelle du rectangle.

        Returns:
            str: Description du rectangle au format
                 "[Rectangle] largeur/hauteur"

        Note:
            Cette méthode est appelée par print() et str().
            Elle définit comment l'objet Rectangle s'affiche.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
