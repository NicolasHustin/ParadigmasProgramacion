from tkinter import *
from tkinter import font
from tkinter import messagebox
from Person import Employee
from AppController import *

tamano = "500x220+475+180"

class aggEmpleado():

    def __init__(self,ventana):
        self.ventana = ventana
        self.run(self.ventana)

    def run(self,ventana):

        self.vEmpl = Toplevel(ventana)
        self.vEmpl.config(bg='White')
        self.vEmpl.resizable(0, 0)
        self.vEmpl.geometry(tamano)
        self.vEmpl.title("Registrar")
        self.vEmpl.grab_set()

        ComicSansMS = font.Font(family="Comic Sans MS",size=11,weight="bold")
        DejaVuSansMono = font.Font(family="DejaVu Sans Mono",size=15,weight="bold")
        Label(self.vEmpl, text="REGISTRAR EMPLEADO", bg='White',font=DejaVuSansMono).grid(row=1, column=10)

        Label(self.vEmpl, text="Cedula*:",bg='White',font=ComicSansMS).grid(row=5, column=9)
        self.cedula = Entry(self.vEmpl)
        self.cedula.focus()
        self.cedula.grid(row=5, column=10)

        Label(self.vEmpl, text="Nombre: ",bg='White',font=ComicSansMS).grid(row=6, column=9)
        self.nombre = Entry(self.vEmpl)
        self.nombre.grid(row=6, column=10)

        Label(self.vEmpl, text="Apellido: ",bg='White',font=ComicSansMS).grid(row=7, column=9)
        self.apellido = Entry(self.vEmpl)
        self.apellido.grid(row=7, column=10)

        Label(self.vEmpl, text="Direccion: ",bg='White',font=ComicSansMS).grid(row=8, column=9)
        self.direccion = Entry(self.vEmpl)
        self.direccion.grid(row=8, column=10)

        Label(self.vEmpl, text="Telefono: ",bg='White',font=ComicSansMS).grid(row=9, column=9)
        self.telefono = Entry(self.vEmpl)
        self.telefono.grid(row=9, column=10)

        Label(self.vEmpl, text="Sueldo: ",bg='White',font=ComicSansMS).grid(row=10, column=9)
        self.sueldo = Entry(self.vEmpl)
        self.sueldo.focus()
        self.sueldo.grid(row=10, column=10)

        self.btonAgregar = Button(self.vEmpl, text="Agregar", bg="green", command=self.addempleado)
        self.btonAgregar.grid(row=6, column=12)

        Button(self.vEmpl, text="Cancelar", bg="red",command=self.vEmpl.destroy).grid(row=8, column=12)

        self.vEmpl.mainloop()

    def addempleado(self):
        ci=self.cedula.get()
        nombre = self.nombre.get()
        apellido = self.apellido.get()
        direccion = self.direccion.get()
        telefono = self.telefono.get()
        salary = self.sueldo.get()

        try:
            self.validateNumeric(ci)
            self.validateNumeric(salary)
            newEmpleado = Employee(salary, name=nombre, lastName=apellido, ci=ci, address=direccion, telephone=telefono)
            self.vEmpl.destroy()
            Controller.addEmployee(ci,newEmpleado)
            messagebox.showinfo("EMPLEADO", "EMPLEADO AGREGADO CON EXITO")

        except Exception as e:
            messagebox.showerror("ERROR", e)

    def validateNumeric(self, value):
        if not value.isdigit():
            raise Exception("Debe ser un valor numerico")
