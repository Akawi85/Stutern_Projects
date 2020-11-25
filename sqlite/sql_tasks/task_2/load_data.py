#!/usr/bin/env python3

# import dependencies
import sqlite3
import csv

# create an insurance database
conn = sqlite3.connect("insurance.db")

# create a cursor
cursor = conn.cursor()

#create a table format and the data types
table = """CREATE TABLE test_data (age INTEGER, bmi FLOAT, sex_male INTEGER,
                                 smoker_yes INTEGER, region_northwest INTEGER,
                                  region_southeast INTEGER, region_southwest INTEGER, kids INTEGER)"""

# create the actual table
cursor.execute(table)

# get the test file
opened_file = open('test_data.csv')

# read the file 
read_file = csv.reader(opened_file)

# insert the values of the read file into the sql table
cursor.executemany("INSERT INTO test_data VALUES(?, ?, ?, ?, ?, ?, ?, ?)", read_file)

# commit the changes
conn.commit()

# close the connection
conn.close()