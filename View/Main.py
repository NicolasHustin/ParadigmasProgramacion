from tkinter import *
from tkinter import messagebox
from PIL import ImageQt, Image 
import random
from View.consulta_general import consultaGeneral
from View.consulta_por_ci import consultaPorCi
from View.agg_empleado import Agg_Empleado
from View.agg_reserva import agregar_reserva
from View.devolverReserva import devolver
from View.presupuesto import presupuesto

resolucion_print = "650x425+550+200"
colores = ["Navy blue","gray", "black"]

class MainWindow():

    def __init__(self, ventana):
        self.ventana = ventana
        self.main(self.ventana)

    def main(self, ventana):

        ventana.resizable(0, 0)
        ventana.geometry(resolucion_print)
        ventana.title("Rental Control SYSTEM")
        ventana.config(bg = random.choice(colores))
        #Representacion imagenes, TODO: verificar como asignar el icono, actualmente no funciona de esa manera capaz por la version
        icono = PhotoImage(file='pruebapp.gif')
        ventana.iconphoto(ventana, icono)

        barraMenu = Menu(ventana, bg='black', fg='red')

        #Representacion imagenes, TODO: verificar como asignar el icono, actualmente no funciona de esa manera capaz por la version
        #image = ImageQt.PhotoImage(Image.open("pruebapp.gif"))
        #lbl= Label(ventana, image=image).place(x=7, y=10)

        menu_consulta = Menu(barraMenu, tearoff=0)
        menu_consulta.add_command(label="CONSULTAR POR CI", command=self.consultar_por_ci)
        menu_consulta.add_command(label="CONSULTA GRAL", command=self.consulta_gral)
        menu_consulta.add_command(label="CONSULTA PRESUPUESTO", command=self.consulta_presupuesto)
        barraMenu.add_cascade(label="CONSULTA", menu=menu_consulta)

        menu_agregar_reserva = Menu(barraMenu, tearoff=0)
        menu_agregar_reserva.add_command(label="Agregar Reserva", command=self.agregar_reserva)
        barraMenu.add_cascade(label="RESERVAS", menu=menu_agregar_reserva)

        menu_devolver = Menu(barraMenu, tearoff=0)
        menu_devolver.add_command(label="DEVOLVER ARTICULOS", command=self.devolver_articulos)
        barraMenu.add_cascade(label="DEVOLVER", menu=menu_devolver)

        menu_agregar_empleado = Menu(barraMenu, tearoff=0)
        menu_agregar_empleado.add_command(label="AGREGAR EMPLEADO", command=self.agregar_empleado)
        barraMenu.add_cascade(label="AGREGAR", menu=menu_agregar_empleado)

        ventana.config(menu=barraMenu)
        ventana.mainloop()

    def salir(self):
        if(messagebox.askyesno("Salir", "¿Terminar la ejecución?")):
            exit()

    def consulta_gral(self):
        '''Metodo que devuelve la pantalla para una consulta general '''
        consultaGeneral(self.ventana)

    def agregar_reserva(self):
        '''metodo que devuelve la pantalla para agregar una reserva'''
        agregar_reserva(self.ventana)

    def agregar_empleado(self):
        '''metodo que devuelve la pantalla para agregar un empleado'''
        Agg_Empleado(self.ventana)

    def devolver_articulos(self):
        '''metodo que devuelve la pantalla para devolver un articulo'''
        devolver(self.ventana)

    def consultar_por_ci(self):
        '''metodo que devuelve la patnalla para una consulta de persona por ci'''
        consultaPorCi(self.ventana)

    def consulta_presupuesto(self):
        '''metodo que devuelve la pantalla para armar un presupuesto aproximado'''
        presupuesto(self.ventana)
