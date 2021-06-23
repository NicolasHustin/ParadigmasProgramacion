from mizodb import MiZODB, transaction
from Person import Customer, Employee
from Bussines import Bussines
from Leasable import *

db = MiZODB('./Data')
dbroot = db.root
'''CLASS IN CHARGE OF PERSISTING THE OBJECTS AND MAKING THE RENTAL MODIFICATIONS AND
RETURNS MADE FROM THE CONTROLLER
Encargado de la persistencia de los datos y obtencion de los mismos'''

def save_stock():
    #dbroot[keyArticle] = value
    #transaction.commit()
    dbroot['iron_chair']=500
    dbroot['plastic_chair']=500
    dbroot['puff']=500
    dbroot['long_table']=500
    dbroot['short_table']=500
    dbroot['circle_table']=500
    dbroot['glasses']=500
    dbroot['cutlery']=500
    dbroot['dish']=500

def start_data_test():
    longTable = LongTable(description='Long Table ', cant=500)
    dbroot['longTableTest'] = longTable, 500

def save_customer(key, value):
    ''' metodo encargado de agregar un nuevo cliente'''
    dbroot[key]=value
    transaction.commit()

def save_employee(key, value):
    ''' metodo encargado de agregar un nuevo empleado'''
    dbroot[key]=value
    transaction.commit()

def get_custostomer(key):
    '''get customer from key'''
    try:
        if(dbroot[key]!=None):
            return dbroot[key]
        else:
            raise(KeyError)
    except KeyError:
        print('Customer: \"'+ key +'\" not found!')

def get_employee(key):
    '''get the Employee from key'''
    try:
        if(dbroot[key] != None):
            return dbroot[key]
        else:
            raise(KeyError)
    except KeyError:
        print('Employee: \" '+key+' \" not found!')

def get_item_stock(key):
    '''get articles in stock from a key'''
    try:
        return dbroot[key]
    except ValueError:
        print('Articulo: \"'+key+' \" not found !')
        return None

def rent(key, quantity):
    '''function for rent article'''
    try:
        dbroot[key] -= quantity
        transaction.commit()
        return True
    except ValueError:
        return None

def return_obj(key, quantity):
    '''function for return article'''
    try:
        dbroot[key] += quantity
        transaction.commit()
        return True
    except ValueError:
        return None

def get_rented_objects(key):
    ''' metodo para obtener los articulos rentados'''
    dbroot[key].rentedObjects={'iron_chair':0, 'plastic_chair':0, 'puff':0, 'long_table':0,
    'short_table':0, 'circle_table':0, 'glasses':0 ,'cutlery':0, 'dish':0}
    transaction.commit()

def get_article(key):
    ''' metodo para obtener un articulo segun el codigo '''
    try:
        if(dbroot[key] != None):
            return dbroot[key]
        else:
            return None
    except KeyError:
        print('Article with code [{}] not found!'.format(key))

def list_records():
    ''' metodo para la obtener un listado de Clientes '''
    result = []
    for key in dbroot.keys():
        object = dbroot[key]
        if isinstance (object, Customer):
            result.append(object)

    return result

def list_records_employee():
    ''' metodo para la obtencion de un listado de empleados '''
    result = []
    for key in dbroot.keys():
        object = dbroot[key]
        if isinstance (object, Employee):
            result.append(object)
    
    return result

def list_articles():
    ''' metodo para la obtencion del listado de articulos '''
    result = []
    for key in dbroot.keys():
        object = dbroot[key]
        if isinstance (object, Bussines):
            result.append(object)
    
    return result

#TODO: preguntar como podemos replicar esto en el modulo de la vista
def print_articles():
    ''' metodo que se encarga de imprimir la lista de los articulos '''
    for key in dbroot.keys():
        print('*****' * 10)
        print(key)
        print('*****' * 10)
        print(dbroot[key])