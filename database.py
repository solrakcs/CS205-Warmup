import sqlite3

def init():

        # Open database file for querying
        database_file = sqlite3.connect('database_file.db')
        cursor = database_file.cursor()

        # TODO Create tables for movies and production companies
        cursor.execute('''
            
            CREATE TABLE IF NOT EXISTS movies (

            )
       ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS production_companies (

            )
        ''')

        # TODO Add data to both tables
        #cursor.execute('''INSERT INTO movies VALUES ('Avatar', 12345, '2009-01-01', 1234567 );''')

#Functions for calling from parser

# get_category function receives the title of a movie and a requested column, and will print the requested column as a string
# For example, get_category("Titanic", "revenue" will query for the revenue of Titanic, and print "200000000"
# def get_category(title, category):
    # TODO will only work without table joins for attributes in the movies table.
    # TODO attributes in the production_companies table will require a join

# get_maximum receives an attribute of a movie, revenue or rating, and prints the highest value of that attribute, as well as the title of the movie
# def get_maximum(category)
