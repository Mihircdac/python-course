"""Database script:
    drop table new_schema.test ;
create table new_schema.test ( a integer);

select * from new_schema.test ;

insert into new_schema.test(a) values(1);
insert into new_schema.test (a) values(2);
insert into new_schema.test (a) values(3);
insert into new_schema.test (a) values(4);

commit;
select * from new_schema.test ;

update new_schema.test  set a = 9 where a= 1;

select * from new_schema.test ;

delete from new_schema.test where a=9

    """
# # Connecting to MySQL from Python

# MySQL is a powerful, open-source relational database management system (RDBMS). In many applications, you may need to connect to a MySQL database from a Python program to read, write, or update data. Python, being a versatile and widely-used language, provides several libraries that allow for smooth interaction with MySQL.

# ## Key Concepts

# ### 1. MySQL and Python Connection Libraries
# To connect Python with a MySQL database, you need a connector library that facilitates communication between your Python code and the MySQL database. **`mysql-connector-python`** is one such library provided by MySQL itself, which allows Python applications to access MySQL databases.

# **Why use `mysql-connector-python`?**
# - It’s the official MySQL connector, ensuring full compatibility with MySQL.
# - It supports Python’s database API (DB-API), a standard for Python database access.
# - It simplifies the connection process, allowing the execution of SQL queries from Python.

# ### 2. Connection Workflow

# Connecting to a MySQL database follows a specific workflow:

# #### 1. **Install the Connector**
#    Before you start working with MySQL, you need to install the `mysql-connector-python` package using `pip`:
#    
#    pip install mysql-connector-python




# #Basic Connection to MySQL and Select Query
# #This script demonstrates how to connect to your MySQL database and execute a simple SELECT query on the new_schema.test table you created.

# import mysql.connector

# # Establish connection to the MySQL database
# conn = mysql.connector.connect(
#     host="localhost",  # Assuming MySQL is hosted locally
#     user="user",  # Replace with your MySQL username
#     password="user",  # Replace with your MySQL password
#     database="new_schema"  # The schema where your table is
# )

# # Create a cursor to execute SQL queries
# cursor = conn.cursor()

# # Insert a new record into the table
# insert_query = "insert into test(a) values(%s);"
# cursor.execute(insert_query, (5,))

# # Commit the transaction to save the changes
# conn.commit()

# print("Data inserted successfully.")

# # Execute a simple SELECT query
# cursor.execute("SELECT * FROM test")

# # Fetch and print all the results
# results = cursor.fetchall()
# for row in results:
#     print(row)

# # Close the cursor and connection
# cursor.close()
# conn.close()


# # Using a Context Manager for Safe Connection Handling
# import mysql.connector

# # Define the connection parameters
# config = {
#     "host": "localhost",
#     "user": "user",
#     "password": "user",
#     "database": "new_schema"
# }

# # Using a context manager to handle the connection safely
# with mysql.connector.connect(**config) as conn:
#     with conn.cursor() as cursor:
#         # Execute a SELECT query
#         cursor.execute("SELECT * FROM test")
#         rows = cursor.fetchall()
        
#         # Print the results
#         for row in rows:
#             print(row)


# # Error Handling with MySQL Connection
# import mysql.connector
# from mysql.connector import Error

# try:
#     # Attempt to connect to the database
#     conn = mysql.connector.connect(
#         host="localhost",
#         user="user",
#         password="user",
#         database="new_schema"
#     )
    
#     if conn.is_connected():
#         print("Connected to MySQL database")
        
#         cursor = conn.cursor()
#         cursor.execute("SELECT * FROM test")
#         results = cursor.fetchall()

#         for row in results:
#             print(row)
    
# except Error as e:
#     print(f"Error: {e}")
    
# finally:
#     # Ensure that the connection is closed properly
#     if conn.is_connected():
#         cursor.close()
#         conn.close()
#         print("MySQL connection closed")



# # Using Pandas to Read Data from MySQL
import mysql.connector
import pandas as pd

# Establish the connection
conn = mysql.connector.connect(
    host="localhost",
    user="user",
    password="user",
    database="new_schema"
)

# Create a DataFrame from the SQL query
query = "SELECT * FROM test"
df = pd.read_sql(query, conn)

# Show the DataFrame
print(df)

# Close the connection
conn.close()
