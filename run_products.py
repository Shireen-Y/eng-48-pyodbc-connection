from db_products_oop import *

products_table = NWProducts()

while True:
    print('Choose 1 for getting all products')
    print('Choose 2 for getting 1 product')
    user_input = input('Choose 1 or 2: ').strip() # Removes trailing white spaces so it doesn't break

    if user_input == '1':
        products_table.print_all()

    elif user_input == '2':
        id = products_table.set_id()
        product = products_table.read_one(id)
        print(product)

    elif 'bye' in user_input or 'exit' in user_input:
        print('Goodbye! Thank you!')
        break

    else:
        print("I didn't quite catch that. Please choose an available option")
