import sqlite3

conn = sqlite3.connect('todo.db')
c = conn.cursor()
# execute CREATE TABLE in our database
# the execure method takes any single SQL statement and optional parameter necessary to execute the query
c.execute('''CREATE TABLE tasks ( 
          id INTEGER PRIMARY KEY,
          name TEXT NOT NULL,
          priority INTEGER NOT NULL
);''')