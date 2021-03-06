# Elaborado por: Juan Ceballos y Esteban Solano
# Fecha de Creación: 05/05/2022 02:00pm
# Fecha de última Modificación: 27/05/2022 11:35am
# Versión: 3.10.2

# Importación de librerías
from tkinter import *
from tkinter.scrolledtext import ScrolledText
import re
import random
import smtplib
from asyncore import read
from csv import writer
import csv

# Variables globales
matrizPart = []
diccPaises = {}
enlazados = {}

#================================================================================================================================================#
#                                                           DEFINICIÓN DE FUNCIONES
#================================================================================================================================================#
# Funciones de GUI
def cerrarPantalla(ppantalla): # Función de "Salir" de la pantalla
    ppantalla.destroy()
    return ""

#Definición de funciones
def cantidadAdultM():
    matrizPart
    contador = 0
    for i in matrizPart:
        if i[2][0] == "a":
            contador += 1
    return contador

def cantidadVolunt():
    matrizPart
    contador = 0
    for i in matrizPart:
        if i[2][0] == "v":
            contador += 1
    return contador

def generarFecha():
    eleccion = random.randint(0,1)
    if eleccion == 0:
        anno = str(random.randint(1997, 2005) or random.randint(1901, 1967))
    else:
        anno = str(random.randint(1901, 1967))
    mes = str(random.randint(1,12))
    if len(mes) == 1:
        mes = "0"+mes
    dia = str(random.randint(1,31))
    if len(dia) == 1:
        dia = "0"+dia
    return dia+"/"+mes+"/"+anno

def generarNombre():
    nombres = []
    apellidos = []
    aps = []
    archivo = open("nombres.txt", "r")
    for i in archivo:
        nombres.append(i)
    archivo.close()
    archivo = open("apellidos.txt", "r")
    for i in archivo:
        apellidos.append(i)
    archivo.close()
    indiceN = random.randint(0,127)
    for i in range(2):
        indiceA = random.randint(0,94)
        aps.append(indiceA)
    nombre = nombres[indiceN]
    ap1 = apellidos[aps[0]]
    ap2 = apellidos[aps[1]]
    nombre = nombre[:-1]
    ap1 = ap1[:-1]
    ap2 = ap2[:-1]
    return (nombre, ap1, ap2)

def generarDescripcion():
    codigoTel = random.randint(100,999)
    num1 = random.randint(1000,9999)
    num2 = random.randint(1000,9999)
    descripcion = "("+str(codigoTel)+")"+str(num1)+"-"+str(num2)
    return descripcion

def validarFechaN(fechaN):
    if re.match("^\d{2}\/\d{2}\/\d{4}$", fechaN):
        return fechaN
    print("Debe ingresar una fecha de nacimiento con el formato (##/##/####). Por favor inténtelo de nuevo.\n")
    return False

def validarNombre(pnombre):
    if re.match("^[A-Z]{1}[a-z]{1,}", pnombre):
        return True
    return False

def ingresarNombre(n, ap1, ap2):
    if validarNombre(n) == True:
        if validarNombre(ap1) == True:
            if validarNombre(ap2) == True:
                return n, ap1, ap2
            else:
                return 1
        else:
            return 1
    else:
        return 0

def validarCantidadH(cantidad):
    if isinstance(cantidad, int):
        if cantidad >= 1 and cantidad <= 3:
            return cantidad
        print("Debe ingresar un valor entre 1 y 3.")
        return validarCantidadH(cantidad)
    print("Debe ingresar un valor numérico.")
    return validarCantidadH(cantidad)

def validarCodigo(pcodigo):
    if re.match("^v\d{5}$", pcodigo) or re.match("^am\d{5}$", pcodigo):
        return True
    return False

def agregarFechaNYTipoPart(pparticipante, fechaN):
    edad = 0
    edad = 2022 - int(fechaN[6:])
    if 17 <= edad <= 25:
        pparticipante.append(fechaN)
        pparticipante.append(False)
        return pparticipante
    elif 55 <= edad <= 121:
        pparticipante.append(fechaN)
        pparticipante.append(True)
        return pparticipante
    else:
        return False

def identificarPart(pparticipante):
    identificador = ""
    num = ""
    for i in range(5):
        num += str(random.randint(0, 9))
    if pparticipante[1] == False:
        identificador = "v"+num
    else:
        identificador = "am"+num
    pparticipante.append(identificador)
    return pparticipante

def agregarNombre(pparticipante, tuplaNombres):
    pparticipante.append(tuplaNombres)
    return pparticipante

def agregarHobbies(pparticipante, cantidad):
    listaHobbies = []
    num = ""
    for i in range(cantidad):
        num += str(random.randint(1, 25))
        listaHobbies.append("hobbie"+num)
        num = ""
    pparticipante.append(listaHobbies)
    return pparticipante

def agregarOcupacion(pparticipante):
    ocupacion = ()
    num2 = ""
    num1 = random.randint(0, 9)
    for i in range(2):
        num2 += str(random.randint(0, 9))
    ocupacion = (num1,int(num2))
    pparticipante.append(ocupacion)
    return pparticipante

def agregarCorreoE(pparticipante):
    correo = ""
    nombre = pparticipante[3][0].lower()
    apellido = pparticipante[3][1].lower()
    correo = str(nombre[0])+str(apellido)+"@gmail.com"
    pparticipante.append(correo)
    return pparticipante

def agregarPaisOrigen(pparticipante):
    region = ""
    pais = ""
    origen = ()
    llaves = []
    valores = []
    indiceRegion = 0
    indicePais = 0
    llaves = list(diccPaises.keys())
    indiceRegion = random.randint(0, len(llaves) - 1)
    region = str(llaves[indiceRegion])
    valores = list(diccPaises.get(region))
    indicePais = random.randint(0, len(valores) - 1)
    pais = str(valores[indicePais])
    origen = (region, pais)
    pparticipante.append(origen)
    return pparticipante

def agregarDescripcion(pparticipante, descripcion):
    pparticipante.append(descripcion)
    return pparticipante

def agregarAdoptado(pparticipante):
    if pparticipante[2][0] == "a":
        pparticipante.append(False)
    return pparticipante

def adoptadoTrue(penlazados):
    matrizPart
    indice = 0
    indiceEnlazados = 0
    llavesEnlazados = list(penlazados.keys())
    for i in matrizPart:
        for j in range(len(llavesEnlazados)):
            if i[2] == llavesEnlazados[indiceEnlazados]:
                matrizPart[indice][10] = True
                break
            indiceEnlazados += 1
        indice += 1
        indiceEnlazados = 0
    return matrizPart

