#!/usr/bin/env python3
"""
Abstract Animal Class and its Subclasses

Ce module démontre l'utilisation des classes abstraites en Python avec
le module ABC.
Une classe abstraite sert de modèle pour d'autres classes et
 ne peut pas être instanciée directement.
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Classe abstraite Animal qui sert de base pour tous les animaux.

    Cette classe hérite d'ABC (Abstract Base Class) et définit une
    méthode abstraite
    que toutes les sous-classes doivent implémenter.
    """

    @abstractmethod
    def sound(self):
        """
        Méthode abstraite qui doit être implémentée par toutes les
        sous-classes.

        Returns:
            str: Le son que fait l'animal
        """
        pass


class Dog(Animal):
    """
    Classe Dog qui hérite d'Animal.
    Représente un chien avec son comportement spécifique.
    """

    def sound(self):
        """
        Implémentation concrète de la méthode sound pour un chien.

        Returns:
            str: "Bark" - le son que fait un chien
        """
        return ("Bark")


class Cat(Animal):
    """
    Classe Cat qui hérite d'Animal.
    Représente un chat avec son comportement spécifique.
    """

    def sound(self):
        """
        Implémentation concrète de la méthode sound pour un chat.

        Returns:
            str: "Meow" - le son que fait un chat
        """
        return ("Meow")
