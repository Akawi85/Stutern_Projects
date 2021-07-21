#!/usr/bin/env python3

import sqlite3

# connect to a database
conn = sqlite3.connect("student.db")

# create a cursor
cursor = conn.cursor()

# Query table in database
cursor.execute("SELECT * FROM student")

# fetchall rows in the table
items = cursor.fetchall()

# format outputs to display in a tabular form
print("first_name"+ "\t Surname"+ "\tE-mail" "\t\t\t\t  Course \n........................................................" )

# loop through the items
for item in items:
    first_name, last_name, email, course = item
    print(f"{first_name:16}{last_name:16}{email}\t\t{course}")

# print confirmation message
print("Command executed successfully...")

# commit the database and table
conn.commit()

# close the connection to the database
conn.close()