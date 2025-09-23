#!/usr/bin/python3
"""
Module qui contient la classe Square héritant de Rectangle.
Cette classe implémente un carré comme cas spécial de rectangle.
"""

# Import de la classe Rectangle depuis le module 9-rectangle
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Classe Square qui hérite de Rectangle.

    Un carré est un cas spécial de rectangle où largeur = hauteur.
    Cette classe démontre l'héritage en chaîne :
    Square -> Rectangle -> BaseGeometry

    Attributes:
        __size (int): Taille du côté du carré (attribut privé)
    """

    def __init__(self, size):
        """
        Initialise un carré avec une taille de côté.

        Args:
            size (int): Taille du côté du carré (doit être un entier positif)

        Note:
            - Valide la taille avec integer_validator() héritée de BaseGeometry
            - Stocke la taille en attribut privé (__size)
            - Appelle le constructeur parent Rectangle avec size, size
            - super() permet d'appeler la méthode de la classe parente
        """
        # Validation du paramètre avec la méthode héritée
        self.integer_validator("size", size)

        # Stockage de la taille en attribut privé
        self.__size = size

        # Appel du constructeur parent avec size pour width et height
        super().__init__(size, size)
