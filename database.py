import sqlite3

# Open database file for querying
database_file = sqlite3.connect('database_file.db')
cursor = database_file.cursor()

# Create demo table
cursor.execute('''
    
    CREATE TABLE IF NOT EXISTS movies (
        title varchar(30),
        budget decimal(15),
        release date,
        revenue decimal(15) );
''')

# Add two demo rows to table
cursor.execute('''INSERT INTO movies VALUES ('Titanic', 200000000, '1997-12-19', 2187000000 );''')
cursor.execute('''INSERT INTO movies VALUES ('Avatar', 12345, '2009-01-01', 1234567 );''')

# Select all table rows
command = '''SELECT title, revenue FROM movies; '''
print (command)
for row in cursor.execute(command): #WHERE title='Titanic'
    print (row)

#cursor.execute('''DROP TABLE movies;''');

database_file.close()
