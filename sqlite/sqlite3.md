#### Creating a Database
SQLite database is a single file, saved in our computer.Each file, regardless of the operating system used, has its location (a path to a specific disk space). When you create a database, you can create it in your current working directory, or in any other location. To create a database, use the ```connect``` method provided by the sqlite3 module:
```python
import sqlite3

conn = sqlite3.connect('hello.db')
```
The ```connect``` method returns the database representation as a Connection object. In the example above, the method takes only the database name as the argument. This means that the database will be created in the same directory as the script that wants to access it. If we'd like to create a database in the sqlite3 directory on your C disk you can do this as follows:
```python  
import sqlite3

conn = sqlite3.connect('C:\sqlite\hello.db')
```
It's also possible to use a special name, :memory:, which creates a database in RAM:

