#!/usr/bin/python3
"""
Module qui contient la fonction is_kind_of_class.
Cette fonction vérifie si un objet est une instance d'une classe
ou d'une classe qui en hérite.
"""


def is_kind_of_class(obj, a_class):
    """
    Vérifie si l'objet est une instance de la classe ou d'une classe dérivée.

    Args:
        obj: L'objet à vérifier
        a_class: La classe de base à vérifier

    Returns:
        bool: True si obj est une instance de a_class ou d'une sous-classe

    Note:
        isinstance() vérifie l'héritage : si obj est une instance de a_class
        ou de n'importe quelle sous-classe de a_class, retourne True.
        C'est différent de type() qui vérifie seulement la classe exacte.

    Exemple:
        is_kind_of_class(1, int) -> True
        is_kind_of_class(True, int) -> True (car bool hérite de int)
        is_kind_of_class(1, object) -> True (car tout hérite d'object)
    """
    return isinstance(obj, a_class)
