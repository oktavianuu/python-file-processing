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
It's also possible to use a special name, ```:memory:```, which creates a database in RAM:
```python
import sqlite3

conn = sqlite3.connect(':memory:')
```
NOTE: Remember that the connect method creates a database only if it cannot find a database in the given location. If a database exists, SQLite connects to it.

#### A Few Words About SQL
You’ve already learned how to create a database in Python using the sqlite3 module. It's now time to discuss how we can create its structure. For this purpose, we’ll need some knowledge of SQL.

SQL is a Structured Query Language for creating, modifying, and managing relational databases. It’s used by the most popular database management systems such as MySQL, PostgreSQL, and our favorite SQLite. The SQL language was developed in the 70s by IBM. Over the years, SQL has been modified by many companies that have implemented it in their products. Therefore, it became necessary to introduce a standard that would standardize its syntax.

Since the first production deployments, the following standards have been created: SQL-86, SQL-89, SQL-92, SQL:1999, SQL:2003, SQL:2006, SQL:2008, SQL:2011, SQL:2016, SQL:2019. Detailed information on each of the standards can be found in the Internet resources. It’s worth mentioning that SQLite generally implements the SQL-92 standard, with some exceptions that we can read about here.

#### sqlite3 – the TODO application
Let's create a simple project called TODO, during which we’ll create a database to store tasks (to do) along with their priorities. The structure of our database will consist of only one table called ```tasks```. To create the table, we’ll need to use the SQL statement CREATE TABLE. Its syntax looks like this:
```SQL
CREATE TABLE table_name(
    column1 datatype,
    column2 datatype,
    column3 datatype,
    ...
    columnN datatype
);
```
The ```CREATE TABLE``` create a new table in the database. In our case, it will be a table called ```tasks``` consisting of three columns: ```id, name``` and ```priority```. 
The id column is a primary key that allows you to uniquely identify records stored in the table. The second column called name is responsible for storing the names of the tasks we’ll have to do. It's not difficult to guess that these will be textual values.

For this purpose, we’ll use the TEXT type. The last column called priority defines the priority of our tasks and should store integers.

Below is the SQL code that we’ll use later in the course to create our table using the sqlite3 module. Note the name and priority columns that contain the NOT NULL constraint. This will avoid creating tasks with fields equal to NULL.
```SQL
CREATE TABLE tasks(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    priority INTEGER NOT NULL
);
```

#### sqlite3 - inserting data
To insert data to our table, we'll use 'INSERT INTO' statement. Its syntax is as follow:
```python
INSERT INTO table_name (column1, column2, column3, ..., columnN)
VALUES (value1, value2, value3, ..., value4)
```
Using the above formula, we're able to prepare a query that will allow us to save our first task in the database:
```python
INSERT INTO tasks (id, name, priority) VALUES (1, 'My first task', 1);
```
or we can omitt id column 
```python
INSERT INTO tasks (name, priority) VALUES ('My first task', 1);
```
or omitt the columns name:
```python
INSERT INTO taks VALUES(value1, value2, ..., valueN)
```
This is how we do it:
```python
c.execute('INSERT INTO tasks (name, priority) VALUES (?, ?)', ('My first task', 1))
# The "?" characters will later be replaced by correct values during the execution of the statement. In the example above, 
# the first "?" character will be replaced by 'My first task' and the second "?" character will be replaced by 1
# this is to avoid SQL injection attack, which is malicious sql is appended to a query that could possibly 
# destroy our database
```
At this stage, we have not adding anything yet to our database. There are two steps remaining:
```conn.commit()``` and ```conn.close()``` methods provided by Connection object.
The ```commit``` method confirms our changes (the current transaction). If we forget to call it, our changes won't be visible in our database.
The ```close``` method is used to close the conneection of our database after inserting data.

#### the ```executemany()``` method
Imagine if we want to add three task to the database, if we use ```execute``` method, we need to do it separately three times. This is where ```executemany``` is useful. This method is provided by the ```Cursor``` object. 
The ```executemany``` method allows us to insert multiple records at once. As an argument, it accepts an SQL statement and an array containing any number of tuples.

#### Reading Data
The purpose of reading data is to display what is inside our database to the screen. In order to do that we need SQL statement called ```SELECT```.
The select statement allows us to read data from one or more tables. Its syntax looks like this:
```python
SELECT column FROM table_name;
```
Here, we decide to read the values saved in only one column. If we'd like to read only the names of the tasks save in in the ```tasks``` table we could use the following:
```python
SELECT name FROM tasks;
```
or
```python
SELECT column1, column2, column3, ..., columnN FROM table_name;
```
This allows us to read values from more columns. If we'd like to read the task names and their priorities, we could use the following query:
```python
SELECT name, priority FROM tasks;
```
or
```
SELECT * table_name;
```
If we don't have specific requirements, we can read the values from all.

#### Reading Data: continue
if we don't want to treat the ```Cursor``` object as an iterator, we can use its method called ```fetchall```. The ```fetchall``` methods fetches all records 