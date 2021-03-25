from abc import ABCMeta, abstractmethod
from persistent import *


class Person(object):

    __metaclass__ = ABCMeta

    def __init__(self, name='', lastName='', ci='', address='Sin direccion', telephone=''):
        self.name = name
        self.lastName = lastName
        self.ci = ci
        self.address = address
        self.telephone = telephone

    def getName(self):
        return self.name

    def getLastName(self):
        return self.lastName

    def getCi(self):
        return self.ci

    def getAddress(self):
        return self.address

    def getTelephone(self):
        return self.telephone

    def __str__(self):
        return ('\nNombre: ' + self.name + '\nApellido: ' + self.lastName + '\nCedula: ' + self.ci + '\nDireccion: ' + self.address)
        +'\nTelefono: ' + self.telephone)

    
class Customer(Person, Persistent):

    def __init__(self, ruc='Anonimo', rentedObjects=None, **kwargs):
        super().__init__(**kwargs)
        self.ruc = ruc
        self.rentedObjects = rentedObjects

    def getRuc(self):
        return self.ruc

    def __str__(self):
        return (super().__str__()+'\nRuc: '+self.ruc+'\n Objetos Arrendados: '+ str(self.rentedObjects))

    
class Employee(Persona, Persistent):

    def __init__(self, salary=0, **kwargs):
        super().__init__(**kwargs)
        self.salary = salary

    def __str__(self):
        return(super().__str__()+'\nSalario: ' + str(self.salary))


