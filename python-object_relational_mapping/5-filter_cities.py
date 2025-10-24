#!/usr/bin/python3
"""
Filter cities by state name from MySQL database.

This script connects to a MySQL server and displays all cities
that belong to a specific state. The state name is provided as
a command line argument. Uses parameterized queries to prevent
SQL injection attacks. Takes 4 arguments: mysql username,
mysql password, database name, and state name to filter by.
"""
import MySQLdb
import sys


def main():
    """Connect to MySQL and display cities filtered by state name."""
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
    )
    cur = db.cursor()

    state_name = sys.argv[4]

    query = ("SELECT cities.name FROM cities "
             "JOIN states ON cities.state_id = states.id "
             "WHERE states.name = %s ORDER BY cities.id ASC")

    cur.execute(query, (state_name,))

    rows = cur.fetchall()
    cities = [row[0] for row in rows]
    print(", ".join(cities))

    cur.close()
    db.close()


if __name__ == "__main__":
    main()
