#!/usr/bin/python3
"""takes in an argument and displays all values in the states table"""
import MySQLdb
import sys

if __name__ == "__main__":
    MY_HOST = "localhost"
    MY_USER = sys.argv[1]
    MY_PASS = sys.argv[2]
    MY_DB = sys.argv[3]
    MY_NAME = sys.argv[4]

    db = MySQLdb.connect(host=MY_HOST, user=MY_USER, passwd=MY_PASS,
                         db=MY_DB, port=3306, charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE states.name LIKE '{}' \
                ORDER BY states.id".format(MY_NAME))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    db.close()
    cur.close()
