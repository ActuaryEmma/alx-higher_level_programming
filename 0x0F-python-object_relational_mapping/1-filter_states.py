#!/usr/bin/python3
""" MySQLdb provides a way db interact with python scripts
     lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
from sys import argv

if __name__ == '__main__':

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])

    # prepare cursor object
    cursor = db.cursor()

    sql = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id"

    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            print(row)
    except MySQLdb.Error as e:
        print(f"Error executing the SELECT quesry: {e}")
    db.close()
