#!/usr/bin/env python3

import sqlite3

# connect to a database
conn = sqlite3.connect("student.db")

# create a cursor
cursor = conn.cursor()

# create a table called students and insert values into it
cursor.execute("""CREATE TABLE student (
                first_name text,
                last_name text,
                email text,
                course text            
        )""")

# commit the database and table
conn.commit()

# close the connection to the database
conn.close()