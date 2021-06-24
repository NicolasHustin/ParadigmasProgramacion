from View.MainView import *
from database import *

class Controller():

    def add_employee(ciEmployee, new_employee):
        ''' save employee in database '''
        save_employee(ciEmployee, new_employee)

    def add_article(codArticle, newArticle):
        ''' save item in stock '''
        #save_article(codArticle, newArticle)

    def employee_inquiry(ciEmployee):
        '''funcion que sirve para la consulta individual de un empleado'''
        return get_employee(ciEmployee)

    def articlesInquiry(keyArticle):
        '''funcion que sirve para la consulta individual de un articulo por medio del codigo'''
        return get_article(keyArticle)

    def get_general_employees():
        '''funcion que sirve para listar todos los empleados'''
        return list_records_employee()

    def list_of_articles():
        '''funcion que sirve para listar todos los articulos'''
        return list_articles()

    #TODO:llevar a clase Vista, para cumplir con el objetivo de modularidad
    def printArticles():
        '''funcion que sirve para imprimir todos los articulos'''
        return print_articles()

        
    def rentArticleClient(ciClient):
        '''funcion que sirve para rentar un articulo'''
        pass

    def returnArticles():
        '''funcion que sirve para realizar la devolucion de los articulos'''
        pass


    