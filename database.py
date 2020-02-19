import sqlite3
import csv

class Database:
        def load_data(self):
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
                try:
                    with open('Companies_Table.csv','r') as fin: # `with` statement available in 2.5+
                        # csv.DictReader uses first line in file for column headings by default
                        dr = csv.DictReader(fin) # comma is default delimiter
                        to_db = [(i['ref_id'], i['name'], i['location'], i['founder']) for i in dr]
                except FileNotFoundError:
                    print("Companies data not available\n")
                    return(1)

                self.cursor.executemany("INSERT INTO production_companies (ref_id, name, location, founder) VALUES (?, ?, ?, ?);", to_db)
                self.database_file.commit()

                # Adding data to movies table
                try:
                    with open('Movies_Table.csv','r') as fin: # `with` statement available in 2.5+
                        # csv.DictReader uses first line in file for column headings by default
                        dr = csv.DictReader(fin) # comma is default delimiter
                        to_db = [(i['id'], i['title'], i['vote_average'], i['revenue']) for i in dr]
                except FileNotFoundError:
                    print("Movies data not available\n")
                    return(1)

                self.cursor.executemany("INSERT INTO movies (id, title, vote_average, revenue) VALUES (?, ?, ?, ?);", to_db)
                self.database_file.commit()
                return(0)

        # Functions for calling from parser
        def print_all_titles(self):
            for row in self.cursor.execute('''SELECT title FROM movies;'''):
                print(row[0])
            print("Search finished\n")

        def print_all_companies(self):
            for row in self.cursor.execute('''SELECT name FROM production_companies;'''):
                print(row[0])
            print("Search finished\n")

        def get_vote_average(self, title):
            for row in self.cursor.execute("SELECT vote_average FROM movies WHERE title = :title", (title,)):
                print(row[0])
                print("Search finished\n")

        def get_revenue(self, title):
            for row in self.cursor.execute("SELECT revenue FROM movies WHERE title = :title", (title,)):
                print(row[0])
                print("Search finished\n")

        def get_proco_name(self, title):
            for row in self.cursor.execute("SELECT name FROM production_companies JOIN movies ON movies.id = production_companies.ref_id WHERE title = :title", (title,)):
                print(row[0])
                print("Search finished\n")

        def get_proco_founder(self, title):
            for row in self.cursor.execute("SELECT founder FROM production_companies JOIN movies ON movies.id = production_companies.ref_id WHERE title = :title", (title,)):
                print(row[0])
                print("Search finished\n")

        def get_proco_location(self, title):
            for row in self.cursor.execute('''SELECT location FROM movies JOIN production_companies ON production_companies.ref_id = movies.id WHERE title="''' + str(title) + '";'):
                print(row[0])
                print("Search finished\n")

        def get_max_revenue(self):
            for row in self.cursor.execute('''SELECT title, MAX(revenue) FROM movies;'''):
                print(str(row[0]) + ", " + str(row[1]))
                print("Search finished\n")

        def get_max_rating(self):
            for row in self.cursor.execute('''SELECT title, MAX(vote_average) FROM movies;'''):
                print(str(row[0]) + ", " + str(row[1]))
                print("Seach finished\n")
