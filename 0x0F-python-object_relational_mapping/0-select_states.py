#!/usr/bin/python3
""" MySQLdb provides a way db interact with python scripts
     lists all states from the database hbtn_0e_0_usa"""
import MySQLdb

db = MySQLdb.connect(host="localhost", port=3306, user="emma", passwd="emma", db="hbtn_0e_0_usa");

# prepare cursor object
cursor = db.cursor()

sql = "SELECT * FROM states ORDER BY states.id ASC"

try:
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        print(row)
except MySQLdb.Error as e:
    print(f"Error executing the SELECT quesry: {e}")
db.close()
