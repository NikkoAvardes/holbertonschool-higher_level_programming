#!/usr/bin/python3
"""
This module filters states from a MySQL database based on user input.

The script connects to a MySQL server and displays all values in the states
table where the name matches the argument provided by the user. This version
uses string formatting which makes it vulnerable to SQL injection attacks.
The results are sorted by states.id in ascending order.
"""

import MySQLdb
import sys


def main():
    """
    Connect to MySQL database and display states matching user input.

    This function takes command line arguments to connect to a MySQL server
    running on localhost at port 3306, then executes a SELECT query to find
    states with names matching the fourth argument. The query uses string
    formatting which creates a potential SQL injection vulnerability.
    """
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = '{}' "
                "ORDER BY id ASC".format(sys.argv[4]))

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    main()
