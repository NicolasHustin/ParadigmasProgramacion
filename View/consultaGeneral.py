from tkinter import *
from tkinter import font
import tkinter.ttk as ttk
from AppController import *
'tamaño de ventanas'
tamano="600x325+430+150"
tamano2="520x370+470+150"
'clor de las ventanas'
color='White'

class consultaGeneral():
    
    def __init__(self, ventana):
        self.ventana = ventana
        self.run(self.ventana)

    def run(self,ventana):
        self.vLista = Toplevel(ventana)
        self.vLista.config(bg=color)
        self.vLista.resizable(0,0)
        self.vLista.geometry(tamano)
        self.vLista.title("LISTA DE EMPLEADOS")
        self.vLista.grab_set()

        self.ComicSansMS = font.Font(family="Comic Sans MS",size=11,weight="bold")
        self.DejaVuSansMono = font.Font(family="DejaVu Sans Mono",size=15,weight="bold")

        Label(self.vLista, text="EMPLEADOS", bg='White', font=self.ComicSansMS).pack()

        # Crear una barra de deslizamiento con orientación vertical.
        scrollbarVertical = ttk.Scrollbar(self.vLista, orient=VERTICAL)
        scrollbarHorizontal = ttk.Scrollbar(self.vLista, orient=HORIZONTAL)

        self.listbox = Listbox(self.vLista, yscrollcommand=scrollbarVertical.set, xscrollcommand = scrollbarHorizontal.set, borderwidth=8,activestyle=None, bg='black', fg='gray',selectbackground='Red', selectborderwidth=2, font=self.ComicSansMS, selectmode=EXTENDED )

        scrollbarVertical.config(command = self.listbox.yview)
        scrollbarHorizontal.config(command = self.listbox.xview)
        scrollbarVertical.pack(side=RIGHT, fill=Y, expand= False)
        scrollbarHorizontal.pack(side=BOTTOM, fill=X, expand= False)
        self.listbox.pack(fill='both', expand='yes')

        listClient = Controller.getGeneralEmployees()

        for i in listClient:
            self.listbox.insert(END,i)
            self.listbox.insert(END, '****'*25)

        self.vLista.mainloop()



