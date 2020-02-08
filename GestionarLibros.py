# -*- coding: utf-8 -*-

#author:Dex Loggica

from tkinter import *
from math import *


#creo la ventana
ventana = Tk()
#le coloco titulo a la ventana
ventana.title("Gestor de Libros")
#establezco el tamaño de la ventana
#ventana.geometry("450x450")
#┬hago que la ventana no se pueda modificar de tamaño
ventana.resizable(False,False)
#configuro el color de la ventana
ventana.configure(background="white")

#caracteristicas del boton
color_boton="gray99"
ancho_boton=10
alto_boton=1
entrada=StringVar()
#botones de la PRIMER fila
#el metodo grid es para situarlo en la pantalla
Texto0=Label(text="Libro: ",font=("Chiller",15),bg="white").grid(row=0,column=0,pady=10)
Titulo=Entry(ventana,textvariable=entrada).grid(row=0,column=1,pady=10)
Texto1=Label(text="Cantidad de paginas: ",font=("Chiller",15),bg="white").grid(row=1,column=0,pady=10)
CantPaginas=Entry(ventana,textvariable=entrada).grid(row=1,column=1,pady=10)

Registrar= Button(ventana, text="Registrar",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:click(0)).grid(row=2,column=0,pady=10)
Boton1= Button(ventana, text="Mostrar",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:click(1)).grid(row=2,column=1,pady=10)
#linea de codigo que va al final si o si
ventana.mainloop()