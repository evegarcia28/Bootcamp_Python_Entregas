"""
Diseñe un programa en Python que agregue el siguiente contenido al archivo: informacion.dat. 
Este en una nueva línea en el archivo 
agregando la segunda línea del archivo 
finalizando la línea agregada

El nuevo archivo contiene la siguiente información: 
Datos de información en la línea 1 
Datos de información en la línea 2 
Datos de información en la línea 3 
Datos de información en la línea 4 
Datos de información en la línea 5 
Este en una nueva línea en el archivo 
agregando la segunda línea del archivo 
finalizando la línea agregada
"""
import os

# Nombre del archivo
archivo = "informacion.dat"

# Verificar si el archivo ya existe
if os.path.exists(archivo):
    print(f"El archivo '{archivo}' ya existe, ha sido creado previamente .")
else:
    # Crear el archivo y escribe la información
    with open(archivo, "w") as file:
        file.write("Datos de informacion en la linea 1\n")
        file.write("Datos de informacion en la linea 2\n")
        file.write("Datos de informacion en la linea 3\n")
        file.write("Datos de informacion en la linea 4\n")
        file.write("Datos de informacion en la linea 5\n")
    print(f"El archivo '{archivo}' ha sido creado con éxito.")
    

#Método para agregar nuevas líneas

def agregar_nuevas_lineas():
    try: 
        file=open("informacion.dat","a")
        file.write("Este en una nueva línea en el archivo")
        file.write("\nagregando la segunda línea del archivo")
        file.write("\nfinalizando la línea agregada")
        file.close()
    except FileNotFoundError:
        print("No se encuentra el archivo")
    except Exception as e:
        print(f"{e}, se ha generado un error no previsto")

agregar_nuevas_lineas()        

file=open("informacion.dat", "r")
contenido=file.read()
print(contenido)
file.close()