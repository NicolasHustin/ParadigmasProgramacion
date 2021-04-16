import os
from Person import Customer, Employee
from View.ViewUtils import *
from AppController import *


class View():

    
    @staticmethod
    def cleanScreen():
        '''Function for clear screen'''
        os.system('cls' if os.name =='nt' else 'clear')

    @staticmethod
    def validateOperation(min, max):
        '''Function for validate input operations'''
        value = input("[{}] al [{}] -->> ".format(min, max))
        try:
            valor = int(valor)
            if(valor <= max and valor >= min):
                return valor
            else:
                raise (ValueError)
        except ValueError:
            print('\n['+str(valor)+'] Is not a valid option... please try again;')

    def aggEmployee():
        View.cleanScreen()
        print('--'*45)
        print('\n\n\t\tINGRESE LOS DATOS DEL EMPLEADO\n')
        while True:
            try:
                name = input('\t\tNOMBRE: ')
                lastName = input('\t\tAPELLIDO: ')
                ciEmployee = input('\t\tCEDULA: ')
                salary = int(input('\t\tSUELDO: '))
                address = input('\t\tDIRECCION: ')
                telephone = input('\t\tTELEFONO: ')
                print('--'*45)
                newEmployee = Employee(salary, name=name, lastName=lastName, ci=ciEmployee, address=address, telephone=telephone)
                Controller.addEmployee(ciEmployee, newEmployee)
                print('\nEmpleado [{}] con nombre: {} guardado con exito!'.format(ciEmployee, newEmployee.getName()))
            except Exception as e:
                print('\nError in addEmployee: -> ', e)

    def generalInquiry():
        operationInquiry = 0
        while(operationInquiry != 4):
            View.cleanScreen()
            operationInquiry = 0
            print('--'*45)
            print('\n\tCONSULTAS GENERALES')
            print('\n\n1) CONSULTA EMPLEADOS')
            print('2) CONSULTA ARTICULOS')
            print('3) CONSULTA CLIENTES')
            print('4) VOLVER \n\n')
            print('--'*45)
            operationInquiry = int(input('Ingrese una opcion [1 al 4]: '))
            if(operationInquiry==1):
                typeEmployee = 0
                while(typeEmployee != 3):
                    typeEmployee = View.typeEmployee()
                    #QUERY FOR ID
                    if(typeEmployee == 1):
                        View.cleanScreen()
                        ciEmployee = View.employeeInquity()
                        employee = Controller.employeeInquiry(ciEmployee)
                        print(employee)
                        pauseProcess()
                    #A GENERAL QUERY 
                    if(typeEmployee == 2):
                        View.cleanScreen()
                        listOfEmployees = Controller.getGeneralEmployees()
                        print('\n')
                        for empl in listOfEmployees:
                            print('--'*45)
                            print(empl)
                            print('--'*45)
                        pauseProcess()
            if(operationInquiry == 2):
                typeArticle = 0
                while (typeArticle != 3):
                    typeArticle = View.typeQueryArticle()
                    if(typeArticle==1):
                        print('Consulta por codigo')
                        #keyArticle = 
                        article = Controller.articlesInquiry(keyArticle)
                        pauseProcess()
                    if(typeArticle==2):
                        View.cleanScreen()
                        listOfArticles = Controller.printArticles()
                        print('\n')
                        for article in listArticles:
                            print('--'*45)
                            print(article)
                            print('--'*45)
                        pauseProcess()
            
    def rentArticles():
        operationRent = 0
        while(operationRent != 3):
            View.cleanScreen()
            print('--'*45)
            print('\n\n\tAGREGAR RESERVA')
            print('\n1)Ingresar ci cliente')
            print('2) Nuevo cliente')
            isClient = int(input('Ingrese una opcion [1 al 3]: '))
            if(isClient==1):
                View.rentArticlesClient()
            if(isClient==2):
                rentArticlesNewClient()

    def typeEmployee():
        ''' procedure to print menu to select type of employee, general or individual '''
        View.cleanScreen()
        print('--'*45)
        print('\n\tCONSULTA EMPLEADO')
        print('\n\n1) Consulta por ci:')
        print('2) Consulta general')
        print('3) Volver')
        typeEmployee = int(input('\n\nIngrese una opcion: '))
        return typeEmployee

    def employeeInquity():
        ''' Query for CI, return a single employee '''
        View.cleanScreen()
        print('--'*45)
        print('\n\n\tCONSULTA EMPLEADO')
        ciEmployee = input('\n\nCedula Empleado: ')
        return ciEmployee

    #TODO: MODIFICAR 
    def articleInquiry():
        View.cleanScreen()
        print('--'*45)
        print('\n\n\tCONSULTA DE ARTICULOS')
        print('COD\t\t DESCRIPCION')
        listArticlesInStock = []
        listArticlesInStock = listArticles()
        for key in listArticles:
            print(++i, key)
        keyArticle = input('\nCodigo Articulo: ')
        return keyArticle

    def typeQueryArticle():
        ''' procedure to print menu to select type of article query  '''
        View.cleanScreen()
        print('--'*45)
        print('\n\tCONSULTA ARTICULOS')
        print('\n\n1) Consultar por codigo')
        print('2) Consulta general')
        print('3) Volver')
        typeArticle = int(input('\n\nIngrese una opcion: '))
        return typeArticle

    def rentArticlesClient():
        View.cleanScreen()
        print('--'*45)
        print('\n\tAGREGAR RESERVA')
        print('\nCedula cliente: ')
        #client = Controller.
                
            
