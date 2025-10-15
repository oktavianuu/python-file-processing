import sqlite3

conn = sqlite3.connect('todo.db')
c = conn.cursor()
# execute CREATE TABLE in our database
# the execure method takes any single SQL statement and optional parameter necessary to execute the query
c.execute('''CREATE TABLE IF NOT EXISTS tasks ( 
          id INTEGER PRIMARY KEY,
          name TEXT NOT NULL,
          priority INTEGER NOT NULL
);''')
# Adding records
c.execute('INSERT INTO tasks (name, priority) VALUES (?, ?)', ('My first task', 1))
conn.commit() # confirm our changes, if we forget this, the change won't be visible in our db.
conn.close() # closes the database connection after inserting data
