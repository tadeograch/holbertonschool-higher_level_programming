#!/usr/bin/python3
"""
takes in the name of a state as an argument
and lists all cities of that state
"""
import MySQLdb
import sys

if __name__ == "__main__":
    MY_HOST = "localhost"
    MY_USER = sys.argv[1]
    MY_PASS = sys.argv[2]
    MY_DB = sys.argv[3]
    MY_C = sys.argv[4]

    db = MySQLdb.connect(host=MY_HOST, user=MY_USER, passwd=MY_PASS,
                         db=MY_DB, port=3306, charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities INNER JOIN states on states.name=%s \
                WHERE cities.state_id=states.id ORDER BY cities.id", (MY_C,))
    rows = cur.fetchall()
    rows = [i[0] for i in rows]
    if rows:
        for j in range(len(rows)):
            if j is len(rows) - 1:
                print("{}".format(rows[j]))
            else:
                print("{}, ".format(rows[j]), end="")
    else:
        print()
    db.close()
    cur.close()
