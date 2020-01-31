import sqlite3
import csv

def init():

        # Open database file for querying
        database_file = sqlite3.connect('database_file.db')
        cursor = database_file.cursor()

        # TODO Create tables for movies and production companies
        cursor.execute('''
            
            CREATE TABLE IF NOT EXISTS movies (
            ID INT PRIMARY KEY NOT NULL,
            TITLE CHAR(100) NOT NULL,
            VOTE_AVERAGE REAL NOT NULL,
            REVENUE BIGINT NOT NULL 

            );
       ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS production_companies (
            REF_ID INT PRIMARY KEY NOT NULL,
            NAME CHAR(100) NOT NULL,
            LOCATION CHAR(100) NOT NULL,
            FOUNDER CHAR(100) NOT NULL,
            FOREIGN KEY(REF ID) REFERENCES movies (ID)

            );
        ''')

        # ADDING DATA TO MOVIES TABLE
        with open('Movies_Table.csv','rb') as fin: # `with` statement available in 2.5+
    	    # csv.DictReader uses first line in file for column headings by default
    	    dr = csv.DictReader(fin) # comma is default delimiter
    	    to_db = [(i['ID'], i['TITLE'], i['VOTE_AVERAGE'], i['REVENUE']) for i in dr]

        cur.executemany("INSERT INTO movies (ID, TITLE, VOTE_AVERAGE, REVENUE) VALUES (?, ?, ?, ?);", to_db)
        database_file.commit()


		# ADDING DATA TO COMPANIES TABLE
        with open('Companies_Table.csv','rb') as fin: # `with` statement available in 2.5+
    	    # csv.DictReader uses first line in file for column headings by default
    	    dr = csv.DictReader(fin) # comma is default delimiter
    	    to_db = [(i['REF_ID'], i['NAME'], i['LOCATION'], i['FOUNDER']) for i in dr]

        cur.executemany("INSERT INTO movies (REF_ID, NAME, LOCATION, FOUNDER) VALUES (?, ?, ?, ?);", to_db)
        database_file.commit()


#Functions for calling from parser

# get_category function receives the title of a movie and a requested column, and will print the requested column as a string
# For example, get_category("Titanic", "revenue" will query for the revenue of Titanic, and print "200000000"
# def get_category(title, category):
    # TODO will only work without table joins for attributes in the movies table.
    # TODO attributes in the production_companies table will require a join

# get_maximum receives an attribute of a movie, revenue or rating, and prints the highest value of that attribute, as well as the title of the movie
# def get_maximum(category)
