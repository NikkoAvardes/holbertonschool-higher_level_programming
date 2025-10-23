#!/usr/bin/python3
"""
Liste tous les états commençant par 'N' de la base hbtn_0e_0_usa.

Usage: ./1-filter_states.py mysql_user mysql_password database_name
"""

import MySQLdb
import sys


def main():
    """Se connecte à MySQL et affiche les états commençant par 'N'."""
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    main()
