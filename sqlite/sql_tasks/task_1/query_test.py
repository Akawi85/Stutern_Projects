#!/usr/bin/env python3

# import dependencies
import sqlite3
import csv

# create an insurance database
conn = sqlite3.connect("insurance.db")

# create a cursor
cursor = conn.cursor()

# query table values
cursor.execute("SELECT * FROM test_data")

# get five rows from table
items = cursor.fetchmany(5)

# format the output of four columns for the first four rows
for item in items:
    age, bmi, sex_male, _, _, _, _, kids = item
    print(f"{age}\t{bmi}\t{kids}\t{sex_male:8}")

print("command executed successfully....")

# commit changes
conn.commit()

# close connection
conn.close()