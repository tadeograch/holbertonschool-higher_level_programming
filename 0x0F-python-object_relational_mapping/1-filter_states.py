#!/usr/bin/python3
"""Lists all states with a name starting with N"""
import MySQLdb
import sys

if __name__ == "__main__":
    MY_HOST = "localhost"
    MY_USER = sys.argv[1]
    MY_PASS = sys.argv[2]
    MY_DB = sys.argv[3]
    db = MySQLdb.connect(host=MY_HOST, user=MY_USER, passwd=MY_PASS, db=MY_DB)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE states.name LIKE 'N%' \
                ORDER BY states.id")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    db.close()
    cur.close()
