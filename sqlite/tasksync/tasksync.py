import sqlite3

class TaskSync:
    def __init__(self):
        self.conn = sqlite3.connect('todo.db')
        self.c = self.conn.cursor()
        self.create_task_table()
    
    def create_task_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS tasks (
                       id INTEGER PRIMARY KEY,
                       name TEXT NOT NULL UNIQUE,
                       priority INTEGER NOT NULL CHECK(priority >= 1)
        );''')
        self.conn.commit()
    
    def add_task(self):
        name = input('Enter task name: ').strip() # remove leading/trailing whitespace
        if not name:
            print("The task name cannot be an empty string.")
            return 
    
        try:
            priority = int(input("Enter priority: "))
            if priority < 1:
                print("task priority must be at least 1.")
                return
        except ValueError:
            print("Priority must be a number.")
            return
        
        if self.find_task(name) is not None:
            print(" A task with the same name already exists.")
            return
        
        self.c.execute('INSERT INTO tasks (name, priority) VALUES (?, ?)', (name, priority))
        self.conn.commit()
        print("Task added successfully.")
    
    def find_task(self, task_name):
        self.c.execute('SELECT * FROM tasks WHERE name = ?', (task_name, ))
        return self.c.fetchone()
    
    def show_tasks(self):
        self.c.execute('SELECT * FROM tasks')
        tasks = self.c.fetchall()
        for task in tasks:
            print(task)

    def change_priority(self):
        # Get and validate ID
        while True:
            try:
                user_id = int(input("Enter the task ID: "))
                if user_id < 1:
                    print("ID must be a positive number")
                    continue # back to the start of the loop
                break # exit loop when valid
            except ValueError:
                print("Please enter a valid number.")
        
        # Get and validate priority
            try:
                priority = int(input("Enter new priority: "))
                if priority < 1:
                    print()
            
            except:



    def delete_task(self):
        pass

# functionality testing
app = Todo()
app.add_task()
app.add_task()

# app.find_task()

app.show_tasks()
# test finding a specific task