def adoptadoFalse(pcodigo):
    matrizPart
    for i in matrizPart:
        if i[2] == pcodigo:
            i[10] = False
            break
    return matrizPart

def existeEnBd(pcodigo):
    matrizPart
    for i in matrizPart:
        if pcodigo == i[2]:
            return True
    return False

def modificaEstado(pcodigo):
    estado = ()
    valor = 0
    justificacion = ""
    for i in matrizPart:
        if i[2] == pcodigo:
            valor = 0
            justificacion = input("Por favor indique la razón por la que se retira de la comunidad: ")
            estado = (valor, justificacion)
            i[8] = estado
            break
    return matrizPart

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

def insertarPart(fechaN, n, ap1, ap2, cantidad, descripcion):
    participante = []
    agregarFechaNYTipoPart(participante, fechaN)
    identificarPart(participante)
    tuplaNombres = (n,ap1,ap2)
    agregarNombre(participante, tuplaNombres)
    cantidad = validarCantidadH(cantidad)
    agregarHobbies(participante, cantidad)
    agregarOcupacion(participante)
    agregarCorreoE(participante)
    agregarPaisOrigen(participante)
    participante.append((1, ""))
    agregarDescripcion(participante, descripcion)
    agregarAdoptado(participante)
    matrizPart.append(participante)
    print(matrizPart)
    return ""

def insertarNPart(num):
    try:
        if num >= 10:
            for i in range(num):
                participante = []
                fechaN = generarFecha()
                agregarFechaNYTipoPart(participante, fechaN)
                identificarPart(participante)
                tuplaNombres = generarNombre()
                agregarNombre(participante, tuplaNombres)
                cantidad = random.randint(1,3)
                agregarHobbies(participante, cantidad)
                agregarOcupacion(participante)
                agregarCorreoE(participante)
                agregarPaisOrigen(participante)
                participante.append((1, ""))
                descripcion = generarDescripcion()
                agregarDescripcion(participante, descripcion)
                agregarAdoptado(participante)
                matrizPart.append(participante)
            print(matrizPart)
            return ""
        else:
            print("Debe ingresar un número mayor o igual a 10.")
            return insertarNPart()
    except ValueError:
        print("El valor ingresado debe ser un número entero.")
        return ""

def enlazarAbuelos():
    indice = 0
    contador = 0
    abuelos = []
    voluntarios = []
    for i in matrizPart:
        if i[2][0] == "a":
            abuelos.append(i)
        else:
            voluntarios.append(i)
    porcAdultM = int(cantidadAdultM() * 0.7)
    for i in abuelos:
        if porcAdultM == contador:
            break
        if indice == len(voluntarios):
            indice = 0
        enlazados[i[2]] = voluntarios[indice][2]
        contador += 1
        indice += 1
    adoptadoTrue(enlazados)
    print(enlazados)
    return ""

def darDeBaja(codigo):
    indice = 0
    opcion = 0
    llaves = list(enlazados.keys())
    for i in llaves:
        if codigo == i:
            while opcion != 1 or opcion != 2:
                print("1 = Sí\n2 = No")
                opcion = int(input("¿Está seguro que desea darse de baja?: "))
                if opcion == 1:
                    modificaEstado(codigo)
                    adoptadoFalse(i)
                    del enlazados[llaves[indice]]
                    print(f"Su usuario: {llaves[indice]}, ha sido dado de baja exitosamente.")
                    return ""
                elif opcion == 2:
                    print("Se ha cancelado el proceso.\n¡Muchas gracias por mantenerse con nosotros!")
                    return ""
                else:
                    print("Debe ingresar una opción entre 1 y 2.")
        else:
            if codigo in enlazados[i]:
                while opcion != 1 or opcion != 2:
                    print("1 = Sí\n2 = No")
                    opcion = int(input("¿Está seguro que desea darse de baja?: "))
                    if opcion == 1:
                        modificaEstado(enlazados[i])
                        adoptadoFalse(i)
                        del enlazados[llaves[indice]]
                        print(f"Su usuario: {llaves[indice]}, ha sido dado de baja exitosamente.")
                        return ""
                    elif opcion == 2:
                        print("Se ha cancelado el proceso.\n¡Muchas gracias por mantenerse con nosotros!")
                        return ""
                    else:
                        print("Debe ingresar una opción entre 1 y 2.")
        indice += 1
    return ""

def enviarCorreo():
    parejas = list(enlazados.items())
    indice = random.randint(0, len(parejas) - 1)
    codigo = parejas[indice][0]
    for i in matrizPart:
        if i[2] == codigo:
            dirCorreo = i[6]
            break
    print(dirCorreo)
    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login("tprogdos@gmail.com", "tareaProgra2!")
        encabezado = "Prueba de envio de correo"
        mensaje = "Esto es una prueba para una tarea de programacion.\nDisculpe las molestias, ignorar mensaje por favor."
        correo = f"Subject: {encabezado}\n\n{mensaje}"
        smtp.sendmail("tprogdos@gmail.com", dirCorreo, correo) # Aqui se ingresa: emisor, receptor, mensaje. Para pruebas cambiar el receptor
    print("El correo se ha enviado satisfactoriamente.")       # a un correo personal
    return ""

def crearExcel(nombre, reporte):
    try:
        with open(nombre, "w", newline="")as f:
            for i in reporte:
                writer=csv.writer(f)
                writer.writerow(i)
    except:
        print("Error al leer archivo")
    return ""
def mostrarReporte1():
    lista=[]
    for i in matrizPart:
        lista.append(i)
    crearExcel("Reporte1.csv", lista)
    return ""
def mostrarReporte2():
    pruebaen=list(enlazados)
    listaPruebaTemp=matrizPart.copy()
    enlazar=[]
    print(pruebaen)
    for i in matrizPart:
        abu=[]
        for n in pruebaen:
            if i[2]==n:
                listaPruebaTemp.remove(i)  
                abu.append(listaPruebaTemp)
                enlazar.append(abu)        
    crearExcel("Reporte2.csv", enlazar)
    return ""

def mostrarReporte3():
    enlazar=[]
    for i in matrizPart:
        abu=[]
        for n in enlazados:
            if i[2]==n:
                abu.append(i[2])
                abu.append(i[3])
                enlazar.append(abu)
    for j in enlazados.values():
        for m in matrizPart:
            participante=[]
            if m[2]==j:
                participante.append(m[2])
                participante.append(m[3])
                enlazar.append(participante)
    crearExcel("Reporte3.csv", enlazar)
    return ""

