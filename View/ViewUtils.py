import os

class View_util():

    def pause_process():
        input('\n\n\nPresione cualquier tecla para continuar...')

    @staticmethod
    def clean_screen():
        ''' funcion que sirve para limpiar la pantalla en la consola '''
        os.system('cls' if os.name =='nt' else 'clear')

    #TODO:Reemplazar en todas las invocaciones de la vista para cumplir con el requisito de modularidad
    @staticmethod
    def imprimir(text):
        '''funcion que sirve para la impresion de los datos'''
        print(text)