from abc import ABCMeta, abstractmethod
from DataBase import rent, returnObj

class Leasable (object):

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

    __metaclass__=ABCMeta

    def __init__(self):
        super().__init__()

class IronChair(Chair):
    __price=5000

    def __init__(self):
        super().__init__()

    def rent(cant):
        rent('ironChair', cant)

    def returnObj(cant)
        returnObj('ironChair', cant)
    
    @classmethod
    def price(self)
        return(IronChair.__price)

    def __str__(self):
        return (super().__str__())

class PlasticChair(Chair):
    __price = 2500

    def __init__(self):
        super().__init__()

    def rent(cant):
        rent('plasticChair', cant)

    def returnObj(cant):
        returnObj('plasticChair', cant)

    @classmethod
    def price(self):
        return (PlasticChair.__price)

    def __str__(self):
        return(super().__str__())

class Puff(Chair):
    __price=2000

    def __init__(self):
        super().__init__()

    def rent(cant):
        rent('puff', cant)

    def returnObj(cant):
        returnObj('puff', cant)

    @classmethod
    def price(self):
        return (Puff.__price)

    def __str__(self):
        return(super().__str__())

    
class Table(Leasable):
    __metaclass__ = ABCMeta

    def __init__(self):
        super().__init__()

class LongTable(Table):

    __price = 20000

    def __init__(self):
        super().__init__()

    def rent(cant):
        rent('longTable', cant)

    def returnObj(cant):
        returnObj('longTable', cant)

    @classmethod
    def getPrice(self):
        return (LongTable.__price)

    def __str__(self):
        return (super().__str__())

class ShortTable(Table):

    __price = 10000

    def __init__(self):
        super().__init__()

    def rent(cant):
        rent('shortTable', cant)

    def returnObj(cant):
        returnObj('shortTable', cant)

    @classmethod
    def getPrice(self):
        return (ShortTable.__price)

    def __str__(self):
        return (super().__str__())

class CircleTable(Table):

    __price=10000

    def rent(cant):
        rent('circleTable', cant)

    def returnObj(cant):
        returnObj('cicrcleTable', cant)

    @classmethod
    def getPrice(self):
        return (CircleTable.__price)

    def __str__(self):
        return (super().__str__())

class Cookware(Leasable):

    __metaclass__=ABCMeta

    def __init__(self):
        super().__init__()
    
class Dish(Cookware):

    __price = 2000

    def rent(cant):
        rent('dish', cant)

    def returnObj(cant):
        returnObj('dish', cant)

    @classmethod
    def getPrice(self):
        return (Dish.__price)

    def __str__(self):
        return (super().__str__())

class Cutlery(Cookware):

    __price = 2000

    def rent(cant):
        rent('cutlery', cant)

    def returnObj(cant):
        returnObj('cutlery', cant)

    @classmethod
    def getPrice(self):
        return (Cutlery.__price)

    def __str__(self):
        return (super().__str__())

class Glasses(Cookware):

    __price = 1000

    def rent(cant):
        rent('glasses', cant)

    def returnObj(cant):
        returnObj('glasses', cant)

    @classmethod
    def getPrice(self):
        return (Glasses.__price)

    def __str__(self):
        return (super().__str__())

class TableCloth(Leasable):

    __metaclass__=ABCMeta

    def __init__(self):
        super().__init__()

class DiolenCloth(TableCloth):

    __price=10000

    __color='blanco'

    def rent(color, cant):
        rent(color, cant)

    def returnObj(color, cant):
        returnObj(color, cant)

    @classmethod
    def getPrice(self):
        return (DiolenCloth.__price)

    @classmethod
    def getColor(self):
        return (DiolenCloth.__color)

    def __str__(self):
        return (super().__str__())
