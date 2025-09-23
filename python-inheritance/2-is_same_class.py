#!/usr/bin/python3
"""
Module qui contient la fonction is_same_class.
Cette fonction vérifie si un objet est exactement une instance
d'une classe spécifique (pas d'héritage).
"""


def is_same_class(obj, a_class):
    """
    Vérifie si l'objet est exactement une instance de la classe spécifiée.

    Args:
        obj: L'objet à vérifier
        a_class: La classe à comparer

    Returns:
        bool: True si obj est exactement une instance de a_class, False sinon

    Note:
        Cette fonction utilise type() au lieu de isinstance() pour vérifier
        EXACTEMENT la classe, sans tenir compte de l'héritage.
        type(obj) retourne la classe exacte de l'objet.

    Exemple:
        is_same_class(1, int) -> True
        is_same_class(True, int) -> False (même si bool hérite de int)
    """
    return type(obj) is a_class