def mostrarReporte4(hobbie):
    enlazar=[]
    for i in matrizPart:
        abu=[]
        if hobbie in i[4]:
            abu.append(i[4])
            abu.append(i[1])
            abu.append(i[3])
            abu.append(i[7])
            enlazar.append(abu)
    crearExcel("Reporte4.csv", enlazar)
    return ""

def mostrarReporte5():
    enlazar=[]
    abu=[]
    for i in matrizPart:
        if i[8][0]!=1:
            abu.append(i)
            enlazar.append(abu)
        crearExcel("Reporte5.csv", enlazar)
    return ""

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
    
    def cambiosFecha():
        identificador = ""
        num = ""
        for i in range(5):
            num += str(random.randint(0, 9))
        fechaN = entradaFechaN.get()
        if validarFechaN(fechaN) == False:
            pIngresarPart.deiconify()
            errorFecha = Toplevel()
            errorFecha.geometry("450x180")
            errorFecha.config(cursor = "star")
            Label(errorFecha, text = "Debe ingresar una fecha de nacimiento", font = ("Helvetica", 15), fg = "Black").place(x = 23, y = 20)
            Label(errorFecha, text = "con el formato: (##/##/####)", font = ("Helvetica", 15), fg = "Black").place(x = 23, y = 50)
            Label(errorFecha, text = "Por favor inténtelo de nuevo.", font = ("Helvetica", 15), fg = "Black").place(x = 23, y = 80)
            botonRegresar = Button(errorFecha, text = "Regresar", padx = 30, pady = 5, font = ("Impact", 12), relief = "raised", fg = "White", bg = "Black", command = lambda: cerrarPantalla(errorFecha))
            botonRegresar.place(x = 300, y = 120)
            return ""
        edad = 2022 - int(fechaN[6:])
        if 17 <= edad <= 25:
            radioVar.set(2)
            identificador = "v"+num
            entradaIdenPart.config(text = identificador)
            return ""
        elif 55 <= edad <= 121:
            radioVar.set(1)
            identificador = "am"+num
            entradaIdenPart.config(text = identificador)
            return ""
        else:
            pIngresarPart.deiconify()
            fechaInval = Toplevel()
            fechaInval.geometry("400x215")
            fechaInval.config(cursor = "star")
            Label(fechaInval, text = "Debe ingresar un participante entre las", font = ("Helvetica", 15), fg = "Black").place(x = 23, y = 20)
            Label(fechaInval, text = "edades de 17 y 25 si es un voluntario", font = ("Helvetica", 15), fg = "Black").place(x = 23, y = 50)
            Label(fechaInval, text = "y entre 55 y 121 si es un adulto mayor.", font = ("Helvetica", 15), fg = "Black").place(x = 23, y = 80)
            Label(fechaInval, text = "Por favor inténtelo de nuevo.", font = ("Helvetica", 15), fg = "Black").place(x = 23, y = 110)
            botonRegresar = Button(fechaInval, text = "Regresar", padx = 30, pady = 5, font = ("Impact", 12), relief = "raised", fg = "White", bg = "Black", command = lambda: cerrarPantalla(fechaInval))
            botonRegresar.place(x = 250, y = 155)
            return ""
    
    def cambiosNombre():
        nombreC = entradaNombreC.get()
        nombreC = nombreC.split(" ")
        if len(nombreC) != 3:
            pIngresarPart.deiconify()
            errorNombre = Toplevel()
            errorNombre.geometry("450x180")
            errorNombre.config(cursor = "star")
            Label(errorNombre, text = "Debe ingresar un nombre y dos apellidos", font = ("Helvetica", 15), fg = "Black").place(x = 23, y = 20)
            Label(errorNombre, text = "separados por espacios.", font = ("Helvetica", 15), fg = "Black").place(x = 23, y = 50)
            Label(errorNombre, text = "Por favor inténtelo de nuevo.", font = ("Helvetica", 15), fg = "Black").place(x = 23, y = 80)
            botonRegresar = Button(errorNombre, text = "Regresar", padx = 30, pady = 5, font = ("Impact", 12), relief = "raised", fg = "White", bg = "Black", command = lambda: cerrarPantalla(errorNombre))
            botonRegresar.place(x = 300, y = 120)
            return ""
        n = nombreC[0]
        ap1 = nombreC[-2]
        ap2 = nombreC[-1]
        if ingresarNombre(n,ap1,ap2) == 0:
            pIngresarPart.deiconify()
            errorNombre = Toplevel()
            errorNombre.geometry("450x180")
            errorNombre.config(cursor = "star")
            Label(errorNombre, text = "Debe ingresar un nombre que comience con", font = ("Helvetica", 15), fg = "Black").place(x = 23, y = 20)
            Label(errorNombre, text = "mayúscula y de dos o más caracteres de largo.", font = ("Helvetica", 15), fg = "Black").place(x = 23, y = 50)
            Label(errorNombre, text = "Por favor inténtelo de nuevo.", font = ("Helvetica", 15), fg = "Black").place(x = 23, y = 80)
            botonRegresar = Button(errorNombre, text = "Regresar", padx = 30, pady = 5, font = ("Impact", 12), relief = "raised", fg = "White", bg = "Black", command = lambda: cerrarPantalla(errorNombre))
            botonRegresar.place(x = 300, y = 120)
            return ""
        elif ingresarNombre(n,ap1,ap2) == 1:
            pIngresarPart.deiconify()
            errorNombre = Toplevel()
            errorNombre.geometry("450x180")
            errorNombre.config(cursor = "star")
            Label(errorNombre, text = "Debe ingresar un apellido que comience con", font = ("Helvetica", 15), fg = "Black").place(x = 23, y = 20)
            Label(errorNombre, text = "mayúscula y de dos o más caracteres de largo.", font = ("Helvetica", 15), fg = "Black").place(x = 23, y = 50)
            Label(errorNombre, text = "Por favor inténtelo de nuevo.", font = ("Helvetica", 15), fg = "Black").place(x = 23, y = 80)
            botonRegresar = Button(errorNombre, text = "Regresar", padx = 30, pady = 5, font = ("Impact", 12), relief = "raised", fg = "White", bg = "Black", command = lambda: cerrarPantalla(errorNombre))
            botonRegresar.place(x = 300, y = 120)
            return ""

        num2 = ""
        num1 = random.randint(0, 9)
        for i in range(2):
            num2 += str(random.randint(0, 9))
        ocupacion = f"{num1}, {int(num2)}"
        entradaOcupacion.config(text = ocupacion)
        
        correo = ""
        nombre = n.lower()
        apellido = ap1.lower()
        correo = str(nombre[0])+str(apellido)+"@gmail.com"
        entradaCorreo.config(text = correo)
        
        origen = ()
        llaves = list(diccPaises.keys())
        indiceRegion = random.randint(0, len(llaves) - 1)
        region = str(llaves[indiceRegion])
        valores = list(diccPaises.get(region))
        indicePais = random.randint(0, len(valores) - 1)
        pais = str(valores[indicePais])
        origen = f"{region}, {pais}"
        entradaPais.config(text = origen)

        entradaEstado.config(text = "Activo")
        return ""
    
    def cambiosHobbies():
        def errorHobbies():
            pIngresarPart.deiconify()
            errorHobbies = Toplevel()
            errorHobbies.geometry("472x180")
            errorHobbies.config(cursor = "star")
            Label(errorHobbies, text = "Debe ingresar un valor númerico entre 1 y 3 que", font = ("Helvetica", 15), fg = "Black").place(x = 23, y = 20)
            Label(errorHobbies, text = "represente la cantidad de hobbies que practica.", font = ("Helvetica", 15), fg = "Black").place(x = 23, y = 50)
            Label(errorHobbies, text = "Por favor inténtelo de nuevo.", font = ("Helvetica", 15), fg = "Black").place(x = 23, y = 80)
            botonRegresar = Button(errorHobbies, text = "Regresar", padx = 30, pady = 5, font = ("Impact", 12), relief = "raised", fg = "White", bg = "Black", command = lambda: cerrarPantalla(errorHobbies))
            botonRegresar.place(x = 300, y = 120)
            return ""
        try:
            hobbies = int(entradaHobbies.get())
            if hobbies > 0 and hobbies < 4:
                return ""
            else:
                errorHobbies()
        except:
            errorHobbies()

    def insertarP():
        try:
            fechaN = entradaFechaN.get()
            nombreC = entradaNombreC.get()
            nombreC = nombreC.split(" ")
            n = nombreC[0]
            ap1 = nombreC[-2]
            ap2 = nombreC[-1]
            cantidad = int(entradaHobbies.get())
            descripcion = entradaDescripcion.get("1.0","end-1c")
            insertarPart(fechaN, n, ap1, ap2, cantidad, descripcion)
            pIngresarPart.deiconify()
            exitoInsPart = Toplevel()
            exitoInsPart.geometry("450x180")
            exitoInsPart.config(cursor = "star")
            Label(exitoInsPart, text = "Se ha ingresado exitosamente", font = ("Helvetica", 15), fg = "Black").place(x = 23, y = 20)
            Label(exitoInsPart, text = "como un participante.", font = ("Helvetica", 15), fg = "Black").place(x = 23, y = 50)
            Label(exitoInsPart, text = "¡Muchas gracias!", font = ("Helvetica", 15), fg = "Black").place(x = 23, y = 80)
            botonRegresar = Button(exitoInsPart, text = "Regresar", padx = 30, pady = 5, font = ("Impact", 12), relief = "raised", fg = "White", bg = "Black", command = lambda: cerrarPantalla(exitoInsPart))
            botonRegresar.place(x = 300, y = 120)
            return ""
        except:
            pIngresarPart.deiconify()
            errorInsertarP = Toplevel()
            errorInsertarP.geometry("450x180")
            errorInsertarP.config(cursor = "star")
            Label(errorInsertarP, text = "Todos los campos deben estar llenos", font = ("Helvetica", 15), fg = "Black").place(x = 23, y = 20)
            Label(errorInsertarP, text = "para poder insertarse como participante.", font = ("Helvetica", 15), fg = "Black").place(x = 23, y = 50)
            Label(errorInsertarP, text = "Por favor inténtelo de nuevo.", font = ("Helvetica", 15), fg = "Black").place(x = 23, y = 80)
            botonRegresar = Button(errorInsertarP, text = "Regresar", padx = 30, pady = 5, font = ("Impact", 12), relief = "raised", fg = "White", bg = "Black", command = lambda: cerrarPantalla(errorInsertarP))
            botonRegresar.place(x = 300, y = 120)
            return ""
        
    def limpiar():
        entradaFechaN.delete(0, END)
        radioVar.set(0)
        entradaIdenPart.config(text = "")
        entradaNombreC.delete(0, END)
        entradaHobbies.delete(0, END)
        entradaOcupacion.config(text = "")
        entradaCorreo.config(text = "")
        entradaPais.config(text = "")
        entradaEstado.config(text = "")
        entradaDescripcion.delete("1.0","end-1c")
    
    Label(pIngresarPart, text = "Insertar un participante", font = ("Impact", 25), fg = "Black").place(x = 30, y = 30)

    Label(pIngresarPart, text = "Fecha de nacimiento", font = ("Helvetica", 14), fg = "Black").place(x = 30, y = 110)
    entradaFechaN = Entry(pIngresarPart, width = 23, font = ("Helvetica", 14), relief = "raised", bg = "Orange")
    entradaFechaN.place(x = 300, y = 115)
    entradaFechaN.config(justify = "center")

    botonAgregar1 = Button(pIngresarPart, padx = 5, pady = 0, relief = "raised", bg = "teal", command = cambiosFecha)
    botonAgregar1.place(x = 275, y = 116)
    
    radioVar = IntVar()
    Label(pIngresarPart, text = "Tipo de participante", font = ("Helvetica", 14), fg = "Black").place(x = 30, y = 155)
    radioBAdultoMayor = Radiobutton(pIngresarPart, text = "Adulto Mayor", font = ("Helvetica", 12), variable = radioVar, value = 1)
    radioBVoluntario = Radiobutton(pIngresarPart, text = "Voluntario", font = ("Helvetica", 12), variable = radioVar, value = 2)
    radioBAdultoMayor.place(x = 300, y = 160)
    radioBVoluntario.place(x = 300, y = 200)

    Label(pIngresarPart, text = "Identificador de participante", font = ("Helvetica", 14), fg = "Black").place(x = 30, y = 240)
    entradaIdenPart = Label(pIngresarPart, width = 23, text = "", font = ("Helvetica", 14), relief = "raised", bg = "Orange")
    entradaIdenPart.place(x = 300, y = 245)

    Label(pIngresarPart, text = "Nombre completo", font = ("Helvetica", 14), fg = "Black").place(x = 30, y = 285)
    entradaNombreC = Entry(pIngresarPart, width = 23, font = ("Helvetica", 14), relief = "raised", bg = "Orange")
    entradaNombreC.place(x = 300, y = 290)
    entradaNombreC.config(justify = "center")

    botonAgregar2 = Button(pIngresarPart, padx = 5, pady = 0, relief = "raised", bg = "teal", command = cambiosNombre)
    botonAgregar2.place(x = 275, y = 291)

    Label(pIngresarPart, text = "Hobbies", font = ("Helvetica", 14), fg = "Black").place(x = 30, y = 330)
    entradaHobbies = Entry(pIngresarPart, width = 23, font = ("Helvetica", 14), relief = "raised", bg = "Orange")
    entradaHobbies.place(x = 300, y = 335)
    entradaHobbies.config(justify = "center")

    botonAgregar3 = Button(pIngresarPart, padx = 5, pady = 0, relief = "raised", bg = "teal", command = cambiosHobbies)
    botonAgregar3.place(x = 275, y = 336)

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

    botonIngresar = Button(pIngresarPart, text = "Ingresar", padx = 30, pady = 5, font = ("Impact", 13), relief = "raised", fg = "White", bg = "Black", command = insertarP)
    botonIngresar.place(x = 63, y = 677)

    botonLimpiar = Button(pIngresarPart, text = "Limpiar", padx = 30, pady = 5, font = ("Impact", 13), relief = "raised", fg = "White", bg = "Black", command = limpiar)
    botonLimpiar.place(x = 233, y = 677)

    botonRegresar = Button(pIngresarPart, text = "Regresar", padx = 30, pady = 5, font = ("Impact", 13), relief = "raised", fg = "White", bg = "Black", command = lambda: cerrarPantalla(pIngresarPart))
    botonRegresar.place(x = 400, y = 677)

