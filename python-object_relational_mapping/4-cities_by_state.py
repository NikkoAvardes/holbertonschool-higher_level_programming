#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa.

This script connects to a MySQL server and displays all cities
sorted by their id in ascending order. Takes 3 arguments:
mysql username, mysql password, and database name.
"""
import MySQLdb
import sys


def main():
    """Connect to MySQL and display all cities ordered by id."""

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cur = db.cursor()

    query = ("SELECT cities.id, cities.name, states.name FROM cities "
             "JOIN states ON cities.state_id = states.id "
             "ORDER BY cities.id ASC")
    cur.execute(query)

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    main()
