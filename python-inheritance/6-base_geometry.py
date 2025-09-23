#!/usr/bin/python3
"""
Module qui contient la classe BaseGeometry avec la méthode area.
Cette classe définit une interface pour les objets géométriques.
"""


class BaseGeometry:
    """
    Classe de base pour les objets géométriques.

    Cette classe définit une méthode area() qui doit être
    implémentée par les sous-classes. C'est un exemple de
    méthode abstraite en Python.
    """

    def area(self):
        """
        Méthode abstraite pour calculer l'aire.

        Cette méthode doit être surchargée dans les sous-classes.
        Si elle est appelée directement, elle lève une Exception.

        Raises:
            Exception: Toujours, avec le message "area() is not implemented"

        Note:
            C'est un pattern courant en Python pour créer des méthodes
            abstraites avant l'introduction du module abc
            (Abstract Base Classes).
            Les sous-classes DOIVENT redéfinir cette méthode.
        """
        raise Exception("area() is not implemented")
