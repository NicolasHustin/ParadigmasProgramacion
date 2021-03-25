from ZODB import FileStorage,DB
import transaction

class MiZODB(object):
    def __init__(self,archivo):
        self.storage = FileStorage.FileStorage(archivo)
        self.db = DB(self.storage)
        self.conection = self.db.open()
        self.root = self.conection.root()