
class Bussines ():
    ''' this class contains the list of customers and articles, these lists will be in use while the program is running '''

    Stock = {'plasticChair':300, 'ironChair': 300, 'puff':150, 'longTable':50, 'shortTable':50, 'circleTable':50
    , 'dish': 300, 'glasses': 300, 'cutlery': 300}
    Customers = {}
    Employees = {}

class About():

    def __init__(self, name=' ', ruc=' ', address=' ', telephone=' '):
        self.name = name
        self.ruc = ruc
        self.address = address
        self.telephone = telephone

    def __str__(self):
        return('\nNombre de la empresa: ' + self.name + '\nRuc: '+ self.ruc+
        '\nDireccion: ' + self.address+'\nTelefono: '+self.telephone)