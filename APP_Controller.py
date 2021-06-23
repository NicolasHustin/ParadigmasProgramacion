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
        return get_employee(ciEmployee)

    def articlesInquiry(keyArticle):
        return get_article(keyArticle)

    def get_general_employees():
        return list_records_employee()

    def list_of_articles():
        return list_articles()

    def printArticles():
        return print_articles()

        
    def rentArticleClient(ciClient):
        pass

    def returnArticles():
        pass


    