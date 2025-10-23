#!/usr/bin/python3
import MySQLdb
import sys


def main():
    db = MySQLdb.connect(
        host='localhost',
        user=sys.argv[1],
        paswrd=sys.argv[2],
        db=sys.argv[3],
        search=sys.argv[4]
    )

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = ? ORDER BY id ASC")

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    main()
