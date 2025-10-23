#!/usr/bin/python3
"""
Filtre les états par nom fourni en argument (format string).

Usage: ./2-my_filter_states.py mysql_user mysql_password database state_name
"""

import MySQLdb
import sys


def main():
    """Se connecte à MySQL et affiche l'état correspondant au nom."""
    db = MySQLdb.connect(
        host='localhost',
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = '{}' ORDER BY id ASC"
                .format(sys.argv[4]))

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    main()
