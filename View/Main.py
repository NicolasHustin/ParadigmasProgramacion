from tkinter import *
from tkinter import messagebox
from PIL import ImageQt, Image 
import random
from View.consultaGeneral import consultaGeneral
from View.consultaPorCi import consultaPorCi
from View.aggEmpleado import aggEmpleado
from View.aggReserva import agregarReserva

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
        ventana.protocol("WM_DELETE_WINDOW", self.salir)
        ventana.config(bg = random.choice(colores))
        #Representacion imagenes, TODO: verificar como asignar el icono, actualmente no funciona de esa manera capaz por la version
        #icono = PhotoImage(file='icono.png')
        #ventana.iconphoto(ventana, icono)

        barraMenu = Menu(ventana, bg='black', fg='red')

        #Representacion imagenes, TODO: verificar como asignar el icono, actualmente no funciona de esa manera capaz por la version
        #image = ImageQt.PhotoImage(Image.open("fondo.png"))
        #lbl= Label(ventana, image=image).place(x=7, y=10)

        menuConsulta = Menu(barraMenu, tearoff=0)
        menuConsulta.add_command(label="CONSULTAR POR CI", command=self.consultarPorCI)
        menuConsulta.add_command(label="CONSULTA GRAL", command=self.consultaGral)
        barraMenu.add_cascade(label="CONSULTA", menu=menuConsulta)

        menuAgregarReserva = Menu(barraMenu, tearoff=0)
        menuAgregarReserva.add_command(label="Agregar Reserva", command=self.agregarReserva)
        barraMenu.add_cascade(label="RESERVAS", menu=menuAgregarReserva)

        menuDevolver = Menu(barraMenu, tearoff=0)
        menuDevolver.add_command(label="DEVOLVER ARTICULOS", command=self.devolverArticulos)
        barraMenu.add_cascade(label="DEVOLVER", menu=menuDevolver)

        menuAgregarEmpleado = Menu(barraMenu, tearoff=0)
        menuAgregarEmpleado.add_command(label="AGREGAR EMPLEADO", command=self.agregarEmpleado)
        barraMenu.add_cascade(label="AGREGAR", menu=menuAgregarEmpleado)

        ventana.config(menu=barraMenu)
        ventana.mainloop()

    def salir(self):
        if(messagebox.askyesno("Salir", "¿Terminar la ejecución?")):
            exit()

    def consultaGral(self):
        consultaGeneral(self.ventana)

    def agregarReserva(self):
        agregarReserva(self.ventana)

    def agregarEmpleado(self):
        aggEmpleado(self.ventana)

    def devolverArticulos(self):
        #TODO: IMPLEMENTAR EL METODO
        pass

    def consultarPorCI(self):
        consultaPorCi(self.ventana)
