from abc import ABCMeta, abstractmethod
from Person import Customer
from Leasable import *
import time
'''time.strftime("%H:%M:%S") time.strftime("%d:%b:%Y")'''
class Receipt(object):

    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    def __str__(self):
        pass


class Invoice(Receipt):
    '''Clase que hereda de Receipt'''

    def __init__(self):
        super().__init__()

    def calcular(customerData):
        #TODO: implementar el metodo para calcular el monto
        return ('\nFECHA: '+time.strftime("%d:%b:%Y")+'\tHORA: '+time.strftime("%H:%M:%S")+str(customerData)+'\n\nMONTO: '+str(0)+' Gs')