#!/usr/bin/python3
"""
a script that lists all cities from the database hbtn_0e_4_usa
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
    c.execute("""SELECT cities.id, cities.name, states.name
                 From cities
                 LEFT JOIN states ON cities.state_id = states.id
                 ORDER BY cities.id ASC""")
    cities = c.fetchall()
    for city in cities:
        print(city)
    c.close()
    db.close()
