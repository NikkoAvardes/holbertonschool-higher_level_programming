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
    user_name = sys.argv[1]
    user_passwd = sys.argv[2]
    data_base = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=user_name,
        passwd=user_passwd,
        db=data_base
    )

    cur = db.cursor()
    query = ("SELECT * FROM states WHERE name = BINARY '{}' ORDER BY id ASC")
    cur.execute(query.format(state_name,))

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    main()
