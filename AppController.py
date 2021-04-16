from View.MainView import *
from DataBase import *

class Controller():

    def addEmployee(ciEmployee, newEmployee):
        ''' save employee in database '''
        saveEmployee(ciEmployee, newEmployee)

    def addArticle(codArticle, newArticle):
        ''' save item in stock '''
        saveArticle(codArticle, newArticle)

    def employeeInquiry(ciEmployee):
        return getEmployee(ciEmployee)

    def articlesInquiry(keyArticle):
        return getArticle(keyArticle)

    def getGeneralEmployees():
        return listRecordsEmployee()

    def listOfArticles():
        return listArticles()

    def printArticles():
        return printArticles()

        
    #def rentArticleClient(ciClient):


    