#!/usr/bin/python3
"""
Filter cities by state name from MySQL database.

This script connects to a MySQL database and displays all cities
that belong to a specific state. The state name is provided as
a command line argument. Uses parameterized queries to prevent
SQL injection attacks and displays results sorted by city ID.
Takes 4 arguments: username, password, database name, and state name.
"""
import MySQLdb
import sys


def main():
    """
    Connect to MySQL database and display cities for a given state name.

    Establishes connection to MySQL server, executes a parameterized query
    to find all cities belonging to the specified state, and displays
    the results in comma-separated format sorted by city ID.
    Uses command line arguments for database credentials and state name.
    """
    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT name FROM cities WHERE state_id = (SELECT id "
                   "FROM states WHERE name = %s) "
                   "ORDER BY cities.id", (sys.argv[4],))
    results = cursor.fetchall()

    cities = [row[0] for row in results]
    print(", ".join(cities))

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
