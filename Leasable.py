from abc import ABCMeta, abstractmethod
from database import *

class Leasable (object):
    ''' clase abstracta que representa o hace referencia a un objeto que puede ser rentado '''

    __metaclass__ = ABCMeta

    def __init__(self, description, cant):
        self.description=description
        self.cant=cant

    @abstractmethod
    def rent():
        pass

    @abstractmethod
    def returnObj():
        pass

class Chair(Leasable):
    ''' clase que representa una silla y hereda de Leasable'''

    __metaclass__=ABCMeta

    def __init__(self):
        super().__init__()

class IronChair(Chair):
    ''' clase que representa a una silla de hierro dentro del negocio'''
    __price=5000

    def __init__(self):
        super().__init__()

    def rent(cant):
        rent('iron_chair', cant)

    def return_obj(cant):
        return_obj('iron_chair', cant)
    
    @classmethod
    def price(self):
        return(IronChair.__price)

    def __str__(self):
        return (super().__str__())

class PlasticChair(Chair):
    __price = 2500

    def __init__(self):
        super().__init__()

    def rent(cant):
        rent('plastic_chair', cant)

    def return_obj(cant):
        return_obj('plastic_chair', cant)

    @classmethod
    def price(self):
        return (PlasticChair.__price)

    def __str__(self):
        return(super().__str__())

class Puff(Chair):
    ''' clase que hace referencia a los puff dentro del negocio '''
    __price=2000

    def __init__(self):
        super().__init__()

    def rent(cant):
        rent('puff', cant)

    def return_obj(cant):
        return_obj('puff', cant)

    @classmethod
    def price(self):
        return (Puff.__price)

    def __str__(self):
        return(super().__str__())

    
class Table(Leasable):
    ''' Clase que representa a una Mesa dentro del negocio y hereda de Leasable (rentable)'''
    __metaclass__ = ABCMeta

    def __init__(self):
        super().__init__()

class LongTable(Table):
    ''' clase que hace referencia a una mesa larga o tablon dentro del negocio '''

    __price = 20000

    def __init__(self):
        super().__init__()

    def rent(cant):
        rent('long_table', cant)

    def return_obj(cant):
        return_obj('long_table', cant)

    @classmethod
    def price(self):
        return (LongTable.__price)

    def __str__(self):
        return (super().__str__())

class ShortTable(Table):

    __price = 10000

    def __init__(self):
        super().__init__()

    def rent(cant):
        rent('short_table', cant)

    def return_obj(cant):
        return_obj('short_table', cant)

    @classmethod
    def price(self):
        return (ShortTable.__price)

    def __str__(self):
        return (super().__str__())

class CircleTable(Table):
    ''' clase que hace referencia a una mesa redonda dentro del negocio '''
    __price=10000

    def rent(cant):
        rent('circle_table', cant)

    def return_obj(cant):
        return_obj('cicrcle_table', cant)

    @classmethod
    def price(self):
        return (CircleTable.__price)

    def __str__(self):
        return (super().__str__())

class Cookware(Leasable):
    ''' Clase que hace referencia a los articulos de cocina dentro del negocio y hereda de la clase Leasable, rentable'''

    __metaclass__=ABCMeta

    def __init__(self):
        super().__init__()
    
class Dish(Cookware):
    ''' clase que hace referencia a un Plato dentro del negocio'''

    __price = 2000

    def rent(cant):
        rent('dish', cant)

    def return_obj(cant):
        return_obj('dish', cant)

    @classmethod
    def price(self):
        return (Dish.__price)

    def __str__(self):
        return (super().__str__())

class Cutlery(Cookware):
    ''' clase que hace refencia a un juego de cubiertos dentro del negocio'''

    __price = 2000

    def rent(cant):
        rent('cutlery', cant)

    def return_obj(cant):
        return_obj('cutlery', cant)

    @classmethod
    def price(self):
        return (Cutlery.__price)

    def __str__(self):
        return (super().__str__())

class Glasses(Cookware):
    ''' clase que hace referencia a un VASO dentro del negocio'''

    __price = 1000

    def rent(cant):
        rent('glasses', cant)

    def return_obj(cant):
        return_obj('glasses', cant)

    @classmethod
    def price(self):
        return (Glasses.__price)

    def __str__(self):
        return (super().__str__())

class TableCloth(Leasable):
    ''' clase que hace referencia a un mantel para la mesa, hereda de Leasable (un articulo rentable) '''

    __metaclass__=ABCMeta

    def __init__(self):
        super().__init__()

class DiolenCloth(TableCloth):
    ''' clase que hace referencia a un mantel de diolen '''

    __price=10000

    __color='blanco'

    def rent(color, cant):
        rent(color, cant)

    def return_obj(color, cant):
        return_obj(color, cant)

    @classmethod
    def price(self):
        return (DiolenCloth.__price)

    @classmethod
    def getColor(self):
        return (DiolenCloth.__color)

    def __str__(self):
        return (super().__str__())
