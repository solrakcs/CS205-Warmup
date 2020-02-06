import sqlite3
import csv

class Database:
        def __init__(self):
                # Open database file for querying
                self.database_file = sqlite3.connect('database_file.db')
                self.cursor = self.database_file.cursor()

                self.cursor.execute('''DROP TABLE movies;''')
                self.cursor.execute('''DROP TABLE production_companies;''')

                # Production companies
                self.cursor.execute('''
                    CREATE TABLE IF NOT EXISTS production_companies (
                        ref_id INT NOT NULL,
                        name CHAR(100) NOT NULL,
                        location CHAR(100) NOT NULL,
                        founder CHAR(100) NOT NULL,
                        PRIMARY KEY (ref_id)
                    );
                ''')

                # Movies
                self.cursor.execute('''
                    CREATE TABLE IF NOT EXISTS movies (
                    id INT NOT NULL,
                    title CHAR(100) NOT NULL,
                    vote_average REAL NOT NULL,
                    revenue BIGINT NOT NULL,
                    PRIMARY KEY (title),
                    FOREIGN KEY(id) REFERENCES production_companies (ref_id)
                    );
                ''')

                # Adding data to companies table
                with open('Companies_Table.csv','r') as fin: # `with` statement available in 2.5+
                    # csv.DictReader uses first line in file for column headings by default
                    dr = csv.DictReader(fin) # comma is default delimiter
                    to_db = [(i['ref_id'], i['name'], i['location'], i['founder']) for i in dr]

                self.cursor.executemany("INSERT INTO production_companies (ref_id, name, location, founder) VALUES (?, ?, ?, ?);", to_db)
                self.database_file.commit()

                # Adding data to movies table
                with open('Movies_Table.csv','r') as fin: # `with` statement available in 2.5+
                    # csv.DictReader uses first line in file for column headings by default
                    dr = csv.DictReader(fin) # comma is default delimiter
                    to_db = [(i['id'], i['title'], i['vote_average'], i['revenue']) for i in dr]

                self.cursor.executemany("INSERT INTO movies (id, title, vote_average, revenue) VALUES (?, ?, ?, ?);", to_db)
                self.database_file.commit()
    
        # Functions for calling from parser
        def print_all_titles(self):
            for row in self.cursor.execute('''SELECT title FROM movies;'''):
                print(row[0])

        def print_all_companies(self):
            for row in self.cursor.execute('''SELECT name FROM production_companies;'''):
                print(row[0])

        



        # get_category function receives the title of a movie and a requested column, and will print the requested column as a string
        # For example, get_category("Titanic", "revenue" will query for the revenue of Titanic, and print "200000000"
        # def get_category(title, category):
            # TODO will only work without table joins for attributes in the movies table.
            # TODO attributes in the production_companies table will require a join

        # get_maximum receives an attribute of a movie, revenue or rating, and prints the highest value of that attribute, as well as the title of the movie
        # def get_maximum(category)
