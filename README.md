# Modules, Libraries and Packages
## Specifically PYODBC

### Libraries
- Refer to python standard libraries
- They come standard with python but need to be imported

### Modules
- These are python files - like our MonsterStudent that we imported into our programs
- We create and import our own modules internally

### Packages
- These are external modules, that we need to install (externally) and then import them
- Allow us to do complex things easier and quicker because they are abstracted

##### These are modules usually written in OOP style, that abstract something

 - These things that are abstracted include:
    - Connection to a service (google maps or google image recognition api, price of stocks, price of bitcoin)
    - Tools and calculators (prime number calculator, other complex calculators)
    - Connections to databases or using HTTP protocols
    - Front-end tools like JS compiler or other things like scss
    - Full fledged frameworks
    
### Searching
- Google
- Look at good git repos
- https://pypi.org/
- Analyse if it's maintained and how/why you will use it
- Previous experience

### Installing
- pip - Python Package Manager (deals with dependencies and installs in virtual environment) - using command line
- Pycharm - you can just add to interpreter

### Using
- Import and call your functions
- Follow the documentation


## PYODBC
- This package allows us to connect to a DB :)


## Task
- As a user I can create a passenger
- As a user I can list all flights
- As a user I can add_passenger to flight

- Go to MS SQL Server and create table for:
    - Passenger
    - Flight
    - Planes
- These should have all the columns they need (first_name, last_name, passport_number)

- Add one data point to each table (3 inserts)

- Try to connect via your python project
