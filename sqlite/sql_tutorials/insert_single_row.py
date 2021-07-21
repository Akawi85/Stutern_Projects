#!/usr/bin/env python3

import sqlite3

# connect to a database
conn = sqlite3.connect("student.db")

# create a cursor
cursor = conn.cursor()

# insert single rows into students table
cursor.execute("INSERT INTO student VALUES('Josiah', 'Oborekanhwo', 'josiahO@outlook.com', 'Data Science')")
cursor.execute("INSERT INTO student VALUES('Toyin', 'Olape', 'toyinolape@yahoo.com', 'Data Science')")

# check the new values
cursor.execute("SELECT * FROM student")

# print confirmation message
print("Command executed successfully...")

# commit the database and table
conn.commit()

# close the connection to the database
conn.close()