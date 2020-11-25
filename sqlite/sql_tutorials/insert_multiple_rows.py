#!/usr/bin/env python3

import sqlite3

# connect to a database
conn = sqlite3.connect("student.db")

# create a cursor
cursor = conn.cursor()

# create rows to input into the table called students in the student database
student_list = [("Ifeanyi", "Akawi", "ifeanyi.akawi85@gmail.com", "Data Science"),
                ("Toyin", "Olape", "toyinolape@yahoo.com", "Data Science"),
                ("Josiah", "Oborekanhwo", "josiahO@outlook.com", "Data Science"),
                ("Mayowa", "Kolawole", "mayorkay@aol.com", "Data Science")
                ]

# insert the multiple rows into the students table
cursor.executemany("INSERT INTO student VALUES(?, ?, ?, ? )", student_list)

# print confirmation message
print("Command executed successfully...")

# commit the database and table
conn.commit()

# close the connection to the database
conn.close()