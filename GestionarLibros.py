# -*- coding: utf-8 -*-

#author:Dex Loggica

#from pymysql import *
####################################BASE DE DATOS
#me conecto a la base de datos
import pymysql



####################################
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
title=StringVar()
#title="hola"
cant=IntVar()
#cant=0

#botones de la PRIMER fila
#el metodo grid es para situarlo en la pantalla
Texto0=Label(text="Libro: ",font=("Chiller",15),bg="white").grid(row=0,column=0,pady=10)
Entry0=Entry(ventana,textvariable=title).grid(row=0,column=1,pady=10)
Texto1=Label(text="Cantidad de paginas: ",font=("Chiller",15),bg="white").grid(row=1,column=0,pady=10)
Entry1=Entry(ventana,textvariable=cant).grid(row=1,column=1,pady=10)

def conectar():
    connection = pymysql.connect(host='localhost',user='root',password='', db='20181020_version1')
    return connection

def insertar():
    print(title.get())
    print(cant.get())
    #print(title1)
   # print(cant1)
    #print(Entry0)
    #print(Entry1)
    titulo=title.get()
    cantidad=cant.get()
    
    print(titulo)
    print(cantidad)
    #abro la conexion
    connect = conectar()
    #creo el puntero
    cursor=connect.cursor()
    #realizar consulta sql
    sql="INSERT INTO libro (Titulo,Numero,Pais_idPais,Editorial_idEditorial,Estado) VALUES ('%s', '%d', '%d', '%d', '%d')" % (titulo, cantidad,1,1,1)
    try:
        print("try")
        cursor.execute(sql)
        #cerrar puntero
        connect.commit()
    except:
        print("except")
        #en el caso de error
        connect.rollback()
        
    cursor.close()
    connect.close()
    
def mostrar():
    connect = conectar()
    cursor=connect.cursor()
    cursor.execute("SELECT idLibro, Titulo FROM libro")
    
    for Titulo, Numero in cursor.fetchall():
        print("{0} {1}".format(Titulo, Numero))
    
    cursor.close()
    connect.commit()
    connect.close()
    
    
def main():
    Registrar= Button(ventana, text="Registrar",bg=color_boton,width=ancho_boton,height=alto_boton,command= insertar).grid(row=2,column=0,pady=10)
    Mostrar= Button(ventana, text="Mostrar",bg=color_boton,width=ancho_boton,height=alto_boton,command= mostrar).grid(row=2,column=1,pady=10)
    #linea de codigo que va al final si o si
    ventana.mainloop()

if __name__ == "__main__":
    main()
