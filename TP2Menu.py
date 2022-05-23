# Elaborado por: Juan Ceballos y Esteban Solano
# Fecha de Creación: 04/05/2022 04:53pm
# Fecha de última Modificación: XX/XX/2022 XX:XXxm
# Versión: 3.10.2

# Importación de librerías
from TP2Funciones import *
from tkinter import *
from tkinter.scrolledtext import ScrolledText
import re
import random
from turtle import width
import smtplib

# Variables globales
matrizPart = []
diccPaises = {}
enlazados = {}

def cerrarPantalla(ppantalla): # Función de "Salir" de la pantalla
    ppantalla.destroy()
    return ""

def cargarBdPaises():
    botonIns1P.config(state=ACTIVE)
    botonInsNP.config(state=ACTIVE)
    botonEnlazarAbu.config(state=ACTIVE)
    botonDarBaja.config(state=ACTIVE)
    botonCorreo.config(state=ACTIVE)
    botonReportes.config(state=ACTIVE)
    diccPaises
    with open("paises.txt") as file:
        for i in file:
            region, pais=i.strip("\n").split(":")
            pais=pais.split(",")
            diccPaises[region]=pais
    return diccPaises

#================================================================================================================================================#
#                                                             PROGRAMA PRINCIPAL
#================================================================================================================================================#
# Creación y xonfiguración de la raiz
raiz = Tk()
raiz.title("Adoptemos un Adulto Mayor")
raiz.geometry("600x750")
raiz.resizable(True, True)
raiz.config(cursor = "star")

#================================================================================================================================================#
#                                                       SECCION DE INTERFACES GRÁFICAS
#================================================================================================================================================#
# Interfaz ingresar participante
def guiInsertarPart():
    raiz.deiconify()
    pIngresarPart = Toplevel()
    pIngresarPart.geometry("600x750")
    pIngresarPart.config(cursor = "star")
    
    Label(pIngresarPart, text = "Insertar un participante", font = ("Impact", 25), fg = "Black").place(x = 30, y = 30)

    Label(pIngresarPart, text = "Fecha de nacimiento", font = ("Helvetica", 14), fg = "Black").place(x = 30, y = 110)
    entradaFechaN = Entry(pIngresarPart, width = 23, font = ("Helvetica", 14), relief = "raised", bg = "Orange")
    entradaFechaN.place(x = 300, y = 115)

    Label(pIngresarPart, text = "Tipo de participante", font = ("Helvetica", 14), fg = "Black").place(x = 30, y = 155)
    radioBAdultoMayor = Radiobutton(pIngresarPart, text = "Adulto Mayor", font = ("Helvetica", 12), variable = 1, value = 1)
    radioBVoluntario = Radiobutton(pIngresarPart, text = "Voluntario", font = ("Helvetica", 12), variable = 0, value = 1)
    radioBAdultoMayor.place(x = 300, y = 160)
    radioBVoluntario.place(x = 300, y = 200)

    Label(pIngresarPart, text = "Identificador de participante", font = ("Helvetica", 14), fg = "Black").place(x = 30, y = 240)
    entradaIdenPart = Label(pIngresarPart, width = 23, font = ("Helvetica", 14), relief = "raised", bg = "Orange")
    entradaIdenPart.place(x = 300, y = 245)

    Label(pIngresarPart, text = "Nombre completo", font = ("Helvetica", 14), fg = "Black").place(x = 30, y = 285)
    entradaNombreC = Label(pIngresarPart, width = 23, font = ("Helvetica", 14), relief = "raised", bg = "Orange")
    entradaNombreC.place(x = 300, y = 290)

    Label(pIngresarPart, text = "Hobbies", font = ("Helvetica", 14), fg = "Black").place(x = 30, y = 330)
    entradaHobbies = Label(pIngresarPart, width = 23, font = ("Helvetica", 14), relief = "raised", bg = "Orange")
    entradaHobbies.place(x = 300, y = 335)

    Label(pIngresarPart, text = "Profesión u oficio", font = ("Helvetica", 14), fg = "Black").place(x = 30, y = 375)
    entradaOcupacion = Label(pIngresarPart, width = 23, font = ("Helvetica", 14), relief = "raised", bg = "Orange")
    entradaOcupacion.place(x = 300, y = 380)

    Label(pIngresarPart, text = "Correo electrónico", font = ("Helvetica", 14), fg = "Black").place(x = 30, y = 420)
    entradaCorreo = Label(pIngresarPart, width = 23, font = ("Helvetica", 14), relief = "raised", bg = "Orange")
    entradaCorreo.place(x = 300, y = 425)

    Label(pIngresarPart, text = "País de Origen", font = ("Helvetica", 14), fg = "Black").place(x = 30, y = 465)
    entradaPais = Label(pIngresarPart, width = 23, font = ("Helvetica", 14), relief = "raised", bg = "Orange")
    entradaPais.place(x = 300, y = 470)

    Label(pIngresarPart, text = "Estado", font = ("Helvetica", 14), fg = "Black").place(x = 30, y = 510)
    entradaEstado = Label(pIngresarPart, width = 23, font = ("Helvetica", 14), relief = "raised", bg = "Orange")
    entradaEstado.place(x = 300, y = 515)

    Label(pIngresarPart, text = "Descripción", font = ("Helvetica", 14), fg = "Black").place(x = 30, y = 555)
    entradaDescripcion = ScrolledText(pIngresarPart, width = 23, height = 4, font = ("Helvetica", 14), relief = "raised", bg = "Orange")
    entradaDescripcion.place(x = 300, y = 560)

    botonIngresar = Button(pIngresarPart, text = "Ingresar", padx = 30, pady = 5, font = ("Impact", 13), relief = "raised", fg = "White", bg = "Black")
    botonIngresar.place(x = 63, y = 677)

    botonLimpiar = Button(pIngresarPart, text = "Limpiar", padx = 30, pady = 5, font = ("Impact", 13), relief = "raised", fg = "White", bg = "Black")
    botonLimpiar.place(x = 233, y = 677)

    botonRegresar = Button(pIngresarPart, text = "Regresar", padx = 30, pady = 5, font = ("Impact", 13), relief = "raised", fg = "White", bg = "Black", command = lambda: cerrarPantalla(pIngresarPart))
    botonRegresar.place(x = 400, y = 677)

