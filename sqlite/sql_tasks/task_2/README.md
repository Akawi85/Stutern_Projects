# Create and query SQL Database in Python

##### This project executes the basic SQL commands and performs some simple tasks in SQL using python scripts

A user is expected to run the `load_data.py` script first, followed by the `insurance_app.py` script and finally call the functions in the `call_function.py` script.

- The `load_data.py` script creates an sql database `insurance.db`
  - the script also creates a table in the database `test_data`, specifying data types of the columns of the expected data
  - the script goes further to insert a csv file `test_data.csv` into the sql table
- The `insurance_app.py` script connects to the database and extracts values from the table in the database, specifically, the scrip does the following:
   - creates a function that outputs all the values from all columns in the table
   - creates a function that shows values for a given number of females in the table and displays the results in a columnar format
   - creates a function that shows values for a given number of males in the table and displays the results in a columnar format
   - creates a function that deletes one row from the table given the row id
   - creates a function that shows four columns for a given number of rows in the table and displays the results in a columnar format
- The `call_function.py` script expects a user uncomment a particular line he/she wishes to see its functioning and pass an integer argument to the function call.



