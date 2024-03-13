import sqlite3

conn = sqlite3.connect('todo.db')
c = conn.cursor()
c.execute('''CREATE TABLE tasks (
          id INTEGER PRIMARY KEY,
          name TEXT NOT NULL,
          priority INTEGER NOT NULL
);''')