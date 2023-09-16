#!/usr/bin/python3
""" MySQLdb provides a way db interact with python scripts
     lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    if len(argv) != 4:
        print("Error")
        exit(1)

    username = argv[1]
    password = argv[2]
    database = argv[3]

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=username,
                         passwd=password,
                         db=database)

    # prepare cursor object
    cursor = db.cursor()

    sql = "SELECT cities.id, cities.name, states.name FROM cities  INNER JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC"

    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            print(row)
    except MySQLdb.Error as e:
        print(f"Error executing the SELECT quesry: {e}")
    db.close()
