#!/usr/bin/python3
"""
Module pour lister tous les états de la base de données hbtn_0e_0_usa.

Ce script se connecte à MySQL et récupère tous les états triés par ID.
Utilise MySQLdb pour la connexion à la base de données.
Arguments: mysql_username mysql_password database_name
"""

import MySQLdb
import sys


def main():
    """
    Fonction principale qui se connecte à MySQL et affiche tous les états.

    Prend 3 arguments de ligne de commande:
    - sys.argv[1]: nom d'utilisateur MySQL
    - sys.argv[2]: mot de passe MySQL
    - sys.argv[3]: nom de la base de données

    Affiche tous les états triés par states.id en ordre croissant.
    """
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cur = db.cursor()

    cur.execute("SELECT * FROM states ORDER BY id ASC")

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    main()
