# Elaborado por: Juan Ceballos y Esteban Solano
# Fecha de Creación: 04/05/2022 04:53pm
# Fecha de última Modificación: XX/XX/2022 XX:XXxm
# Versión: 3.10.2

# Importación de librerías
from TP2Funciones import *
from tkinter import *

#Defincioin de Funciones
def cerrarApp(): # Función del botón "Salir" de la pantalla inicial
    raiz.destroy()

# Definición de validaciones


# Programa Principal
raiz = Tk()

# Configuración de la raiz
raiz.title("Adoptemos un Adulto Mayor")
raiz.geometry("600x750")
raiz.config(cursor = "star")

# Menú principal
Label(raiz, text = "Adoptemos un Adulto Mayor", font = ("Impact", 25), fg = "Black").place(x = 115, y = 50) # Titulo de la App

# Botones del menú inicial
botonBDPaises = Button(raiz, text = "Cargar BD de países", padx = 150, pady = 5, font = "Impact", relief = "raised", fg = "White", bg = "Black")
botonBDPaises.place(x = 65, y = 150)

botonIns1P = Button(raiz, text = "Insertar un participante", padx = 135, pady = 5, font = "Impact", relief = "raised", fg = "White", bg = "Black")
botonIns1P.place(x = 65, y = 220)

botonInsNP = Button(raiz, text = "Insertar n participantes", padx = 135, pady = 5, font = "Impact", relief = "raised", fg = "White", bg = "Black")
botonInsNP.place(x = 65, y = 290)

botonEnlazarAbu = Button(raiz, text = "Enlazar con abuelos", padx = 151, pady = 5, font = "Impact", relief = "raised", fg = "White", bg = "Black")
botonEnlazarAbu.place(x = 65, y = 360)

botonDarBaja = Button(raiz, text = "Dar de baja", padx = 185, pady = 5, font = "Impact", relief = "raised", fg = "White", bg = "Black")
botonDarBaja.place(x = 65, y = 430)

botonCorreo = Button(raiz, text = "Escribe una carta a su correo", padx = 113, pady = 5, font = "Impact", relief = "raised", fg = "White", bg = "Black")
botonCorreo.place(x = 65, y = 500)

botonReportes = Button(raiz, text = "Reportes", padx = 194, pady = 5, font = "Impact", relief = "raised", fg = "White", bg = "Black")
botonReportes.place(x = 65, y = 570)

botonSalir = Button(raiz, text = "Salir", padx = 212, pady = 5, font = "Impact", relief = "raised", fg = "White", bg = "Black", command = cerrarApp)
botonSalir.place(x = 65, y = 640)

raiz.mainloop()