# Interfaz ingresar n participantes
def guiInsertarNPart():
    raiz.deiconify()
    pIngresarNPart = Toplevel()
    pIngresarNPart.geometry("500x250")
    pIngresarNPart.config(cursor = "star")

    Label(pIngresarNPart, text = "Insertar n participantes", font = ("Impact", 25), fg = "Black").place(x = 20, y = 30)

    Label(pIngresarNPart, text = "Cantidad a generar", font = ("Helvetica", 14), fg = "Black").place(x = 20, y = 100)
    entradaFechaN = Entry(pIngresarNPart, width = 20, font = ("Helvetica", 14), relief = "raised", bg = "Orange")
    entradaFechaN.place(x = 230, y = 105)

    botonIngresar = Button(pIngresarNPart, text = "Ingresar", padx = 30, pady = 5, font = ("Impact", 13), relief = "raised", fg = "White", bg = "Black")
    botonIngresar.place(x = 20, y = 180)

    botonLimpiar = Button(pIngresarNPart, text = "Limpiar", padx = 30, pady = 5, font = ("Impact", 13), relief = "raised", fg = "White", bg = "Black")
    botonLimpiar.place(x = 180, y = 180)

    botonRegresar = Button(pIngresarNPart, text = "Regresar", padx = 30, pady = 5, font = ("Impact", 13), relief = "raised", fg = "White", bg = "Black", command = lambda: cerrarPantalla(pIngresarNPart))
    botonRegresar.place(x = 340, y = 180)

# Interfaz enlazar con abuelos
def guiEnlazarConAbu():
    raiz.deiconify()
    pEnlazarConAbu = Toplevel()
    pEnlazarConAbu.geometry("280x180")
    pEnlazarConAbu.config(cursor = "star")

    Label(pEnlazarConAbu, text = "Enlace creado", font = ("Impact", 20), fg = "Black").place(x = 23, y = 20)
    Label(pEnlazarConAbu, text = "satisfactoriamente", font = ("Impact", 20), fg = "Black").place(x = 23, y = 50)

    botonRegresar = Button(pEnlazarConAbu, text = "Regresar", padx = 30, pady = 5, font = ("Impact", 12), relief = "raised", fg = "White", bg = "Black", command = lambda: cerrarPantalla(pEnlazarConAbu))
    botonRegresar.place(x = 75, y = 115)

