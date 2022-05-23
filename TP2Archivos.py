# Elaborado por: Juan Ceballos y Esteban Solano
# Fecha de Creación: 04/05/2022 04:53pm
# Fecha de última Modificación: XX/XX/2022 XX:XXxm
# Versión: 3.10.2

# Importación de librerías
import pickle

def graba(nomArchGrabar,lista): #Función que graba un archivo
    try:
        f=open(nomArchGrabar,"wb")
        pickle.dump(lista,f)
        f.close()
    except:
        print("Error al grabar el archivo: ", nomArchGrabar)

def lee (nomArchLeer): #Función que lee un archivo
    lista=[]
    try:
        f=open(nomArchLeer,"rb")
        lista = pickle.load(f)
        f.close()
    except:
        print("Error al leer el archivo: ", nomArchLeer)
    return lista