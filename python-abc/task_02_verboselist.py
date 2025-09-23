#!/usr/bin/env python3
"""
Extending the Python List with Notifications

Ce module démontre l'extension d'une classe intégrée de Python (list)
pour ajouter des fonctionnalités de notification lors des modifications.
"""


class VerboseList(list):
    """
    Classe VerboseList qui étend la classe list intégrée de Python.

    Cette classe ajoute des notifications à chaque fois qu'un élément
    est ajouté ou supprimé de la liste, tout en conservant toutes
    les fonctionnalités de la liste standard.
    """

    def append(self, item):
        """
        Ajoute un élément à la fin de la liste et affiche une notification.

        Args:
            item: L'élément à ajouter à la liste
        """
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """
        Étend la liste avec les éléments d'un itérable et
        affiche une notification.

        Args:
            iterable: L'itérable contenant les éléments à ajouter
        """
        super().extend(iterable)
        print(f"Extended the list with [{len(iterable)}] items.")

    def remove(self, value):
        """
        Supprime la première occurrence d'une valeur et affiche
        une notification.

        Args:
            value: La valeur à supprimer de la liste

        Raises:
            ValueError: Si la valeur n'est pas trouvée dans la liste
        """
        super().remove(value)
        print(f"Removed [{value}] from the list.")

    def pop(self, index=-1):
        """
        Supprime et retourne un élément à l'index donné avec notification.

        Args:
            index (int): L'index de l'élément à supprimer.
                        Par défaut -1 (dernier élément)

        Returns:
            L'élément supprimé de la liste

        Raises:
            IndexError: Si l'index est hors limites
        """
        item = super().pop(index)
        print(f"Popped [{item}] from the list.")
        return item
