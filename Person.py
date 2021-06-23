from abc import ABCMeta, abstractmethod
from persistent import *

class Person(object):
    ''' clase abstracta que hace referencia a cualquier persona dentro del negocio
        ya sea empleado o cliente, esta contiene los datos necesarios para las operaciones
        requeridas en el sistema'''

    __metaclass__ = ABCMeta

    def __init__(self, name='', last_name='', ci='', address='Sin direccion', telephone=''):
        ''' metodo que se encarga de representar a las personas dentro del negocio '''
        self.name = name
        self.last_name = last_name
        self.ci = ci
        self.address = address
        self.telephone = telephone

    def get_name(self):
        return self.name

    def get_last_name(self):
        return self.last_name

    def get_ci(self):
        return self.ci

    def get_address(self):
        '''metodo que retorna la direccion de una persona'''
        return self.address

    def get_telephone(self):
        '''metodo que retorna el telefono de una persona'''
        return self.telephone

    def __str__(self):
        return ('\nNombre: ' + self.name + '\nApellido: ' + self.last_name + '\nCedula: ' + self.ci + '\nDireccion: ' + self.address
        +'\nTelefono: ' + self.telephone)

    
class Customer(Person, Persistent):
    '''clase que representa o hace referencia a un cliente en el negocio'''
    def __init__(self, ruc='Anonimo', rentedObjects=None, **kwargs):
        super().__init__(**kwargs)
        self.ruc = ruc
        self.rentedObjects = rentedObjects

    def get_ruc(self):
        return self.ruc

    def __str__(self):
        return (super().__str__()+'\nRuc: '+self.ruc+'\n Objetos Arrendados: '+ str(self.rentedObjects))

    
class Employee(Person, Persistent):
    '''Clase que representa un Empleado dentro del negocio y hereda de Persona'''

    def __init__(self, salary=0, **kwargs):
        super().__init__(**kwargs)
        self.salary = salary

    def __str__(self):
        return(super().__str__()+'\nSalario: ' + str(self.salary))


