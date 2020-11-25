#!/usr/bin/env python3

# import dependencies
import sqlite3 

# Query the DB and Return all RECORDs
def show_all():
    # Connect to database 
    conn = sqlite3.connect('insurance.db')
    
    # Create a cursor 
    cursor = conn.cursor()
    
    # select all rows from the test_data table
    cursor.execute("SELECT * FROM test_data")

    # get all items from what is executed
    items = cursor.fetchall()
    
    # loop through the items and display all items
    for item in items: 
        print(item)
        
    # save the execution
    conn.commit()

    # close the connection
    conn.close()
    
# Create a function that returns n rows for just females for the age, bmi, gender and kids column
def get_females(n):

    # connect to a database
    conn = sqlite3.connect("insurance.db")

    # create a cursor
    cursor = conn.cursor()

    # select rows where sex_male is either male or female
    cursor.execute("SELECT * FROM test_data WHERE sex_male = '0'")

    # fetchall rows in the table
    items = cursor.fetchmany(n)
    
    # format the columns output
    print("Age"+ "\t BMI"+ " \t Gender"+ "\t\tkids"+ "\n........................................." )

    #format the output of four columns for the first four rows
    for item in items:
        age, bmi, sex_male, _, _, _, _, kids = item
        print(f"{age}\t{bmi}\t {sex_male}\t\t{kids}")

    # commit changes
    conn.commit()

    # close connection
    conn.close()
    
# Create a function to delete one item given the row id
def delete_one(num): 
    # Connect to database 
    conn = sqlite3.connect('insurance.db')
    
    # Create a cursor 
    cursor = conn.cursor() 

    # delete item with rowid
    cursor.execute("DELETE from test_data WHERE rowid= 'num'")
    
    # commit changes
    conn.commit()

    # close connection
    conn.close()
    
# Create a function that returns n rows for just males for the age, bmi, gender and kids column
def get_males(n):

    # connect to a database
    conn = sqlite3.connect("insurance.db")

    # create a cursor
    cursor = conn.cursor()

    # select rows where sex_male is either male or female
    cursor.execute("SELECT * FROM test_data WHERE sex_male = '1'")

    # fetchall rows in the table
    items = cursor.fetchmany(n)
    
    # format the columns output
    print("Age"+ "\t BMI"+ " \t Gender"+ "\t\tkids"+ "\n........................................." )

    #format the output of four columns for the first four rows
    for item in items:
        age, bmi, sex_male, _, _, _, _, kids = item
        print(f"{age}\t{bmi}\t {sex_male}\t\t{kids}")

    # commit changes
    conn.commit()

    # close connection
    conn.close()
    
# create a function to display the age, bmi, gender and kids column for n rows
def four_columns_n_rows(n):
    # create an insurance database
    conn = sqlite3.connect("insurance.db")

    # create a cursor
    cursor = conn.cursor()

    # query table values
    cursor.execute("SELECT * FROM test_data")

    # get five rows from table
    items = cursor.fetchmany(n)

    # format the columns output
    print("Age"+ "\t BMI"+ " \t Gender"+ "\t\tkids"+ "\n........................................." )

    # format the output of four columns for the first four rows
    for item in items:
        age, bmi, sex_male, _, _, _, _, kids = item
        print(f"{age}\t{bmi}\t{kids}\t{sex_male}")

    # commit changes
    conn.commit()

    # close connection
    conn.close()
    
    
