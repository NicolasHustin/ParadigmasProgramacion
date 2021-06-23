import os

class View_util():

    def pause_process():
        input('\n\n\nPresione cualquier tecla para continuar...')

    @staticmethod
    def clean_screen():
        ''' funcion que sirve para limpiar la pantalla en la consola '''
        os.system('cls' if os.name =='nt' else 'clear')