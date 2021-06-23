from View.consultaCiV import consultaCiV
from APP_Controller import *
from Person import Customer
from Receipts import Invoice

from tkinter import *
from tkinter import font
from tkinter import messagebox
import tkinter.ttk as ttk
tamano='600x350+430+145'
colorFont='red'

class agregar_reserva():
    ''' clase que sirve a la vista para agregar una reserva '''

    def __init__(self, ventana):
        self.ventana = ventana
        self.run(self.ventana)

    def run(self, ventana):
        '''metodo que da inicio a la pantalla de agregar reserva'''

        #Tipo de letra para la fuente
        self.ComicSansMS = font.Font(family="Comic Sans MS",size=13,weight="bold")

        self.vReserva = Toplevel(ventana)
        self.vReserva.config(bg="white")
        self.vReserva.resizable(0, 0)
        self.vReserva.geometry(tamano)
        self.vReserva.title("AGREGAR RESERVA")
        self.vReserva.grab_set()

        self.pestaña = ttk.Notebook(self.vReserva)
        self.pestaña.pack(fill='both', expand='yes')

        self.frmcli = Frame(self.pestaña, bg='White', highlightthickness=2, highlightbackground='black')
        self.frmbien = Frame(self.pestaña, bg='White',highlightthickness=2, highlightbackground='black')

        self.pestaña.add(self.frmcli, text='Cliente')
        self.pestaña.add(self.frmbien, text='Articulos')

        Label(self.frmcli, text="Cedula*:",bg='White',font=self.ComicSansMS).place(x=60,y=25)
        self.cedula = Entry(self.frmcli)
        self.cedula.focus()
        self.cedula.place(x=160, y=30)

        #BOTON PARA AUTOCOMPLETAR CON LOS DATOS DE UN CLIENTE
        #FALTA IMPLEMENTAR, DEBIDO A QUE SE SUPERPONEN EN LAS PESTAÑAS
        #self.btonAgregar = Button(self.vReserva, text="CONSULTAR", bg="green",command=self.consultaci)
        #self.btonAgregar.place(x=350, y=50)

        Label(self.frmcli, text="Ruc: ",bg='White',font=self.ComicSansMS).place(x=60,y=70)
        self.ruc = Entry(self.frmcli)
        self.ruc.place(x=160,y=75)

        Label(self.frmcli, text="Nombre: ",bg='White',font=self.ComicSansMS).place(x=60,y=115)
        self.nombre = Entry(self.frmcli)
        self.nombre.place(x=160,y=120)

        Label(self.frmcli, text="Apellido: ",bg='White',font=self.ComicSansMS).place(x=60,y=160)
        self.apellido = Entry(self.frmcli)
        self.apellido.place(x=160,y=165)

        Label(self.frmcli, text="Direccion: ",bg='White',font=self.ComicSansMS).place(x=60,y=205)
        self.direccion = Entry(self.frmcli)
        self.direccion.place(x=160,y=210)

        Label(self.frmcli, text="Telefono: ",bg='White',font=self.ComicSansMS).place(x=60,y=250)
        self.telefono = Entry(self.frmcli)
        self.telefono.place(x=160,y=255)

        self.MVBoli=font.Font(family="MV Boli",size=9,weight="bold")

        Label(self.frmbien, text="ARTICULOS",bg='White',  font=self.ComicSansMS).place(x=250,y=0)

        Label(self.frmbien, text="CANT. SILLAS HIERRO:",bg='White',  font=self.MVBoli).place(x=120,y=24)
        self.grande = Entry(self.frmbien)
        self.grande.place(x=325,y=26)
        Label(self.frmbien, text="SILLAS",bg='White',  font=self.MVBoli).place(x=0,y=44)
        Label(self.frmbien, text="CANT. SILLAS PLASTICO:",bg='White',  font=self.MVBoli).place(x=120,y=70)
        self.pequena = Entry(self.frmbien)
        self.pequena.place(x=325,y=72)

        Label(self.frmbien, text="CANT. MESA LARGA:",bg='White',  font=self.MVBoli).place(x=120,y=98)
        self.rectangulo = Entry(self.frmbien)
        self.rectangulo.place(x=325,y=98)

        Label(self.frmbien, text="MESA",bg='White',  font=self.MVBoli).place(x=0,y=120)
        Label(self.frmbien, text="CANT. MESA CHICA:",bg='White',  font=self.MVBoli).place(x=120,y=146)
        self.redonda = Entry(self.frmbien)
        self.redonda.place(x=325,y=148)

        Label(self.frmbien, text="CANT. VASOS:",bg='White',  font=self.MVBoli).place(x=120,y=172)
        self.vaso = Entry(self.frmbien)
        self.vaso.place(x=325,y=174)
        Label(self.frmbien, text="ARTICULO COCINA",bg='White',  font=self.MVBoli).place(x=0,y=198)
        Label(self.frmbien, text="CANT. PLATOS:",bg='White',  font=self.MVBoli).place(x=120,y=198)
        self.plato = Entry(self.frmbien)
        self.plato.place(x=325,y=200)
        Label(self.frmbien, text="CANT. CUBIERTOS:",bg='White',  font=self.MVBoli).place(x=120,y=224)
        self.aparejo = Entry(self.frmbien)
        self.aparejo.place(x=325,y=226)

        Label(self.frmbien, text="TELAS",bg='White',  font=self.MVBoli).place(x=0,y=250)
        Label(self.frmbien, text="CANT. TELAS:",bg='White',  font=self.MVBoli).place(x=120,y=250)

        self.cubre = Entry(self.frmbien)
        self.cubre.place(x=325,y=252)

        self.btonAgregar = Button(self.vReserva, text="Reservar", bg='green',command=self.add_cliente)
        self.btonAgregar.place(x=430,y=305)

        Button(self.vReserva, text="Cancelar", bg="red",command=self.vReserva.destroy).place(x=510,y=305)

        self.vReserva.mainloop()

    def add_cliente(self):
        self.vReserva.destroy()
        messagebox.showinfo("addCustomer", "FALTA IMPLEMENTAR")
        #TODO:
        #aqui agregarmos al cliente una reserva, con articulos y queda guardado, al momento de la devolucion se vuelve a 0

    def validate(self, value):
        if not value.isdigit():
            raise Exception("Cedula o Ruc invalida")

    def agg_reserva(self):
        #TODO: Implementar el metodo
        pass

    def invoice(self, customer):
        pass
        #messagebox.showinfo('Factura',Factura.calcular(cliente))

    def consulta_ci(self):
        ci = self.cedula.get()
        consultaCiV







