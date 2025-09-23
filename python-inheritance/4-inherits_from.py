#!/usr/bin/python3
"""
Module qui contient la fonction inherits_from.
Cette fonction vérifie si un objet hérite d'une classe spécifique
(mais n'est pas exactement cette classe).
"""


def inherits_from(obj, a_class):
    """
    Vérifie si l'objet hérite d'une classe spécifique.

    Args:
        obj: L'objet à vérifier
        a_class: La classe parent à vérifier

    Returns:
        bool: True si obj hérite de a_class (directement ou indirectement)
              mais n'est pas exactement a_class

    Note:
        Cette fonction combine issubclass() et type() :
        - issubclass(type(obj), a_class) : vérifie si la classe de obj
          est une sous-classe de a_class
        - type(obj) is not a_class : exclut la classe exacte
        Donc retourne True seulement si c'est une sous-classe.

    Exemple:
        inherits_from(True, int) -> True (bool hérite de int)
        inherits_from(1, int) -> False (1 est exactement un int)
        inherits_from(True, object) -> True (bool hérite d'object)
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
