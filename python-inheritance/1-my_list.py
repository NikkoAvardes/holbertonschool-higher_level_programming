#!/usr/bin/python3
"""
Module qui contient la classe MyList.
Cette classe hérite de la classe built-in list et ajoute une méthode
pour afficher la liste triée sans modifier l'original.
"""


class MyList(list):
    """
    Classe qui hérite de list et ajoute une méthode print_sorted.

    Cette classe démontre l'héritage simple où on étend les fonctionnalités
    d'une classe existante (list) en ajoutant de nouvelles méthodes.
    Toutes les méthodes de list sont disponibles (append, extend, etc.).
    """

    def print_sorted(self):
        """
        Affiche la liste triée par ordre croissant.

        Cette méthode ne modifie pas la liste originale, elle crée
        une copie triée temporaire pour l'affichage seulement.
        La fonction sorted() retourne une nouvelle liste triée.
        """
        print(sorted(self))
