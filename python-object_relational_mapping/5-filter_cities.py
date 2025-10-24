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
