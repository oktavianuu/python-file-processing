import sqlite3

conn = sqlite3.connect('todo.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY, 
    name TEXT NOT NULL,
    priority INTEGER NOT NULL 
);''')
tasks = [
    ('My first task', 1),
    ('My second task', 5),
    ('My third task', 10),
]
c.executemany('INSERT INTO tasks (name, priority) VALUES (?, ?)', tasks)
conn.commit()
conn.close()

# note: by using executemany() method we can add as many tasks as we want at once.