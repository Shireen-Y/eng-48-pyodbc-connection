from db_products_oop import *
from db_employees_oop import *

products_table = NWProducts()
employees_table = NWEmployees()
import time

while True:
    print('Choose 1 for getting all products')
    print('Choose 2 for getting 1 product')
    print('Choose 3 for searching a product')
    print('Choose 4 for getting all employees')
    print('Choose 5 for information on 1 employee')
    print('Choose 6 for searching an employee')
    print('Choose exit to exit')
    user_input = input('Choose an above option or exit: ').strip() # Removes trailing white spaces so it doesn't break

    if user_input == '1':
        products_table.print_all()
        time.sleep(0.7)

    elif user_input == '2':
        id = products_table.set_id()
        product = products_table.read_one(id)
        print(product)
        time.sleep(0.7)

    elif user_input == '3':
        products_table.product_name()
        time.sleep(0.7)

    elif user_input == '4':
        employees_table.print_all()
        time.sleep(0.7)

    elif user_input == '5':
        id = employees_table.set_id()
        employee = employees_table.read_one(id)
        print(employee)
        time.sleep(0.7)

    elif user_input == '6':
        employees_table.employee_name()
        time.sleep(0.7)

    elif 'bye' in user_input or 'exit' in user_input:
        print('Goodbye! Thank you!')
        break

    else:
        print("I didn't quite catch that. Please choose an available option")
