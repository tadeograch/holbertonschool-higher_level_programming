#!/usr/bin/python3
'''Lists all states from the database hbtn_0e_0_usa'''

import MySQLdb
import sys

MY_HOST = "localhost"
MY_USER = sys.argv[1]
MY_PASS = sys.argv[2]
MY_DB = sys.argv[3]

if __name__ == "__main__":

    db = MySQLdb.connect(host=MY_HOST, user=MY_USER, passwd=MY_PASS, db=MY_DB, port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    db.close()
    cur.close()
