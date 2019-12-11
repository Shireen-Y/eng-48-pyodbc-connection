import pyodbc
from db_connect_oop import *

class NWProducts(MSDBConnect):

    def __sql_query(self, sql_query): # Encapsulation makes it private, meaning it can only be called by other methods
        return self.cursor.execute(sql_query)

    def read_all(self):
        # Build our sql query
        query = 'SELECT * FROM Products'
        # Execute our query
        data = self.__sql_query(query)
        # Return an iterateable object
        return data

    def set_id(self):
        id = int(input('Select an ID: '))
        return id

# Read one - using ID
    def read_one(self, id):
        query = f"SELECT * FROM Products WHERE ProductID = {id} "
        result = self.__sql_query(query)
        return result.fetchone()

# Prints all the products using while loop and fetchone()
    def print_all(self):
        query = 'SELECT * FROM Products'
        data = self.__sql_query(query)
        while True:
            record = data.fetchone()
            if record is None:
                break
            print(record)

# Variable for NW product table
table_products = NWProducts()

# Getting all products
# products = table_products.read_all()
# print(products.fetchone())
#
# # Getting
# product = table_products.read_one()
# print(product)
#
# # Read all and print
# all_products = table_products.read_all()
# print(all_products.fetchone())
#
# while True:
#     record = all_products.fetchone()
#     if record is None:
#         break
#     print(record)
#


# List / read all

# Read one

# Create one --> makes this persistent in DB
# Ask for input --> frontend -- input()

# Update one

# Destroy one

