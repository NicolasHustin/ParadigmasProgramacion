from tkinter import *
from tkinter import font
import tkinter.ttk as ttk
from APP_Controller import *
'tamaño de ventanas'
tamano="600x325+430+150"
tamano2="520x370+470+150"
'clor de las ventanas'
color='White'

class consultaCiV():
    def __init__(self, ventana, ci):
        self.ventana=ventana
        self.ci=ci
        self.run(ventana)

    def run(self,ventana):
        self.vCi=Toplevel(ventana)
        self.vCi.config(bg=color)
        self.vCi.resizable(0,0)
        self.vCi.geometry(tamano)
        self.vCi.title("CONSULTA POR CI")
        self.vCi.grab_set()

        empl = Controller.employee_inquiry(self.ci)

        scrollbarVertical = ttk.Scrollbar(self.vCi, orient=VERTICAL)
        scrollbarHorizontal = ttk.Scrollbar(self.vCi, orient=HORIZONTAL)
        self.ComicSansMS = font.Font(family="Comic Sans MS",size=11,weight="bold")

        self.listbox = Listbox(self.vCi, yscrollcommand=scrollbarVertical.set, xscrollcommand = scrollbarHorizontal.set, borderwidth=8,activestyle=None, bg='black', fg='gray',selectbackground='Red', selectborderwidth=2, font=self.ComicSansMS, selectmode=EXTENDED )
        scrollbarVertical.config(command = self.listbox.yview)
        scrollbarHorizontal.config(command = self.listbox.xview)
        scrollbarVertical.pack(side=RIGHT, fill=Y, expand= False)
        scrollbarHorizontal.pack(side=BOTTOM, fill=X, expand= False)
        self.listbox.pack(fill='both', expand='yes')

        self.listbox.insert(END,'****'*35)
        self.listbox.insert(END,"NO SE ENCONTRO UN EMPLEADO" if empl is None else empl)
        self.listbox.insert(END,'****'*35)

        self.vCi.mainloop()
