"""
Partiendo del ejercicio anterior (ComprobacionS9M4), construya una función que reemplace el contenido de “Información” por “Procesamiento”, e imprima cuántos reemplazos realizó en el archivo.
Teniendo como salida lo siguiente: 
$ $ python ejercicio.py 
Se realizaron: 5 remplazos

El contenido del archivo informacion.dat es: 
Datos de Procesamiento en la línea 1 
Datos de Procesamiento en la línea 2 
Datos de Procesamiento en la línea 3 
Datos de Procesamiento en la línea 4 
Datos de Procesamiento en la línea 5 
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

def remplazar_datos_archivo(texto_viejo, texto_nuevo):
    
    try: 
        archivo = open('informacion.dat', 'r') 
        remplazo = "" 
        contador_reemplazos=0
        for linea in archivo: 
            linea = linea.strip()
            ocurrencias= linea.count(texto_viejo)
            contador_reemplazos +=ocurrencias 
            cambios = linea.replace(texto_viejo, texto_nuevo) 
            remplazo = remplazo + cambios + "\n" 
        archivo.close() 
        
        archivo_remplazo = open('informacion.dat', 'w') 
        archivo_remplazo.write(remplazo) 
        archivo_remplazo.close() 
        return contador_reemplazos
        
    except FileNotFoundError:
        print('No se encuentra el archivo informacion.dat') 
    except Exception as e: 
        print(f'{e} Se ha generado un error no previsto') 
    finally: print("\nEl reemplazo se ha realizado satisfactoriamente:") 

reemplazos= remplazar_datos_archivo("informacion", "Procesamiento")
if reemplazos:
    print(f"\nSe realizaron: {reemplazos} reemplazos.")
else:
    print("\nNo se realizaron reemplazos.") #se muestra cuando el programa se ejecuta más de 1 vez (ya realizó el remplazo)
file=open("informacion.dat", "r")
contenido=file.read()
print(contenido)
file.close()