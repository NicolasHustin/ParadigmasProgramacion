from tkinter import *
from tkinter import messagebox  
from tkinter import font
import tkinter.ttk as ttk
from Leasable import *
#Constantes para la clase
color='white'
tamaño="600x325+430+150"
class presupuesto():

    def __init__(self, ventana):
        self.ventana = ventana
        self.run(ventana)

    def run(self,ventana):

        self.vPre = Toplevel(ventana)
        self.vPre.config(bg=color)
        self.vPre.resizable(0, 0)
        self.vPre.geometry(tamaño)
        self.vPre.title("PRESUPUESTO")
        self.vPre.grab_set()

        self.ComicSansMS = font.Font(family="Comic Sans MS",size=11,weight="bold")
        self.DejaVuSansMono = font.Font(family="DejaVu Sans Mono",size=15,weight="bold")

        Label(self.vPre, text="PRESUPUESTO", bg='White', font=self.DejaVuSansMono).grid(row=1, column=2)

        self.btonCalcular = Button(self.vPre, text="CALCULAR", command=self.calcular)
        self.btonCalcular.grid(row=11, column=3)

        Button(self.vPre, text="Cancelar", command=self.vPre.destroy).grid(row=11, column=5)
        self.vPre.mainloop()

    def calcular(self):
        self.vPre.destroy()
        messagebox.showinfo("calc", "FALTA IMPLEMENTAR")
        pass



