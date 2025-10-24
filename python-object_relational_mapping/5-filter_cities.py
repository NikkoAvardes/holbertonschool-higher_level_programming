#!/usr/bin/python3
"""Filter cities by state name from the database."""
import MySQLdb
import sys


def main():
    """Connect to MySQL and display cities for a given state name."""
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
