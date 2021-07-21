#!/usr/bin/env python3

import sqlite3

# connect to a database
conn = sqlite3.connect("student.db")

# create a cursor
cursor = conn.cursor()

# Query table using the update, set and where clauses
cursor.execute("UPDATE student SET first_name = 'Courage' WHERE last_name ='Akawi'") # Note that updating values using column names is bad practice as it will alter all values where the condition is met 

# commit the update
conn.commit()

# check the updated table
cursor.execute("SELECT * FROM student WHERE first_name = 'Courage'")

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