# Interfaz ingresar n participantes
def guiInsertarNPart():
    raiz.deiconify()
    pIngresarNPart = Toplevel()
    pIngresarNPart.geometry("500x250")
    pIngresarNPart.config(cursor = "star")

    def insertarNP():
        try:
            cantidad = int(entradaCantidad.get())
            if cantidad > 9:
                insertarNPart(cantidad)
                pIngresarNPart.deiconify()
                exitoInsNPart = Toplevel()
                exitoInsNPart.geometry("450x180")
                exitoInsNPart.config(cursor = "star")
                Label(exitoInsNPart, text = "Se han ingresado exitosamente", font = ("Helvetica", 15), fg = "Black").place(x = 23, y = 20)
                Label(exitoInsNPart, text = f"{cantidad} participantes.", font = ("Helvetica", 15), fg = "Black").place(x = 23, y = 50)
                Label(exitoInsNPart, text = "¡Muchas gracias!", font = ("Helvetica", 15), fg = "Black").place(x = 23, y = 80)
                botonRegresar = Button(exitoInsNPart, text = "Regresar", padx = 30, pady = 5, font = ("Impact", 12), relief = "raised", fg = "White", bg = "Black", command = lambda: cerrarPantalla(exitoInsNPart))
                botonRegresar.place(x = 300, y = 120)
                return ""
            else:
                pIngresarNPart.deiconify()
                errorInsertarNP = Toplevel()
                errorInsertarNP.geometry("450x180")
                errorInsertarNP.config(cursor = "star")
                Label(errorInsertarNP, text = "Debe ingresar un número de", font = ("Helvetica", 15), fg = "Black").place(x = 23, y = 20)
                Label(errorInsertarNP, text = "participantes mayor a 10.", font = ("Helvetica", 15), fg = "Black").place(x = 23, y = 50)
                Label(errorInsertarNP, text = "Por favor inténtelo de nuevo.", font = ("Helvetica", 15), fg = "Black").place(x = 23, y = 80)
                botonRegresar = Button(errorInsertarNP, text = "Regresar", padx = 30, pady = 5, font = ("Impact", 12), relief = "raised", fg = "White", bg = "Black", command = lambda: cerrarPantalla(errorInsertarNP))
                botonRegresar.place(x = 300, y = 120)
        except:
            pIngresarNPart.deiconify()
            errorInsertarNP = Toplevel()
            errorInsertarNP.geometry("505x180")
            errorInsertarNP.config(cursor = "star")
            Label(errorInsertarNP, text = "Debe haber llenado el campo requerido con un valor", font = ("Helvetica", 15), fg = "Black").place(x = 23, y = 20)
            Label(errorInsertarNP, text = "numérico para poder insertar a sus participantes.", font = ("Helvetica", 15), fg = "Black").place(x = 23, y = 50)
            Label(errorInsertarNP, text = "Por favor inténtelo de nuevo.", font = ("Helvetica", 15), fg = "Black").place(x = 23, y = 80)
            botonRegresar = Button(errorInsertarNP, text = "Regresar", padx = 30, pady = 5, font = ("Impact", 12), relief = "raised", fg = "White", bg = "Black", command = lambda: cerrarPantalla(errorInsertarNP))
            botonRegresar.place(x = 350, y = 120)
            return ""

    def limpiar():
        entradaCantidad.delete(0, END)
        return ""

    Label(pIngresarNPart, text = "Insertar n participantes", font = ("Impact", 25), fg = "Black").place(x = 20, y = 30)

    Label(pIngresarNPart, text = "Cantidad a generar", font = ("Helvetica", 14), fg = "Black").place(x = 20, y = 100)
    entradaCantidad = Entry(pIngresarNPart, width = 20, font = ("Helvetica", 14), relief = "raised", bg = "Orange")
    entradaCantidad.place(x = 230, y = 105)

    botonIngresar = Button(pIngresarNPart, text = "Ingresar", padx = 30, pady = 5, font = ("Impact", 13), relief = "raised", fg = "White", bg = "Black", command = insertarNP)
    botonIngresar.place(x = 20, y = 180)

    botonLimpiar = Button(pIngresarNPart, text = "Limpiar", padx = 30, pady = 5, font = ("Impact", 13), relief = "raised", fg = "White", bg = "Black", command = limpiar)
    botonLimpiar.place(x = 180, y = 180)

    botonRegresar = Button(pIngresarNPart, text = "Regresar", padx = 30, pady = 5, font = ("Impact", 13), relief = "raised", fg = "White", bg = "Black", command = lambda: cerrarPantalla(pIngresarNPart))
    botonRegresar.place(x = 340, y = 180)

