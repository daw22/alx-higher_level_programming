#!/usr/bin/python3

"""
a script that takes in the name of a state as an argument and lists
all cities of that state, using the database hbtn_0e_4_usa
"""

import MySQLdb
import sys


if __name__ == "__main__":
    argv = sys.argv
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3])
    c = db.cursor()
    c.execute("""SELECT name FROM cities
                 WHERE cities.state_id =
                 (SELECT id FROM states WHERE name LIKE BINARY %s)
                 ORDER BY id ASC""", (argv[4], ))
    cities = c.fetchall()
    for i in range(c.rowcount):
        city = cities[i][0]
        if i < (c.rowcount - 1):
            print(f"{city}, ", end="")
        else:
            print(city, end="")
    print()
    c.close()
    db.close()
