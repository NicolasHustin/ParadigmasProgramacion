import os
from View.MainView import *
from View.ViewUtils import *
from APP_Controller import *
from database import save_stock
class RcsApp ():
    
    @staticmethod
    def init_app():
        #startDataTest()
        
        RcsApp.main_menu()

    def main_menu():
        operation=0 #Var for Operations in Menu
        while(operation != 5):
            View_util.clean_screen()
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
                View.general_inquiry()
                View_util.pause_process()
            if(operation == 2):
                View.rent_articles()
                View_util.pause_process()
            if(operation == 3):
                print('devolver articulos')
                View_util.pause_process()
            if(operation == 4):
                print('agregar empleado')
                View.agg_employee()
                View_util.pause_process()
            if(operation == 5):
                print('salir')
                print('gracias por utilizar el programa')
                
    
if __name__ == "__main__":
    RcsApp.init_app()


    