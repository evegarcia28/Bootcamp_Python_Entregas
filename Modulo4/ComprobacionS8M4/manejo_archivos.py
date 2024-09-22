"""
Diseñe un programa en Python que cree un archivo si no se encuentra; en caso de existir el archivo, debe reflejar un mensaje que especifica que ya se encuentra el archivo previamente creado.
El archivo por crear debe llamarse informacion.dat. el cual contiene lo siguiente: 
Datos de informacion en la linea 1 
Datos de informacion en la linea 2 
Datos de informacion en la linea 3 
Datos de informacion en la linea 4 
Datos de informacion en la linea 5
"""

import os

# Nombre del archivo
archivo = "informacion.dat"

# Verificar si el archivo ya existe
if os.path.exists(archivo):
    print(f"El archivo '{archivo}' ya se encuentra previamente creado.")
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
    
