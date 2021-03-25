import os

class RcsApp ():
    
    @staticmethod
    def initApp():
        RcsApp.mainMenu()

    def mainMenu():
        operation=0 #Var for Operations in Menu
        while(operation != 5):
            os.system('cls')
            print('--'*10)
            print('R.C.S (Rental Control System)')
            print('\n\t1-) CONSULTAR')
            print('\t2-) AGREGAR RESERVA')
            print('\t3-) DEVOLVER ARTICULOS')
            print('\n\n\t4-) AGREGAR EMPLEADO')
            print('\t5-) SALIR')
            print('--'*10)
            operation = input('Ingrese un numero')
            if(operation == 1):
                print('opcion 1')
                input('Presione cualquier tecla para continuar...')
            if(operation == 2):
                print('agregar reserva')
                input('Presione cualquier tecla para continuar...')
            if(operation == 3):
                print('devolver articulos')
                input('Presione cualquier tecla para continuar...')
            if(operation == 4):
                print('agregar empleado')
                input('Presione cualquier tecla para continuar...')
            if(operation == 5):
                print('salir')
                os.system('cls')
                print('gracias por utilizar el programa')
    
if __name__ == "__main__":
    RcsApp.initApp()


    