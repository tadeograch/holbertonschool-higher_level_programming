#!/usr/bin/python3

import MySQLdb
import sys

MY_HOST = "localhost"
MY_USER = sys.argv[1]
MY_PASS = sys.argv[2]
MY_DB = sys.argv[3]

db = MySQLdb.connect(host=MY_HOST, user=MY_USER, passwd=MY_PASS, db=MY_DB)
cur = db.cursor()
cur.execute("SELECT cities.id, cities.name, states.name FROM cities \
             INNER JOIN states on cities.state_id=states.id ORDER BY id")
rows = cur.fetchall()
for row in rows:
    print(row)

if __name__ == "__main__":
    pass
