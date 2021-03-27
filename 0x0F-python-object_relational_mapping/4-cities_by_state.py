#!/usr/bin/python3
"""Lists all cities from the database hbtn_0e_4_usa"""
import MySQLdb
import sys

if __name__ == "__main__":
    MY_HOST = "localhost"
    MY_USER = sys.argv[1]
    MY_PASS = sys.argv[2]
    MY_DB = sys.argv[3]

    db = MySQLdb.connect(host=MY_HOST, user=MY_USER, passwd=MY_PASS,
                         db=MY_DB, port=3306, charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities \
                INNER JOIN states on cities.state_id=states.id ORDER BY cities.id")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    db.close()
    cur.close()