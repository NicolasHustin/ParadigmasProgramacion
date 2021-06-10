from tkinter import *
from AppController import *
from tkinter import font
from tkinter import messagebox
tamano = "400x120+520+180"
class devolver():
    ''' clase para registrar las devoluciones '''

    def __init__(self,ventana):
        self.ventana=ventana
        self.run(ventana)

    def run(self,ventana):
        self.vDevuelve = Toplevel(ventana)
        self.vDevuelve.config(bg='white')
        self.vDevuelve.resizable(0, 0)
        self.vDevuelve.geometry(tamano)
        self.vDevuelve.title("DEVOLUCIONES")
        self.vDevuelve.grab_set()

        self.id = IntVar()
        self.id.set('')
        self.ComicSansMS = font.Font(family="Comic Sans MS",size=11,weight="bold")
        self.MVBoli=font.Font(family="MV Boli",size=15,weight="bold")

        Label(self.vDevuelve, text="DEVOLUCIONES", bg='White',font=self.MVBoli).place(x=100,y=0)
        Label(self.vDevuelve, text="N° CEDULA: ", bg='White',font=self.ComicSansMS).place(x=50,y=50)

        self.cedula = Entry(self.vDevuelve, textvariable=self.id)
        self.cedula.focus()
        self.cedula.place(x=155, y=55)

        Button(self.vDevuelve, text="Devolver", command=self.devoluciones).place(x=241, y=90)
        Button(self.vDevuelve, text="Cancelar", command=self.vDevuelve.destroy).place(x=320, y=90)

    def devoluciones(self):
        ci=self.cedula.get()
        try:
            self.validar(ci)
            self.vDevuelve.destroy()
            Controller.returnArticles()
            messagebox.showinfo('Aviso','EXITO AL DEVOLVER')
        except Exception as e:
            messagebox.showerror("ERROR", e)

    def validar(self, value):
        if not value.isdigit():
            raise Exception("Debe ser un numero")