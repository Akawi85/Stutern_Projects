#!/usr/bin/env python3
"""
Author : Me <Ifeanyi.akawi85@gmail.com>
Date   : today
Purpose: Greet the User and Provide His/Her Detailed Age Information

Note: The shebang line (first line) tells the OS which
program to use to execute this program, in this case python3.
"""

# We must import the argparse module to use it.
import argparse  

""" 
Define a get_args function that holds all the command-line
arguments we need for the program to work
"""
def get_args():
    
    """
    The parser below will figure out
    all the arguments. The
    description appears in
    the help message.
    """
    parser = argparse.ArgumentParser(
        description='Tell Us A Little About You',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    """
    Below, We need to tell the parser to
    expect a required name argument that will be the
    object of our salutations.
    """
    parser.add_argument('name',
                        metavar='name',
                        help='Its a must you type in your name',
                        type=str,
                        nargs='+')

    """
    Below, We need to tell the parser to
    expect a required age argument
    """
    parser.add_argument('age',
                        help='Its a must you type in your age too',
                        metavar='age',
                        type=int)

    """
    We ask the parser to parse any
    arguments to the program.
    """
    return parser.parse_args()


# --------------------------------------------------
def main():
    """The main program is written here"""

    args = get_args() # assign the get_args() function to args variable


    dob = (2020 - args.age)  # get the user's date of birth
    age_group = str()  # create a variable that will hold the user's age group
    year = 'years'  # define a year string

    """
    Generate conditions for age grouping
    """
    if args.age <= 1:
        age_group = 'Infant'
        year = year.replace('s', '') # if user age is less than one, say 'year' not 'years' old
    elif args.age <= 11:
        age_group = 'Child'
    elif args.age <= 17:
        age_group = 'Teen'
    elif (args.age >= 18) & (args.age <= 64):
        age_group = 'Adult'
    elif args.age >= 65:
        age_group = 'Elder'

    """choose the correct article to classify age group"""
    article = f'an' if age_group[0].lower() in 'aeiou' else 'a' 


    """Get past, current and future age"""
    decade_ago = (2020 - 10) # Year decade ago
    age_decade_ago = (args.age - 10) # age decade ago
    current_year = 2020 # Current year


    """Print User Details"""
    print(f'Hello', f' '.join(args.name), f'you are {args.age} {year} old!') # greet the user, tell his age
    print(f'You were born in the year {dob}.') # Tell the user his/her date of birth 
    print(f'You are {article} {age_group}.') # Tell the user his age group for his current age
    print(f'In {decade_ago}, you were {age_decade_ago}') # Tell the user his age a decade ago


    """Print user age for the next 50 years"""
    print(f'In {current_year + 10}, you will be {args.age + 10}') # Tell the user his age in ten years time
    print(f'In {current_year + 20}, you will be {args.age + 20}') # Tell the user his age in twenty years time
    print(f'In {current_year + 30}, you will be {args.age + 30}') # Tell the user his age in thirty years time
    print(f'In {current_year + 40}, you will be {args.age + 40}') # Tell the user his age in forty years time
    print(f'In {current_year + 50}, you will be {args.age + 50}') # Tell the user his age in fifty years time

"""
Every program or module in Python has a
name that can be accessed through the
variable __name__. When the program is
executing, __name__ is set to “__main__”.
If this is true, call the main() function
"""
if __name__ == '__main__':
    main()
