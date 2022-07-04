# Importar la libreria para GUI
from tkinter import *
from tkinter.ttk import Combobox

# importar la libreria para VENTANA DE MENSAJES
from tkinter import messagebox

import re

ventana = Tk()
ventana.title("Cálculo Desviación Estandar")

Label(ventana, text="Dato").grid(row=0)
txtDato = Entry(ventana)
txtDato.grid(row=0, column=1)

lstDatos = Listbox(ventana)
lstDatos.grid(row=2, column=0, columnspan=3)

cmbE = Combobox(ventana)
cmbE.grid(row=3, column=1)
cmbE["values"] = ("Sumatoria", "Promedio", "Desviacion Estandar", "Máximo", "Mínimo")  # Tupla

txtE = Entry(ventana)
txtE.grid(row=3, column=2)

datos = []


def sumatoria():
    suma = 0
    for i in range(0, len(datos)):
        suma += datos[i]
    return suma


def promedio():
    p = 0
    if len(datos) > 0:
        p = sumatoria() / len(datos)
    return p

def desviacion():
    d = 0
    if len(datos) > 1:
        s = 0
        p = promedio()
        for i in range(0, len(datos)):
            s += abs(p - datos[i])
        d = s / (len(datos) - 1)
    return d

def maximo():
    if len(datos) > 0:
        mayor = datos[0]
        for i in range(1, len(datos)):
            if mayor < datos[i]:
                mayor = datos[i]
    return mayor

def minimo():
    if len(datos) > 0:
        menor = datos[0]
        for i in range(1, len(datos)):
            if menor > datos[i]:
                menor = datos[i]
    return menor

def mostrar():
    # limpiar la lista
    lstDatos.delete(0, END)
    for i in range(0, len(datos)):
        # agregar datos a la lista
        lstDatos.insert(END, str(datos[i]))


def agregar():
    if re.match("^[0-9]+[.]?[0-9]*$", txtDato.get()):
        datos.append(float(txtDato.get()))
        mostrar()
    txtDato.delete(0, END)


def quitar():
    if len(lstDatos.curselection()) > 0:
        del datos[int(lstDatos.curselection()[0])]
        mostrar()

def quitarRepetidos():
    global datos
    #crear un conjunto apartir de los datos
    c = set(datos)
    datos = list(c)
    mostrar()

def calcular():
    if cmbE.current() >= 0:
        txtE.delete(0, END)
        if cmbE.current() == 0:
            txtE.insert(0, str(sumatoria()))
        elif cmbE.current() == 1:
            txtE.insert(0, str(promedio()))
        elif cmbE.current() == 2:
            txtE.insert(0, str(desviacion()))
        elif cmbE.current() == 3:
            txtE.insert(0, str(maximo()))
        elif cmbE.current() == 3:
            txtE.insert(0, str(minimo()))
        else:
            txtE.insert(0, str(desviacion()))
    else:
        messagebox.showerror("", "No ha seleccionado el estadístico")


Button(ventana, text="Agregar", command=agregar).grid(row=1, column=0)
Button(ventana, text="Quitar", command=quitar).grid(row=1, column=1)
Button(ventana, text="Quitar repetidos", command=quitarRepetidos).grid(row=1, column=2)
Button(ventana, text="Estadístico", command=calcular).grid(row=3, column=0)

ventana.mainloop()
