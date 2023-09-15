#!/usr/bin/python3
""" MySQLdb provides a way db interact with python scripts
     lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys

if len(sys.argv) != 4:
    sys.exit(1)
username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]

db = MySQLdb.connect(host="localhost",
                     port=3306,
                     user="username", passwd="password", db="database")

# prepare cursor object
cursor = db.cursor()

sql = "SELECT * FROM states ORDER BY id ASC"

try:
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        print(row)
except MySQLdb.Error as e:
    print(f"Error executing the SELECT quesry: {e}")
db.close()
