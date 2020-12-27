# Create and query SQL Database in Python

##### This project executes the basic SQL commands and performs some simple tasks in SQL using python scripts

A user is expected to run the `query_test.py` script first, followed by the `test_data_script.py` script last.

- The `test_data_script.py` script creates an sql database `insurance.db`
  - the script also creates a table in the database `test_data`, specifying columns of the expected data
  - the script goes further to insert a csv file `test_data.csv` into the sql table
- The `query_test.py` script connects to the database and extracts values from the table in the database