# Interfaz enlazar con abuelos
def guiEnlazarConAbu():
    enlazarAbuelos()
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

    def darDeBaja(codigo):
        def guiOpcion():
            def guiJustif():
                cerrarPantalla(opcion)
                def exito():
                    justificacion = entradaJust.get()
                    cerrarPantalla(modEst)
                    def modEstado(pcodigo, justificacion):
                        estado = ()
                        valor = 0
                        for i in matrizPart:
                            if i[2] == pcodigo:
                                valor = 0
                                estado = (valor, justificacion)
                                i[8] = estado
                                break
                        return matrizPart
                    modEstado(codigo, justificacion)
                    adoptadoFalse(i)
                    del enlazados[llaves[indice]]
                    pDarDeBaja.deiconify()
                    pExito = Toplevel()
                    pExito.geometry("450x180")
                    pExito.config(cursor = "star")
                    Label(pExito, text = f"Su usuario: {llaves[indice]},", font = ("Helvetica", 15), fg = "Black").place(x = 23, y = 20)
                    Label(pExito, text = "ha sido dado de baja exitosamente.", font = ("Helvetica", 15), fg = "Black").place(x = 23, y = 50)
                    botonRegresar = Button(pExito, text = "Regresar", padx = 30, pady = 5, font = ("Impact", 12), relief = "raised", fg = "White", bg = "Black", command = lambda: cerrarPantalla(pExito))
                    botonRegresar.place(x = 300, y = 120)
                    return ""

                pDarDeBaja.deiconify()
                modEst = Toplevel()
                modEst.geometry("377x190")
                modEst.config(cursor = "star")
                Label(modEst, text = "Por favor indique la razón", font = ("Helvetica", 15), fg = "Black").place(x = 23, y = 20)
                Label(modEst, text = "por la que se retira de la comunidad:", font = ("Helvetica", 15), fg = "Black").place(x = 23, y = 50)
                entradaJust = Entry(modEst, width = 24, font = ("Helvetica", 15), relief = "raised", bg = "Orange")
                entradaJust.place(x = 55, y = 90)
                botonAceptar = Button(modEst, text = "Ingresar", padx = 20, pady = 5, font = ("Impact", 12), relief = "raised", fg = "White", bg = "Black", command = exito)
                botonAceptar.place(x = 55, y = 130)
                botonRegresar = Button(modEst, text = "Regresar", padx = 20, pady = 5, font = ("Impact", 12), relief = "raised", fg = "White", bg = "Black", command = lambda: cerrarPantalla(modEst))
                botonRegresar.place(x = 210, y = 130)
                return ""

            def cancela():
                cerrarPantalla(opcion)
                pDarDeBaja.deiconify()
                pCancela = Toplevel()
                pCancela.geometry("465x180")
                pCancela.config(cursor = "star")
                Label(pCancela, text = "Se ha cancelado el proceso.", font = ("Helvetica", 15), fg = "Black").place(x = 23, y = 20)
                Label(pCancela, text = "¡Muchas gracias por mantenerse con nosotros!", font = ("Helvetica", 15), fg = "Black").place(x = 23, y = 50)
                botonRegresar = Button(pCancela, text = "Regresar", padx = 30, pady = 5, font = ("Impact", 12), relief = "raised", fg = "White", bg = "Black", command = lambda: cerrarPantalla(pCancela))
                botonRegresar.place(x = 300, y = 120)
                return ""

            pDarDeBaja.deiconify()
            opcion = Toplevel()
            opcion.geometry("450x130")
            opcion.config(cursor = "star")
            Label(opcion, text = "¿Está seguro que desea darse de baja?", font = ("Helvetica", 15), fg = "Black").place(x = 23, y = 20)
            botonSi = Button(opcion, text = "Sí", padx = 30, pady = 5, font = ("Impact", 12), relief = "raised", fg = "White", bg = "Black", command = guiJustif)
            botonSi.place(x = 100, y = 70)
            botonNo = Button(opcion, text = "No", padx = 30, pady = 5, font = ("Impact", 12), relief = "raised", fg = "White", bg = "Black", command = cancela)
            botonNo.place(x = 270, y = 70)
        
        def guiOpcion2():
            def guiJustif2():
                cerrarPantalla(opcion)
                def exito2():
                    justificacion = entradaJust.get()
                    cerrarPantalla(modEst)
                    def modEstado2(pcodigo, justificacion):
                        estado = ()
                        valor = 0
                        for i in matrizPart:
                            if i[2] == pcodigo:
                                valor = 0
                                estado = (valor, justificacion)
                                i[8] = estado
                                break
                        return matrizPart
                    modEstado2(codigo, justificacion)
                    adoptadoFalse(i)
                    del enlazados[llaves[indice]]
                    pDarDeBaja.deiconify()
                    pExito = Toplevel()
                    pExito.geometry("450x180")
                    pExito.config(cursor = "star")
                    Label(pExito, text = f"Su usuario: {llaves[indice]},", font = ("Helvetica", 15), fg = "Black").place(x = 23, y = 20)
                    Label(pExito, text = "ha sido dado de baja exitosamente.", font = ("Helvetica", 15), fg = "Black").place(x = 23, y = 50)
                    botonRegresar = Button(pExito, text = "Regresar", padx = 30, pady = 5, font = ("Impact", 12), relief = "raised", fg = "White", bg = "Black", command = lambda: cerrarPantalla(pExito))
                    botonRegresar.place(x = 300, y = 120)
                    return ""

                pDarDeBaja.deiconify()
                modEst = Toplevel()
                modEst.geometry("377x190")
                modEst.config(cursor = "star")
                Label(modEst, text = "Por favor indique la razón", font = ("Helvetica", 15), fg = "Black").place(x = 23, y = 20)
                Label(modEst, text = "por la que se retira de la comunidad:", font = ("Helvetica", 15), fg = "Black").place(x = 23, y = 50)
                entradaJust = Entry(modEst, width = 24, font = ("Helvetica", 15), relief = "raised", bg = "Orange")
                entradaJust.place(x = 55, y = 90)
                botonAceptar = Button(modEst, text = "Ingresar", padx = 20, pady = 5, font = ("Impact", 12), relief = "raised", fg = "White", bg = "Black", command = exito2)
                botonAceptar.place(x = 55, y = 130)
                botonRegresar = Button(modEst, text = "Regresar", padx = 20, pady = 5, font = ("Impact", 12), relief = "raised", fg = "White", bg = "Black", command = lambda: cerrarPantalla(modEst))
                botonRegresar.place(x = 210, y = 130)
                return ""

            def cancela2():
                cerrarPantalla(opcion)
                pDarDeBaja.deiconify()
                pCancela2 = Toplevel()
                pCancela2.geometry("465x180")
                pCancela2.config(cursor = "star")
                Label(pCancela2, text = "Se ha cancelado el proceso.", font = ("Helvetica", 15), fg = "Black").place(x = 23, y = 20)
                Label(pCancela2, text = "¡Muchas gracias por mantenerse con nosotros!", font = ("Helvetica", 15), fg = "Black").place(x = 23, y = 50)
                botonRegresar = Button(pCancela2, text = "Regresar", padx = 30, pady = 5, font = ("Impact", 12), relief = "raised", fg = "White", bg = "Black", command = lambda: cerrarPantalla(pCancela2))
                botonRegresar.place(x = 300, y = 120)
                return ""

            pDarDeBaja.deiconify()
            opcion = Toplevel()
            opcion.geometry("450x130")
            opcion.config(cursor = "star")
            Label(opcion, text = "¿Está seguro que desea darse de baja?", font = ("Helvetica", 15), fg = "Black").place(x = 23, y = 20)
            botonSi = Button(opcion, text = "Sí", padx = 30, pady = 5, font = ("Impact", 12), relief = "raised", fg = "White", bg = "Black", command = guiJustif2)
            botonSi.place(x = 100, y = 70)
            botonNo = Button(opcion, text = "No", padx = 30, pady = 5, font = ("Impact", 12), relief = "raised", fg = "White", bg = "Black", command = cancela2)
            botonNo.place(x = 270, y = 70)

        indice = 0
        llaves = list(enlazados.keys())
        for i in llaves:
            if codigo == i:
                guiOpcion()
                return ""
            else:
                if codigo in enlazados[i]:
                    guiOpcion2()
                    return ""
            indice += 1
        return ""

    def darBaja():
        codigo = entradaCodigo.get()
        if validarCodigo(codigo) == False:
            pDarDeBaja.deiconify()
            errorCod = Toplevel()
            errorCod.geometry("552x180")
            errorCod.config(cursor = "star")
            Label(errorCod, text = "Debe ingresar un código con el formato:", font = ("Helvetica", 15), fg = "Black").place(x = 23, y = 20)
            Label(errorCod, text = "v##### (para voluntario) o am##### (para adulto mayor).", font = ("Helvetica", 15), fg = "Black").place(x = 23, y = 50)
            Label(errorCod, text = "Por favor inténtelo de nuevo.", font = ("Helvetica", 15), fg = "Black").place(x = 23, y = 80)
            botonRegresar = Button(errorCod, text = "Regresar", padx = 30, pady = 5, font = ("Impact", 12), relief = "raised", fg = "White", bg = "Black", command = lambda: cerrarPantalla(errorCod))
            botonRegresar.place(x = 400, y = 120)
            return ""
        if existeEnBd(codigo) == False:
            pDarDeBaja.deiconify()
            errorCod = Toplevel()
            errorCod.geometry("375x180")
            errorCod.config(cursor = "star")
            Label(errorCod, text = "El código ingresado no se", font = ("Helvetica", 15), fg = "Black").place(x = 23, y = 20)
            Label(errorCod, text = "encuentra en nuestra base de datos.", font = ("Helvetica", 15), fg = "Black").place(x = 23, y = 50)
            Label(errorCod, text = "Por favor inténtelo de nuevo.", font = ("Helvetica", 15), fg = "Black").place(x = 23, y = 80)
            botonRegresar = Button(errorCod, text = "Regresar", padx = 30, pady = 5, font = ("Impact", 12), relief = "raised", fg = "White", bg = "Black", command = lambda: cerrarPantalla(errorCod))
            botonRegresar.place(x = 225, y = 120)
            return ""
        darDeBaja(codigo)
        return ""
    
    def limpiar():
        entradaCodigo.delete(0, END)
        return ""

    Label(pDarDeBaja, text = "Dar de baja", font = ("Impact", 25), fg = "Black").place(x = 20, y = 30)

    Label(pDarDeBaja, text = "Código de participante", font = ("Helvetica", 14), fg = "Black").place(x = 20, y = 100)
    entradaCodigo = Entry(pDarDeBaja, width = 20, font = ("Helvetica", 14), relief = "raised", bg = "Orange")
    entradaCodigo.place(x = 230, y = 105)

    botonBaja = Button(pDarDeBaja, text = "Baja", padx = 40, pady = 5, font = ("Impact", 13), relief = "raised", fg = "White", bg = "Black", command = darBaja)
    botonBaja.place(x = 20, y = 180)

    botonLimpiar = Button(pDarDeBaja, text = "Limpiar", padx = 30, pady = 5, font = ("Impact", 13), relief = "raised", fg = "White", bg = "Black", command = limpiar)
    botonLimpiar.place(x = 180, y = 180)

    botonRegresar = Button(pDarDeBaja, text = "Regresar", padx = 30, pady = 5, font = ("Impact", 13), relief = "raised", fg = "White", bg = "Black", command = lambda: cerrarPantalla(pDarDeBaja))
    botonRegresar.place(x = 340, y = 180)

