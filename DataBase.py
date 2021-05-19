from mizodb import MiZODB, transaction
from Person import Customer, Employee
from Bussines import Bussines
from Leasable import *

db = MiZODB('./Data')
dbroot = db.root
'''CLASS IN CHARGE OF PERSISTING THE OBJECTS AND MAKING THE RENTAL MODIFICATIONS AND
RETURNS MADE FROM THE CONTROLLER'''

def saveStock():
    #dbroot[keyArticle] = value
    #transaction.commit()
    dbroot['ironChair']=500
    dbroot['plasticChair']=500
    dbroot['puff']=500
    dbroot['longTable']=500
    dbroot['shortTable']=500
    dbroot['circleTable']=500
    dbroot['glasses']=500
    dbroot['cutlery']=500
    dbroot['dish']=500

def startDataTest():
    longTable = LongTable(description='Long Table ', cant=500)
    dbroot['longTableTest'] = longTable, 500

def saveCustomer(key, value):
    dbroot[key]=value
    transaction.commit()

def saveEmployee(key, value):
    dbroot[key]=value
    transaction.commit()

def getCustostomer(key):
    '''get customer from key'''
    try:
        if(dbroot[key]!=None):
            return dbroot[key]
        else:
            raise(KeyError)
    except KeyError:
        print('Customer: \"'+ key +'\" not found!')

def getEmployee(key):
    '''get the Employee from key'''
    try:
        if(dbroot[key] != None):
            return dbroot[key]
        else:
            raise(KeyError)
    except KeyError:
        print('Employee: \" '+key+' \" not found!')

def getItemStock(key):
    '''get articles in stock from a key'''
    try:
        return dbroot[key]
    except ValueError:
        return None

def rent(key, quantity):
    '''function for rent article'''
    try:
        dbroot[key] -= quantity
        transaction.commit()
        return True
    except ValueError:
        return None

def returnObj(key, quantity):
    '''function for return article'''
    try:
        dbroot[key] += quantity
        transaction.commit()
        return True
    except ValueError:
        return None

def getRentedObjects(key):
    dbroot[key].rentedObjects={'ironChair':0, 'plasticChair':0, 'puff':0, 'longTable':0,
    'shortTable':0, 'circleTable':0, 'glasses':0 ,'cutlery':0, 'dish':0}
    transaction.commit()

def getArticle(key):
    try:
        if(dbroot[key] != None):
            return dbroot[key]
        else:
            return None
    except KeyError:
        print('Article with code [{}] not found!'.format(key))

def listRecords():
    result = []
    for key in dbroot.keys():
        object = dbroot[key]
        if isinstance (object, Customer):
            result.append(object)

    return result

def listRecordsEmployee():
    result = []
    for key in dbroot.keys():
        object = dbroot[key]
        if isinstance (object, Employee):
            result.append(object)
    
    return result

def listArticles():
    result = []
    for key in dbroot.keys():
        object = dbroot[key]
        if isinstance (object, Bussines):
            result.append(object)
    
    return result

def printArticles():
    for key in dbroot.keys():
        print('*****' * 10)
        print(key)
        print('*****' * 10)
        print(dbroot[key])