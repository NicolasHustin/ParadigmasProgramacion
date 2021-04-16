import os
from View.MainView import *
from View.ViewUtils import *
from AppController import *
from DataBase import saveStock
class RcsApp ():
    
    @staticmethod
    def initApp():
        startDataTest()
        
        RcsApp.mainMenu()

    def mainMenu():
        operation=0 #Var for Operations in Menu
        while(operation != 5):
            View.cleanScreen()
            print('--'*20)
            print('R.C.S (Rental Control System)')
            print('\n' + '*'*30 + ' PAGINA PRINCIPAL ' + '*'*30)
            print('\n\t1-) CONSULTAR')
            print('\t2-) AGREGAR RESERVA')
            print('\t3-) DEVOLVER ARTICULOS')
            print('\n\n\t4-) AGREGAR EMPLEADO')
            print('\t5-) SALIR')
            print('--'*20)
            operation = int(input('Ingrese un numero[1 al 5]: '))
            if(operation == 1):
                View.generalInquiry()
                pauseProcess()
            if(operation == 2):
                View.rentArticles()
                pauseProcess()
            if(operation == 3):
                print('devolver articulos')
                pauseProcess()
            if(operation == 4):
                print('agregar empleado')
                View.aggEmployee()
                pauseProcess()
            if(operation == 5):
                print('salir')
                print('gracias por utilizar el programa')
                
    
if __name__ == "__main__":
    RcsApp.initApp()


    