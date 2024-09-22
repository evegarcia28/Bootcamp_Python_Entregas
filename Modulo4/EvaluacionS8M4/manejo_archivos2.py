"""
Partiendo de la actividad realizada en el ejercicio de Comprobación, construya una función que lea el contenido del archivo informacion.dat.
Teniendo como salida lo siguiente: 
$ python ejercicio.py 
El archivo informacion.dat ya existe, ha sido creado previamente 
Datos de información en la línea 1 
Datos de información en la línea 2 
Datos de información en la línea 3 
Datos de información en la línea 4 
Datos de información en la línea 5
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
        file.write("Datos de informaciin en la linea 4\n")
        file.write("Datos de informacion en la linea 5\n")
        file.close()
    print(f"El archivo '{archivo}' ha sido creado con éxito.")
    
file=open("informacion.dat", "r")
contenido=file.read()
print(contenido)
file.close()