import os
from Person import Customer, Employee
from View.ViewUtils import *
from APP_Controller import *


class View():

    @staticmethod
    def validate_operation(min, max):
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

    def agg_employee():
        View_util.clean_screen()
        print('--'*45)
        print('\n\n\t\tINGRESE LOS DATOS DEL EMPLEADO\n')
        while True:
            try:
                name = input('\t\tNOMBRE: ')
                last_name = input('\t\tAPELLIDO: ')
                ci_employee = input('\t\tCEDULA: ')
                salary = int(input('\t\tSUELDO: '))
                address = input('\t\tDIRECCION: ')
                telephone = input('\t\tTELEFONO: ')
                print('--'*45)
                new_employee = Employee(salary, name=name, last_name=last_name, ci=ci_employee, address=address, telephone=telephone)
                Controller.add_employee(ci_employee, new_employee)
                print('\nEmpleado [{}] con nombre: {} guardado con exito!'.format(ci_employee, new_employee.getName()))
            except Exception as e:
                print('\nError in addEmployee: -> ', e)

    def general_inquiry():
        operation_inquiry = 0
        while(operation_inquiry != 5):
            View_util.clean_screen()
            operation_inquiry = 0
            print('--'*45)
            print('\n\tCONSULTAS GENERALES')
            print('\n\n1) CONSULTA EMPLEADOS')
            print('2) CONSULTA ARTICULOS')
            print('3) CONSULTA CLIENTES\n')
            print('4) PRESUPUSTO \n')
            print('5) VOLVER \n\n')
            print('--'*45)
            operation_inquiry = int(input('Ingrese una opcion [1 al 5]: '))
            if(operation_inquiry==1):
                type_employee = 0
                while(type_employee != 3):
                    type_employee = View.type_employee()
                    #QUERY FOR ID
                    if(type_employee == 1):
                        View_util.clean_screen()
                        ci_employee = View.employee_inquity()
                        employee = Controller.employee_inquiry(ci_employee)
                        print(employee)
                        View_util.pause_process()
                    #A GENERAL QUERY 
                    if(type_employee == 2):
                        View_util.clean_screen()
                        list_of_employees = Controller.get_general_employees()
                        print('\n')
                        for empl in list_of_employees:
                            print('--'*45)
                            print(empl)
                            print('--'*45)
                        View_util.pause_process()
            if(operation_inquiry == 2):
                type_article = 0
                while (type_article != 3):
                    type_article = View.typeQueryArticle()
                    if(type_article==1):
                        print('Consulta por codigo')
                        key_article = 0 #TODO:obtener el codigo del articulo 
                        article = Controller.articlesInquiry(key_article)
                        View_util.pause_process()
                    if(type_article==2):
                        View_util.clean_screen()
                        list_of_articles = Controller.printArticles()
                        print('\n')
                        for article in list_of_articles:
                            print('--'*45)
                            print(article)
                            print('--'*45)
                        View_util.pause_process()
            if(operation_inquiry == 3):
                #TODO
                #Consulta de clientes, se podra ver todos los clientes asi tambien consulta por cedula
                View_util.pause_process()
            if(operation_inquiry == 4):
                #TODO
                #Consulta un presupuesto, un precio estimado de los articulos a rentar
                View_util.clean_screen()
                View.imprimirPresupuesto()
                View_util.pause_process()        
            
    def rent_articles():
        operation_rent = 0
        while(operation_rent != 3):
            View_util.clean_screen()
            print('--'*45)
            print('\n\n\tAGREGAR RESERVA')
            print('\n1)Ingresar ci cliente')
            print('2) Nuevo cliente')
            is_client = int(input('Ingrese una opcion [1 al 3]: '))
            if(is_client==1):
                View.rent_articles_client()
            if(is_client==2):
                #rentArticlesNewClient()
                pass

    def type_employee():
        ''' procedure to print menu to select type of employee, general or individual '''
        View_util.clean_screen()
        print('--'*45)
        print('\n\tCONSULTA EMPLEADO')
        print('\n\n1) Consulta por ci:')
        print('2) Consulta general')
        print('3) Volver')
        type_employee = int(input('\n\nIngrese una opcion: '))
        return type_employee

    def employee_inquity():
        ''' Query for CI, return a single employee '''
        View_util.clean_screen()
        print('--'*45)
        print('\n\n\tCONSULTA EMPLEADO')
        ci_employee = input('\n\nCedula Empleado: ')
        return ci_employee

    #TODO: MODIFICAR 
    def article_inquiry():
        View_util.clean_screen()
        print('--'*45)
        print('\n\n\tCONSULTA DE ARTICULOS')
        print('COD\t\t DESCRIPCION')
        list_articles_in_stock = []
        list_articles_in_stock = list_articles()
        for key in list_articles_in_stock:
            print(++i, key)
        key_article = input('\nCodigo Articulo: ')
        return key_article

    def typeQueryArticle():
        ''' procedure to print menu to select type of article query  '''
        View_util.clean_screen()
        print('--'*45)
        print('\n\tCONSULTA ARTICULOS')
        print('\n\n1) Consultar por codigo')
        print('2) Consulta general')
        print('3) Volver')
        type_article = int(input('\n\nIngrese una opcion: '))
        return type_article

    def rent_articles_client():
        View_util.clean_screen()
        print('--'*45)
        print('\n\tAGREGAR RESERVA')
        print('\nCedula cliente: ')
        #client = Controller.

    def imprimirPresupuesto():
        View_util.clean_screen()
        print('--'*45)
        print('\n\n\tPRESUPUESTO')
        print('\n\tAGREGAR AL PEDIDO:')
        print('\n1) SILLA:')
        print('\n2) MESA:')
        print('\n3) CUBIERTO:')
        print('\n4) TELAS:\n')

        opcion_presupuesto = input('Eliga una opcion:  ')
        return int(opcion_presupuesto)
        

    
                
            
