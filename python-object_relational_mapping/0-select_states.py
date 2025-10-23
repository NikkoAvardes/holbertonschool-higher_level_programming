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
    # Établir la connexion à la base de données MySQL
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],      # Nom d'utilisateur MySQL
        passwd=sys.argv[2],    # Mot de passe MySQL
        db=sys.argv[3]         # Nom de la base de données
    )

    # Créer un curseur pour exécuter les requêtes
    cur = db.cursor()

    # Exécuter la requête pour récupérer tous les états triés par ID
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")

    # Récupérer tous les résultats de la requête
    rows = cur.fetchall()

    # Afficher chaque ligne de résultat (tuple avec id et nom)
    for row in rows:
        print(row)

    # Fermer le curseur et la connexion pour libérer les ressources
    cur.close()
    db.close()


if __name__ == "__main__":
    # Exécuter seulement si le script est lancé directement
    main()
