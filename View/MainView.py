import os
from Person import Customer, Employee

class View():

    
    @staticmethod
    def cleanScreen():
        '''Function for clear screen'''
        os.system('cls' if os.name =='nt' else 'clear')

    @staticmethod
    def validateOperation(min, max):
        '''Function for validate input operations'''
        value = input("[{}] al [{}] -->> ".format(min, max))
        try:
            valor = int(valor)
            if(valor <= max and valor >= min):
                return valor
            else:
                raise (ValueError)
        except ValueError:
            print('\n['+str(valor)+'] Is not a valid option... please try again;')

    def aggEmployee():
        View.cleanScreen()
        print('\n\n\t\tINGRESE LOS DATOS DEL EMPLEADO\n')
        while True:
            try:
                name = input('\t\tNOMBRE: ')
                lastName = input('\t\tAPELLIDO: ')
                ciEmployee = input('\t\tCEDULA: ')
                salary = int(input('\t\tSUELDO: '))
                address = input('\t\tDIRECCION: ')
                telephone = input('\t\tTELEFONO: ')
                newEmployee = Employee(salary, name=name, lastName=lastName, ci=ciEmployee, address=address, telephone=telephone)

                print('--'*35)
                return ciEmployee, newEmployee
            except Exception as e:
                print('\nError in addEmployee: -> ', e)