# Interfaz dar de baja
def guiDarDeBaja():
    raiz.deiconify()
    pDarDeBaja = Toplevel()
    pDarDeBaja.geometry("500x250")
    pDarDeBaja.config(cursor = "star")

    Label(pDarDeBaja, text = "Dar de baja", font = ("Impact", 25), fg = "Black").place(x = 20, y = 30)

    Label(pDarDeBaja, text = "Código de participante", font = ("Helvetica", 14), fg = "Black").place(x = 20, y = 100)
    entradaFechaN = Entry(pDarDeBaja, width = 20, font = ("Helvetica", 14), relief = "raised", bg = "Orange")
    entradaFechaN.place(x = 230, y = 105)

    botonBaja = Button(pDarDeBaja, text = "Baja", padx = 40, pady = 5, font = ("Impact", 13), relief = "raised", fg = "White", bg = "Black")
    botonBaja.place(x = 20, y = 180)

    botonLimpiar = Button(pDarDeBaja, text = "Limpiar", padx = 30, pady = 5, font = ("Impact", 13), relief = "raised", fg = "White", bg = "Black")
    botonLimpiar.place(x = 180, y = 180)

    botonRegresar = Button(pDarDeBaja, text = "Regresar", padx = 30, pady = 5, font = ("Impact", 13), relief = "raised", fg = "White", bg = "Black", command = lambda: cerrarPantalla(pDarDeBaja))
    botonRegresar.place(x = 340, y = 180)

# Interfaz escribe una carta a su correo
def guiEnviarCorreo():
    raiz.deiconify()
    pEnviarCorreo = Toplevel()
    pEnviarCorreo.geometry("280x180")
    pEnviarCorreo.config(cursor = "star")

    Label(pEnviarCorreo, text = "Correo enviado", font = ("Impact", 20), fg = "Black").place(x = 23, y = 20)
    Label(pEnviarCorreo, text = "satisfactoriamente", font = ("Impact", 20), fg = "Black").place(x = 23, y = 50)

    botonRegresar = Button(pEnviarCorreo, text = "Regresar", padx = 30, pady = 5, font = ("Impact", 12), relief = "raised", fg = "White", bg = "Black", command = lambda: cerrarPantalla(pEnviarCorreo))
    botonRegresar.place(x = 75, y = 115)

# Interfaz Menú principal
Label(raiz, text = "Adoptemos un Adulto Mayor", font = ("Impact", 25), fg = "Black").place(x = 113, y = 50)

botonBDPaises = Button(raiz, text = "Cargar BD de países", padx = 147, pady = 5, font = "Impact", relief = "raised", fg = "White", bg = "Black", command = cargarBdPaises)
botonBDPaises.place(x = 65, y = 150)

botonIns1P = Button(raiz, text = "Insertar un participante", padx = 132, pady = 5, font = "Impact", relief = "raised", fg = "White", bg = "Black", command = guiInsertarPart)
botonIns1P.place(x = 65, y = 220)
botonIns1P.config(state=DISABLED)

botonInsNP = Button(raiz, text = "Insertar n participantes", padx = 132, pady = 5, font = "Impact", relief = "raised", fg = "White", bg = "Black", command = guiInsertarNPart)
botonInsNP.place(x = 65, y = 290)
botonInsNP.config(state=DISABLED)

botonEnlazarAbu = Button(raiz, text = "Enlazar con abuelos", padx = 148, pady = 5, font = "Impact", relief = "raised", fg = "White", bg = "Black", command = guiEnlazarConAbu)
botonEnlazarAbu.place(x = 65, y = 360)
botonEnlazarAbu.config(state=DISABLED)

botonDarBaja = Button(raiz, text = "Dar de baja", padx = 182, pady = 5, font = "Impact", relief = "raised", fg = "White", bg = "Black", command = guiDarDeBaja)
botonDarBaja.place(x = 65, y = 430)
botonDarBaja.config(state=DISABLED)

botonCorreo = Button(raiz, text = "Escribe una carta a su correo", padx = 110, pady = 5, font = "Impact", relief = "raised", fg = "White", bg = "Black", command = guiEnviarCorreo)
botonCorreo.place(x = 65, y = 500)
botonCorreo.config(state=DISABLED)

botonReportes = Button(raiz, text = "Reportes", padx = 191, pady = 5, font = "Impact", relief = "raised", fg = "White", bg = "Black")
botonReportes.place(x = 65, y = 570)
botonReportes.config(state=DISABLED)

botonSalir = Button(raiz, text = "Salir", padx = 209, pady = 5, font = "Impact", relief = "raised", fg = "White", bg = "Black", command = lambda: cerrarPantalla(raiz))
botonSalir.place(x = 65, y = 640)

raiz.mainloop()