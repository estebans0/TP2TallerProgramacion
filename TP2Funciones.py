# Elaborado por: Juan Ceballos y Esteban Solano
# Fecha de Creación: 04/05/2022 04:53pm
# Fecha de última Modificación: XX/XX/2022 XX:XXxm
# Versión: 3.10.2

# Importación de librerías
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

#================================================================================================================================================#
#                                                           DEFINICIÓN DE FUNCIONES
#================================================================================================================================================#
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

def validarFechaN():
    pfecha= input("Según el formato (##/##/####), ingrese su fecha de nacimiento: ")
    if re.match("^\d{2}\/\d{2}\/\d{4}$", pfecha):
        return pfecha
    print("Debe ingresar una fecha de nacimiento con el formato (##/##/####). Por favor inténtelo de nuevo.\n")
    return validarFechaN()

def validarNombre(pnombre):
    if re.match("^[A-Z]{1}[a-z]{1,}", pnombre):
        return True
    return False

def ingresarNombre(n, ap1, ap2):
    n = input("Por favor ingrese su nombre: ")
    if validarNombre(n) == True:
        ap1 = input("Por favor ingrese su primer apellido: ")
        if validarNombre(ap1) == True:
            ap2 = input("Por favor ingrese su segundo apellido: ")
            if validarNombre(ap2) == True:
                return n, ap1, ap2
            else:
                print("Debe ingresar un apellido que comience con mayúscula y de dos o más caracteres de largo. Intente de nuevo.\n")
                return ingresarNombre(n, ap1, ap2)
        else:
            print("Debe ingresar un apellido que comience con mayúscula y de dos o más caracteres de largo. Intente de nuevo.\n")
            return ingresarNombre(n, ap1, ap2)
    else:
        print("Debe ingresar un nombre que comience con mayúscula y de dos o más caracteres de largo. Intente de nuevo.\n")
        return ingresarNombre(n, ap1, ap2)

def validarCantidadH(cantidad):
    cantidad = int(input("Ingrese la cantidad de hobbies que desea agregar (Entre 1 y 3): "))
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
        print("Debe ingresar un participante entre las edades de 17 y 25 si es un voluntario y entre 55 y 121 si es un adulto mayor. Por favor inténtelo de nuevo.\n")
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
        for j in range(2):
            num += str(random.randint(0, 9))
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
    """
    correo = ""
    nombre = pparticipante[3][0].lower()
    apellido = pparticipante[3][1].lower()
    correo = str(nombre[0])+str(apellido)+"@gmail.com"
    """
    correo = "estebanjs029@gmail.com"
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
    #botonIns1P.config(state=ACTIVE)
    #botonInsNP.config(state=ACTIVE)
    #botonEnlazarAbu.config(state=ACTIVE)
    #botonDarBaja.config(state=ACTIVE)
    #botonCorreo.config(state=ACTIVE)
    #botonReportes.config(state=ACTIVE)
    diccPaises
    with open("paises.txt") as file:
        for i in file:
            region, pais=i.strip("\n").split(":")
            pais=pais.split(",")
            diccPaises[region]=pais
    return diccPaises

def insertarPart():
    participante = []
    fechaN = validarFechaN()
    if agregarFechaNYTipoPart(participante, fechaN) == False:
        return insertarPart()
    identificarPart(participante)
    tuplaNombres = ingresarNombre("","","")
    agregarNombre(participante, tuplaNombres)
    cantidad = validarCantidadH(0)
    agregarHobbies(participante, cantidad)
    agregarOcupacion(participante)
    agregarCorreoE(participante)
    agregarPaisOrigen(participante)
    participante.append((1, ""))
    descripcion = input("Añada una descripción: ")
    agregarDescripcion(participante, descripcion)
    agregarAdoptado(participante)
    matrizPart.append(participante)
    return ""

def insertarNPart():
    try:
        num = int(input("Ingrese un número mayor o igual a 10 para generar sus participantes: "))
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
    return ""

def darDeBaja():
    indice = 0
    opcion = 0
    codigo = input("Ingrese su código de participante: ")
    if validarCodigo(codigo) == False:
        print("Debe ingresar un código con el formato: v##### (para voluntario) o am##### (para adulto mayor).\nIntente de nuevo.")
        return darDeBaja()
    if existeEnBd(codigo) == False:
        print("El código ingresado no se encuentra en nuestra base de datos. Intente de nuevo.")
        return ""
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
        smtp.sendmail("tprogdos@gmail.com", "estebanjs029@gmail.com", correo) # Aqui se ingresa: emisor, receptor, mensaje. Para pruebas cambiar el receptor
    print("El correo se ha enviado satisfactoriamente.")       # a un correo personal
    return ""

def mostrarReporte1():
    return ""

def mostrarReporte2():
    return ""

def mostrarReporte3():
    return ""

def mostrarReporte4():
    return ""

def mostrarReporte5():
    return ""

def reportes():
    try:
        opcion = 0
        print ("\n***********************************************************")
        print ("Reportes")
        print ("***********************************************************")
        opcion = int(input("1. Mostrar base de datos completa\n2. Lista de Adultos mayores no adoptados\n3. Lista de voluntarios con los adultos mayores enlazados\n4. Participantes y rol según un hobby\n5. Participantes inactivos y su justificación\n6. Regresar\nSeleccione una opción: "))
        if opcion == 1:
            print(f"\n{mostrarReporte1()}")
        elif opcion == 2:
            print(f"\n{mostrarReporte2()}")
        elif opcion == 3:
            print(f"\n{mostrarReporte3()}")
        elif opcion == 4:
            print(f"\n{mostrarReporte4()}")
        elif opcion == 5:
            print(f"\n{mostrarReporte5()}")
        elif opcion == 6:
            return 
        else:
            return f"\nDebe ingresar un valor númerico. {reportes()}"
        return ""
    except ValueError:
        print("Debe ingresar valores válidos.")

def menu():
    """
    Funcionamiento: De manera repetitiva, muestra el menú al usuario. 
    Entradas: NA
    Salidas: Resultado según lo solicitado
    """
    try:
        print ("####################################################################")
        print ("¡Tarea Programada 2: Adopta un abuelo!")
        print ("####################################################################")
        print ("1. Cargar BD de países")
        print ("2. Insertar participante")
        print ("3. Insertar n participantes")
        print ("4. Enlazar con abuelos")
        print ("5. Dar de baja")
        print ("6. Escribe una carta a su correo")
        print ("7. Reportes")
        print ("8. Salir")
        opcion = int(input ("Escoja una opción: "))
        if opcion >=1 and opcion <=8:
            if opcion == 1:
                cargarBdPaises() # FUNCIONA
            elif opcion == 2 :
                insertarPart() # FUNCIONA
            elif opcion == 3:
                insertarNPart() # FUNCIONA
            elif opcion == 4:
                enlazarAbuelos() # FUNCIONA
            elif opcion == 5:
                darDeBaja() # FUNCIONA
            elif opcion == 6 :
                enviarCorreo() # FUNCIONA
            elif opcion == 7:
                reportes() # EN PROCESO
            elif opcion == 8:
                print("\n¡Gracias por utilizar el sistema!")
                return
            else:
                return
        else:
            print ("\nOpción inválida, indique una opción según las opciones indicadas.\n")
        menu()
    except ValueError:
        print("\nOpción inválida, indique una opción según las opciones indicadas.\n")
        menu()
"""
menu()
"""