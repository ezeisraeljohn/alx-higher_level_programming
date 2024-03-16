#!/usr/bin/python3

""" The Module That connects to a MySQL Database and fetches some columns
    of a table of the database
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    conn = MySQLdb.connect(host='localhost', user=argv[1], passwd=argv[2],
                           db=argv[3], port=3306)
    cur = conn.cursor()

    cur.execute("""SELECT cities.id, cities.name, states.name
                   FROM cities
                   INNER JOIN states ON cities.state_id = states.id
                   ORDER BY cities.id ASC"""
                )

    cities = cur.fetchall()

    for city in cities:
        print(city)
