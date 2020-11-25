#!/usr/bin/env python3

import sqlite3

# connect to a database
conn = sqlite3.connect("student.db")

# create a cursor
cursor = conn.cursor()

# Query table using the where clause
cursor.execute("SELECT * FROM student WHERE last_name ='Akawi'")

# fetchall rows in the table
items = cursor.fetchall()

# format outputs to display in a tabular form
print("first_name"+ "\t Surname"+ "\t E-mail"+ "                       Course"+ "\n........................................................" )

# loop through the items
for item in items:
    first_name, last_name, email, course = item
    print(f"{first_name:16}{last_name:16}{email}     {course}")

# print confirmation message
print("Command executed successfully...")

# commit the database and table
conn.commit()

# close the connection to the database
conn.close()