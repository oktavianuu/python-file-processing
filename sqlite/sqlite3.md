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
    