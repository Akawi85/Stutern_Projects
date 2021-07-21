#!/usr/bin/env python3

import sqlite3

# connect to a database
conn = sqlite3.connect("student.db")

# create a cursor
cursor = conn.cursor()

# Query table in database
cursor.execute("SELECT * FROM student")

# fetchall rows in the table
print(cursor.fetchall())

# print confirmation message
print("Command executed successfully...")

# commit the database and table
conn.commit()

# close the connection to the database
conn.close()