# Interfaz escribe una carta a su correo
def guiEnviarCorreo():
    enviarCorreo()
    raiz.deiconify()
    pEnviarCorreo = Toplevel()
    pEnviarCorreo.geometry("280x180")
    pEnviarCorreo.config(cursor = "star")
    
    Label(pEnviarCorreo, text = "Correo enviado", font = ("Impact", 20), fg = "Black").place(x = 23, y = 20)
    Label(pEnviarCorreo, text = "satisfactoriamente", font = ("Impact", 20), fg = "Black").place(x = 23, y = 50)

    botonRegresar = Button(pEnviarCorreo, text = "Regresar", padx = 30, pady = 5, font = ("Impact", 12), relief = "raised", fg = "White", bg = "Black", command = lambda: cerrarPantalla(pEnviarCorreo))
    botonRegresar.place(x = 75, y = 115)

def guiReportes():
    raiz.deiconify()
    reportes = Toplevel()
    reportes.geometry("592x590")
    reportes.config(cursor = "star")
    def obtieneHobbieRep():
        reportes.deiconify()
        pHobbies = Toplevel()
        pHobbies.geometry("600x310")
        pHobbies.config(cursor = "star")

        #Variable global
        hobbies = []

        # Funcion para obtener el valor de la caja seleccionada
        def mostrarInfo():
            for i in range(len(hobbies)):
                seleccionado=""
                if hobbies[i].get()>=1:
                    seleccionado += str(i + 1)
                    mostrarReporte4(f"hobbie{seleccionado}")

        # Añade un valor para cada opcion
        for i in range(25):
            opcion = IntVar()
            opcion.set(0)
            hobbies.append(opcion)

        # Las cajas de seleccion, una para cada hobbie
        Label(pHobbies, text = "Elija los hobbies para los cuales desea un reporte:", font = ("Impact", 18), fg = "Black").place(x = 50, y = 30)

        Checkbutton(pHobbies, text= "Hobbie 1", variable=hobbies[0]).place(x = 50, y = 90)

        Checkbutton(pHobbies, text= "Hobbie 2", variable=hobbies[1]).place(x = 50, y = 120)

        Checkbutton(pHobbies, text= "Hobbie 3", variable=hobbies[2]).place(x = 50, y = 150)

        Checkbutton(pHobbies, text= "Hobbie 4", variable=hobbies[3]).place(x = 50, y = 180)

        Checkbutton(pHobbies, text= "Hobbie 5", variable=hobbies[4]).place(x = 50, y = 210)

        Checkbutton(pHobbies, text= "Hobbie 6", variable=hobbies[5]).place(x = 150, y = 90)

        Checkbutton(pHobbies, text= "Hobbie 7", variable=hobbies[6]).place(x = 150, y = 120)

        Checkbutton(pHobbies, text= "Hobbie 8", variable=hobbies[7]).place(x = 150, y = 150)

        Checkbutton(pHobbies, text= "Hobbie 9", variable=hobbies[8]).place(x = 150, y = 180)

        Checkbutton(pHobbies, text= "Hobbie 10", variable=hobbies[9]).place(x = 150, y = 210)

        Checkbutton(pHobbies, text= "Hobbie 11", variable=hobbies[10]).place(x = 250, y = 90)

        Checkbutton(pHobbies, text= "Hobbie 12", variable=hobbies[11]).place(x = 250, y = 120)

        Checkbutton(pHobbies, text= "Hobbie 13", variable=hobbies[12]).place(x = 250, y = 150)

        Checkbutton(pHobbies, text= "Hobbie 14", variable=hobbies[13]).place(x = 250, y = 180)

        Checkbutton(pHobbies, text= "Hobbie 15", variable=hobbies[14]).place(x = 250, y = 210)

        Checkbutton(pHobbies, text= "Hobbie 16", variable=hobbies[15]).place(x = 350, y = 90)

        Checkbutton(pHobbies, text= "Hobbie 17", variable=hobbies[16]).place(x = 350, y = 120)

        Checkbutton(pHobbies, text= "Hobbie 18", variable=hobbies[17]).place(x = 350, y = 150)

        Checkbutton(pHobbies, text= "Hobbie 19", variable=hobbies[18]).place(x = 350, y = 180)

        Checkbutton(pHobbies, text= "Hobbie 20", variable=hobbies[19]).place(x = 350, y = 210)

        Checkbutton(pHobbies, text= "Hobbie 21", variable=hobbies[20]).place(x = 450, y = 90)

        Checkbutton(pHobbies, text= "Hobbie 22", variable=hobbies[21]).place(x = 450, y = 120)

        Checkbutton(pHobbies, text= "Hobbie 23", variable=hobbies[22]).place(x = 450, y = 150)

        Checkbutton(pHobbies, text= "Hobbie 24", variable=hobbies[23]).place(x = 450, y = 180)

        Checkbutton(pHobbies, text= "Hobbie 25", variable=hobbies[24]).place(x = 450, y = 210)

        # Buton para mostrar el hobbie seleccionado
        botonAceptar = Button(pHobbies, text="Aceptar", padx = 20, pady = 1, font = ("Impact", 10), relief = "raised", fg = "White", bg = "Black", command=mostrarInfo)
        botonAceptar.place(x = 450, y = 255)

        botonRegresar = Button(pHobbies, text="Regresar", padx = 20, pady = 1, font = ("Impact", 10), relief = "raised", fg = "White", bg = "Black", command = lambda: cerrarPantalla(pHobbies))
        botonRegresar.place(x = 330, y = 255)

    Label(reportes, text = "Reportes", font = ("Impact", 25), fg = "Black").place(x = 235, y = 40)

    botonRep1 = Button(reportes, text = "Mostrar la base de datos completa", padx = 102, pady = 5, font = "Impact", relief = "raised", fg = "White", bg = "Black", command = mostrarReporte1)
    botonRep1.place(x = 50, y = 130)

    botonRep2 = Button(reportes, text = "Lista de adultos mayores no adoptados", padx = 84, pady = 5, font = "Impact", relief = "raised", fg = "White", bg = "Black", command = mostrarReporte2)
    botonRep2.place(x = 50, y = 200)

    botonRep3 = Button(reportes, text = "Lista de voluntarios con los adultos mayores enlazados", padx = 20, pady = 5, font = "Impact", relief = "raised", fg = "White", bg = "Black", command = mostrarReporte3)
    botonRep3.place(x = 50, y = 270)

    botonRep4 = Button(reportes, text = "Participantes y rol según su hobby", padx = 103, pady = 5, font = "Impact", relief = "raised", fg = "White", bg = "Black", command = obtieneHobbieRep)
    botonRep4.place(x = 50, y = 340)

    botonRep5 = Button(reportes, text = "Participantes inactivos y su justificación", padx = 78, pady = 5, font = "Impact", relief = "raised", fg = "White", bg = "Black", command = mostrarReporte5)
    botonRep5.place(x = 50, y = 410)

    botonRegresar = Button(reportes, text = "Regresar", padx = 205, pady = 5, font = "Impact", relief = "raised", fg = "White", bg = "Black", command = lambda: cerrarPantalla(reportes))
    botonRegresar.place(x = 50, y = 480)
    return ""

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

botonReportes = Button(raiz, text = "Reportes", padx = 191, pady = 5, font = "Impact", relief = "raised", fg = "White", bg = "Black", command = guiReportes)
botonReportes.place(x = 65, y = 570)
botonReportes.config(state=DISABLED)

botonSalir = Button(raiz, text = "Salir", padx = 209, pady = 5, font = "Impact", relief = "raised", fg = "White", bg = "Black", command = lambda: cerrarPantalla(raiz))
botonSalir.place(x = 65, y = 640)

raiz.mainloop()