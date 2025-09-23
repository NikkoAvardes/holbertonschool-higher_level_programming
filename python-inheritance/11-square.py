#!/usr/bin/python3
"""
Module qui contient la classe Square avec représentation personnalisée.
Cette classe implémente un carré avec affichage spécifique "[Square]".
"""

# Import de la classe Rectangle depuis le module 9-rectangle
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Classe Square qui hérite de Rectangle avec représentation personnalisée.

    Cette version surcharge __str__() pour afficher "[Square]"
    au lieu de "[Rectangle]".
    Un carré est un cas spécial de rectangle où largeur = hauteur.

    Chaîne d'héritage : Square -> Rectangle -> BaseGeometry
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
        """
        # Validation du paramètre avec la méthode héritée
        self.integer_validator("size", size)

        # Stockage de la taille en attribut privé
        self.__size = size

        # Appel du constructeur parent avec size pour width et height
        super().__init__(size, size)

    def __str__(self):
        """
        Retourne une représentation textuelle du carré.

        Returns:
            str: Description du carré au format "[Square] taille/taille"

        Note:
            Cette méthode surcharge __str__() de Rectangle pour afficher
            "[Square]" au lieu de "[Rectangle]". Selon la tâche 11,
            il faut afficher "[Square]" pour différencier du Rectangle.
        """
        return f"[Square] {self.__size}/{self.__size}"
