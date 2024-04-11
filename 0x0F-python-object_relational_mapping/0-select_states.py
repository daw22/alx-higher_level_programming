#!/usr/bin/python3
"""
a script that lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys


def main():
    """ main script """
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3])
    c = db.cursor()
    c.execute("""SELECT * FROM states ORDER BY id ASC""")
    results = c.fetchall()
    for item in results:
        print(item)
    c.close()
    db.close()


if __name__ == "__main__":
    main()
