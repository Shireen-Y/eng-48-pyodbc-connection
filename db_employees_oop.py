import pyodbc
from db_connect_oop import *

class NWEmployees(MSDBConnect):

    def __sql_query(self, sql_query): # Encapsulation makes it private, meaning it can only be called by other methods
        return self.cursor.execute(sql_query)

    # Get all employees data
    def print_all(self):
        query = 'SELECT * FROM Employees'
        data = self.__sql_query(query)
        while True:
            record = data.fetchone()
            if record is None:
                break
            print(record)
        return 'All done!'

    # Get one employee by id
    def set_id(self):
        id = int(input('Select an ID: '))
        return id

    def read_one(self, id):
        query = f"SELECT * FROM Employees WHERE EmployeeID = {id} "
        result = self.__sql_query(query)
        return result.fetchone()

    # Search for one employee by first name or last name
    def employee_name(self):
        name = input('What is the name of the employee? ')
        query = f"SELECT * FROM Employees WHERE FirstName LIKE '%{name}%' OR LastName LIKE '%{name}%'"
        data = self.__sql_query(query)
        while True:
            record = data.fetchone()
            if record is None:
                break
            print(record)
        return 'All done!'

table_employees = NWEmployees()
# data_employees = table_employees.print_all()
# print(data_employees)

# employee = table_employees.read_one(id)
# print(employee)

# name_employee = table_employees.employee_name()
# print(name_employee)



## Add all this amazing functionality to our run_products while loop