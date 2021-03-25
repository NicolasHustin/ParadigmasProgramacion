from View.MainView import *
from DataBase import saveCustomer, saveEmployee, getCustostomer, getRentedObjects

class Controller():

    def addEmployee():
        ''' return the employee data '''
        ciEmployee, newEmployee = View.aggEmployee()
        saveEmployee(ciEmployee, newEmployee)

    def generalInquiry():
        View.
    