import sqlite3

class Todo:
    def __init__(self):
        self.conn = sqlite3.connect('todo.db')
        self.c = self.conn.cursor()
        self.create_task_table()
        self.find_task()
        self.show_task()
    
    def create_task_table(self):
        self.c.execute('''CREATE TABLE tasks (
                       id INTEGER PRIMARY KEY,
                       name TEXT NOT NULL,
                       priority INTEGER NOT NULL
        );''')
    
    def add_task(self):
        name = input('Enter task name: ')
        priority = int(input("Enter priority: "))

        self.c.execute('INSERT INTO tasks (name, priority)')
    
    def find_task(self):
        None

    def show_task(self):
        
    
app = Todo()
app.add_task()
