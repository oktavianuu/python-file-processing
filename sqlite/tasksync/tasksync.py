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
                print("Please enter a valid number: ")
            
        while True:
            try:
                priority = int(input("Enter new priority: "))
                if priority < 1:
                    print("Priority must be at leat 1.")
                    continue
                break   
            except ValueError:
                print("Priority must be >= 1.")
        
        # check if task exist before updating
        self.c.execute('SELECT * FROM tasks WHERE id = ?', (user_id,))
        if not self.c.fetchone():
            print(f"No task found with ID {user_id}.")
            return
                
        # update priority
        self.c.execute("UPDATE tasks SET priority = ? WHERE id = ?", (priority, user_id))
        self.conn.commit()

        print(f"Priority for task ID {user_id} updated to {priority}.")

    def delete_task(self):
        try:
            task_id = int(input("Enter task ID to be deleted: "))
            self.c.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
            self.conn.commit()

            if self.c.rowcount > 0:
                print(f"Task {task_id} deleted successfully!")
            else:
                print(f"No task found with ID {task_id}.")
        
        except ValueError:
            print("Please enter a valid number.")

    def show_menu(self):
        """Display the main menu and handle user choice"""
        menu_options = {
            '1': ('Show All Tasks', self.show_tasks),
            '2': ('Add New Tasks', self.add_task),
            '3': ('Change Task Priority', self.change_priority),
            '4': ('Delete Task', self.delete_task),
            '5': ('Exit', None)
        }

        while True:
            print("n" + "="*40)
            print("              Task Sync Application")
            print("="*40)

            for key, (description, _) in menu_options.items():
                print(f"{key}. {description}")
            print("="*40)
        
            choice = input("Enter your choice (1-5): ")
            if choice == '5':
                print("Goodbye!")
                break
            elif choice in menu_options:
                method = menu_options[choice][1]
                if method:
                    try:
                        method()
                    except Exception as e:
                        print("Error {e}")
            else:
                print("Invalid choice! Please enter 1-5.")

if __name__ == "__main__":
    app = TaskSync()
    app.show_menu()
    app.conn.close()
    print("Database connection closed")