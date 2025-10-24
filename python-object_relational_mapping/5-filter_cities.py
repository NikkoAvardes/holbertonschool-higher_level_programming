#!/usr/bin/python3
"""Filter cities by state name from MySQL database.

This script connects to a MySQL server and displays all cities that belong
to a specific state. The state name is provided as a command line argument.
Uses parameterized queries to prevent SQL injection attacks.

Usage:
    python3 5-filter_cities.py <username> <password> <database> <state_name>

Arguments:
    username: MySQL username
    password: MySQL password
    database: Database name
    state_name: State name to filter cities by
"""
import MySQLdb
import sys


def main():
    """Connect to MySQL database and display cities filtered by state name.

    Retrieves command line arguments, establishes database connection,
    executes parameterized query to fetch cities by state name,
    and displays results in comma-separated format.
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

    query = ("SELECT cities.name FROM cities "
             "JOIN states ON cities.state_id = states.id "
             "WHERE states.name = %s ORDER BY states.id ASC")

    cur.execute(query, (state_name,))

    rows = cur.fetchall()

    cities = [row[0] for row in rows]
    print(", ".join(cities))

    cur.close()
    db.close()


if __name__ == "__main__":
    main()
