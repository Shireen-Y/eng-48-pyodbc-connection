import pyodbc

# These are our variables to connect
server = 'localhost,1433'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'

# Making the connection
docker_Northwind = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

# Making the cursor
cursor = docker_Northwind.cursor()

# Executing some SQL commands
cursor.execute("SELECT * FROM Customers WHERE city LIKE 'London'") # Execute a SQL query against the database
# Cursor will maitain state

# Fetching data from the executed SQL commands and printing
# fetchmany(size) = returns the number of rows specified by size argument
# Fetch single row (first one) from a result set, returns single tuple
# row = cursor.fetchone()
# print(row)

# fetchone() method
# Cursor maintaining state
# print(cursor.fetchone())
# print(cursor.fetchone())

# Accessing specific data or column
    # Use the column name as an attribute of the entry
# row = cursor.fetchone()
# print(row)
# print(row.CompanyName, row.ContactName)

# fetchall() - bad :(
# fetchall() = fetches all the rows of a query result, returns all the rows as a list of tuples
rows_all = cursor.fetchall()
print(rows_all)
print(len(rows_all))

for row in rows_all:
    print(row.ContactName, '-', row.CompanyName, '-', row.Fax)

# To get lots of data, use a while loop and fetchone at a time
rows = cursor.execute("SELECT * FROM Products")
while True:
    record = rows.fetchone()
    if record is None:
        break
    print(record.UnitPrice)