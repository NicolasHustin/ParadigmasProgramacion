from ZODB import FileStorage,DB
import transaction
''' Modulo de la base de datos ZODB: es la encargada de abrir y cerrar
    la base de datos como tambien de la persistencia de los datos '''

class MiZODB(object):
    def __init__(self,archivo):
        ''' metodo que se encarga de abrir la base de datos o bien cerrarla
            si esta ya esta abierta '''
        self.storage = FileStorage.FileStorage(archivo)
        self.db = DB(self.storage)
        self.conection = self.db.open()
        self.root = self.conection.root()