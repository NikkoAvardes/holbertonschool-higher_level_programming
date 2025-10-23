#!/usr/bin/python3
"""
This module provides a safe way to filter states from a MySQL database.

The script connects to a MySQL server and displays all values in the states
table where the name matches the argument provided by the user. This version
is safe from MySQL injections by using parameterized queries instead of
string formatting. The results are sorted by states.id in ascending order.
This script takes 4 arguments: mysql username, mysql password, database name,
and state name to search for.
"""
import MySQLdb
import sys


def main():
    """
    Connect to MySQL server and safely filter states by name.

    This function establishes a connection to a MySQL database using
    command line arguments for credentials and database name. It then
    performs a secure query to find states matching the provided name
    using parameterized queries to prevent SQL injection attacks.
    The results are displayed in ascending order by state ID.

    Command line arguments:
        sys.argv[1]: MySQL username
        sys.argv[2]: MySQL password
        sys.argv[3]: Database name
        sys.argv[4]: State name to search for
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = db.cursor()

    state = sys.argv[4]

    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"

    cursor.execute(query, (state,))

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
