#This program is made by Bryan Liem. This part of the program creates three classes called StoreWorker, Manager, and associate.

#Creates a new class called StoreWorker that holds worker details.
class StoreWorker:
    emp_number = 1

#Declares instance variables for StoreWorker data.
    def __init__(self, newname, years=0, bonus_so_far=[]):
        self.name = newname
        self.employee_number = StoreWorker.emp_number
        self.years = years
        self.__bonus_so_far = bonus_so_far
        StoreWorker.emp_number += 1

#Declares special instructions on what to print out if the class variable is printed.
    def __str__(self):
        return (f'\nEmployee ID: {self.employee_number}\nName: {self.name}\nYears worked: {self.years}\nBonuses: {self.__bonus_so_far}\n')

#Increases the year of the worker by one if called.
    def increase_year(self):
        self.years += 1

#Returns the list of the bonus.
    def get_bonus(self):
        return f'Bonuses: {self.__bonus_so_far}'

#Returns the number of years worked.
    def get_years(self):
        return self.years

#Returns the worker number.
    def get_employee_number(self):
        return f'Employee ID: {self.employee_number}'

#Adds a specified valued into the bonus list.
    def give_bonus(self, amount):
        self.__bonus_so_far.append(amount)

#Creates a new class called Manager that holds manager details with inheritance from class StoreWorker.
class Manager(StoreWorker):

#Declares instance variables for Manager data. Note that some information is inherited from StoreWorker.
    def __init__(self, newname, years=0, bonus_so_far=[], weekly_salary=0):
        self.__weekly_salary = weekly_salary
        StoreWorker.__init__(self, newname, years, bonus_so_far)

#Declares special instructions on what to print out if the class variable is printed.
    def __str__(self):
        return (f'\nEmployee ID: {self.employee_number}\nManager name: {self.name}\nYears worked: {self.years}\nSalary: {self.__weekly_salary}\n')

#Returns the number of years worked. If the number of years is a multiple of 5, a bonus of 200 is added to the list.
    def increase_years(self):
        self.increase_year()
        if (self.years % 5 == 0):
            self.give_bonus(50)

#Adds a specified valued into the raise.
    def give_raise(self, amount):
        self.__weekly_salary += amount

#Returns the salary amount.
    def get_salary(self):
        return self.__weekly_salary

#Creates a new class called Associate that holds associate details with inheritancefrom class StoreWorker.
class Associate(StoreWorker):

#Declares instance variables for Associate data. Note that some information is inherited from StoreWorker.
    def __init__(self, newname, years=0, bonus_so_far=[], hourly_rate=0):
        self.__hourly_rate = hourly_rate
        StoreWorker.__init__(self, newname, years, bonus_so_far)

#Declares special instructions on what to print out if the class variable is printed.
    def __str__(self):
        return (f'\nEmployee ID: {self.employee_number}\nAssociate name: {self.name}\nYears worked: {self.years}\nHourly pay: {self.__hourly_rate}\n')

#Adds a specified valued into the wage.
    def give_raise(self, amount):
        self.__hourly_rate += amount

#Returns the number of years worked. Gives a bonus of 50 for every year passed.
    def increase_years(self):
        self.increase_year()
        self.give_bonus(50)

#Returns the hourly rate.
    def get_hourly_rate(self):
        return f'Hourly rate: {self.__hourly_rate}'

#Returns the weekly pay by multiplying the hourly rate by 40(hours).
    def calc_weekly_pay(self):
        return f'Weekly pay: {self.__hourly_rate * 40}'

        
