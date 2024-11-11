#This program is made by Bryan Liem. This part of the program imports StoreWorkerClasses.py for the classes and allows the
#user to add and edit worker data.

#Imports thhe necessary modules
import StoreWorkerClasses
import pickle

#Sets up the list of workers.
worker_list = []

#User input variable.
user_input = ''

#Opens WorkerData.pkl and prmpts the user if the list of workers should come from WorkerData.pkl. Only accepts "y" and "n" as valid arguments.
with open('WorkerData.pkl', 'rb') as file:
    while user_input != 'y' and user_input != 'n':
        user_input = input('There seems to be saved data. Would you like to open the file? Type "y" for yes and "n" for no. ').lower()
        if user_input == 'y':
            try:
                worker_list = pickle.load(file)
#A safeguard in case if WorkerData.pkl cannot be opened or not found.
            except EOFError:
                print('There was an error opening the file. File remains unopened.')

#Runs while the user input is not "q". Also makes every user's input lowercase.
while user_input != 'q':
    user_input = input('Input a command, type "help" for available commands: ').lower()

#Allows the user to create a new manager object.
    if user_input == 'create manager':
        manager_name = input('Give a name for the manager: ')
        manager_salary = int(input('Give a salary for the manager: '))
        worker_list.append(StoreWorkerClasses.Manager(manager_name, 0, [], manager_salary))
        print('Manager ' + manager_name + ' created.')

#Allows the user to create a new associate object.
    elif user_input == 'create associate':
        associate_name = input('Give a name for the associate: ')
        associate_pay = int(input('Give a salary for the manager: '))
        worker_list.append(StoreWorkerClasses.Associate(associate_name, 0, [], associate_pay))
        print('Associate ' + associate_name + ' created.')

#Allows the user to raise a manager's salary, given an ID and raise amount.
    elif user_input == 'raise manager':
        input_id = int(input('Input a manager\'s ID: '))
        for worker in worker_list:
            if worker.employee_number == input_id and type(worker) == StoreWorkerClasses.Manager:
                amount = int(input('Input a raise amount: '))
                worker.give_raise(amount)
                print(f'{worker.name}\'s raise increased to {worker.get_salary()}.')
            else:
                print(f'No manager exists in ID {input_id}.')

#Allows the user to raise an associate's wage, given an ID and raise amount.
    elif user_input == 'raise associate':
        input_id = int(input('Input an associate\'s ID: '))
        for worker in worker_list:
            if worker.employee_number == input_id and type(worker) == StoreWorkerClasses.Associate:
                amount = int(input('Input a raise amount: '))
                worker.give_raise(amount)
                print(f'{worker.name}\'s raise increased to {worker.get_hourly_rate()}.')
            else:
                print(f'No associate exists in ID {input_id}.')

#Allows the user to increase a manager's years, given an ID.
    elif user_input == 'increase manager years':
        input_id = int(input('Input a manager\'s ID: '))
        for worker in worker_list:
            if worker.employee_number == input_id and type(worker) == StoreWorkerClasses.Manager:
                worker.increase_years()
                print(f'{worker.name}\'s years increased.')
            else:
                print(f'No manager exists in ID {input_id}.')

#Allows the user to increase an associate's years, given an ID.
    elif user_input == 'increase associate years':
        input_id = int(input('Input an associate\'s ID: '))
        for worker in worker_list:
            if worker.employee_number == input_id and type(worker) == StoreWorkerClasses.Associate:
                worker.increase_years()
                print(f'{worker.name}\'s years increased.')
            else:
                print(f'No associate exists in ID {input_id}.')

#Allows the user to print a worker's info, given an ID.
    elif user_input == 'print employee info':
        input_id = int(input('Input a worker\'s ID: '))
        for worker in worker_list:
            if worker.employee_number == input_id:
                print(worker)
            else:
                print(f'No worker exists in ID {input_id}.')

#Allows the user to print the info of all workers.
    elif user_input == 'print all info':
        for worker in worker_list:
            print(worker)

#Allows the user to print a manager's salary, given an ID.
    elif user_input == 'print salary':
        input_id = int(input('Input a manager\'s ID: '))
        for worker in worker_list:
            if worker.employee_number == input_id and type(worker) == StoreWorkerClasses.Manager:
                print(f'{worker.name}\'s salary is {worker.get_salary()}.')
            else:
                print(f'No manager exists in ID {input_id}.')

#Allows the user to print an associate's wage, given an ID.
    elif user_input == 'print pay':
        input_id = int(input('Input an associate\'s ID: '))
        for worker in worker_list:
            if worker.employee_number == input_id and type(worker) == StoreWorkerClasses.Associate:
                print(f'{worker.name}\'s salary is {worker.get_salary()}.')
            else:
                print(f'No associate exists in ID {input_id}.')

#Prints the list of commands the user can use.
    elif user_input == 'help':
        print('\nAvailable commands:')
        print('create manager - Creates a new manager with a name and a salary.')
        print('create associate - Creates a new associate with a name and a salary.')
        print('raise manager - Gives a raise to a manager, provided an employee number.')
        print('raise associate - Gives a raise to an associate, provided an employee number.')
        print('increase manager years - Increases a manager\'s years, provided an employee number.')
        print('increase associate years - Increases an associate\'s years, provided an employee number.')
        print('print employee info - Prints employee\'s info, provided an employee number.')
        print('print all info - Prints the info of all employees.')
        print('print salary - Prints the weekly salary of a manager, provided an employee number.')
        print('print pay - Prints the weekly pay of an associate, provided an employee number.\n')

#Prints that a user's cammand cannot be used.
    elif user_input != 'q':
        print(user_input + ' is not an available command.')

#When user input is q, stores the worker_list data into a WorkerData.pkl file.
with open('WorkerData.pkl', 'wb') as file:
    pickle.dump(worker_list, file)


        
