#!/usr/bin/python3
"""
Module qui contient la fonction lookup.
Cette fonction permet d'obtenir tous les attributs et méthodes d'un objet.
"""


def lookup(obj):
    """
    Retourne la liste des attributs et méthodes disponibles d'un objet.

    Args:
        obj: L'objet dont on veut lister les attributs et méthodes

    Returns:
        list: Liste des noms d'attributs et méthodes de l'objet

    Note:
        La fonction dir() est une fonction built-in de Python qui retourne
        tous les attributs et méthodes d'un objet, y compris ceux hérités.
        Elle est très utile pour l'introspection d'objets.
    """
    return (dir(obj))
