from tkinter import *
from tkinter import font
import tkinter.ttk as ttk
from AppController import *
from View.consultaCiV import consultaCiV
'tamaño de ventanas'
tamaño="600x325+430+150"
'clor de las ventanas'
color='White'


class consultaPorCi():
    ''' Clase que sirve para la consulta por CI de la vista'''
    def __init__(self, ventana):
        self.ventana = ventana
        self.run(ventana)

    def run(self,ventana):
        self.vLista = Toplevel(ventana)
        self.vLista.config(bg=color)
        self.vLista.resizable(0,0)
        self.vLista.geometry(tamaño)
        self.vLista.title("CONSULTA POR CI")
        self.vLista.grab_set()

        self.ComicSansMS = font.Font(family="Comic Sans MS",size=11,weight="bold")
        self.DejaVuSansMono = font.Font(family="DejaVu Sans Mono",size=15,weight="bold")

        Label(self.vLista, text="CONSULTA EMPLEADO", bg='White',font=self.DejaVuSansMono).grid(row=1, column=10)

        Label(self.vLista, text="Cedula*:",bg='White', fg='red',font=self.ComicSansMS).grid(row=5, column=9)

        self.cedula = Entry(self.vLista)
        self.cedula.focus()
        self.cedula.grid(row=5, column=10)

        self.btonAgregar = Button(self.vLista, text="CONSULTAR", bg="green",command=self.consultaci)
        self.btonAgregar.grid(row=6, column=12)

        Button(self.vLista, text="CANCELAR", bg="RED", command=self.vLista.destroy).grid(row=8, column=12)

        self.vLista.mainloop()

        
    def consultaci(self):
        ci = self.cedula.get()
        consultaCiV(self.ventana,ci)


