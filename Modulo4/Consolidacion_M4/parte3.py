import csv
from Vehiculo import Particular,Carga,Bicicleta,Motocicleta

def guardar_datos_csv(vehiculos, nombre_archivo):
    try:
        with open(nombre_archivo, 'w', newline='') as archivo:
            archivo_csv = csv.writer(archivo)
            for vehiculo in vehiculos:
                datos = [vehiculo.__class__.__name__, vehiculo.__dict__]
                archivo_csv.writerow(datos)
        print(f"\nDatos guardados exitosamente en {nombre_archivo}")
    except IOError as e:
        print(f"Error al guardar los datos en {nombre_archivo}: {e}")
        
def leer_datos_csv(nombre_archivo):
    vehiculos = []
    try:
        with open(nombre_archivo, 'r') as archivo:
            archivo_csv = csv.reader(archivo)
            for fila in archivo_csv:
                clase_vehiculo = fila[0]  # se obtiene el nombre de la clase
                atributos = eval(fila[1]) # Convierte la cadena de diccionario de nuevo en diccionario para cumplir con el formato exijido
                print(f"\nLista de Vehiculos {clase_vehiculo}\n {atributos}")
        print(f"\nDatos leídos exitosamente desde {nombre_archivo}")
    except FileNotFoundError:
        print(f"Error: El archivo {nombre_archivo} no existe.")
    except IOError as e:
        print(f"Error al leer los datos desde {nombre_archivo}: {e}")

# Guardado y recuperación:
vehiculos = [
    Particular(marca='Ford', modelo='Fiesta', nro_ruedas=4, velocidad=180, cilindrada=500, nro_puestos=5),
    Carga(marca='Daft Trucks', modelo='G 38', nro_ruedas=10, velocidad=120, cilindrada=1000, peso_carga=20000),
    Bicicleta(marca='Shimano', modelo='MT Ranger', nro_ruedas=2, tipo_bicicleta='Carrera'),
    Motocicleta(marca='BMW', modelo='F800s', nro_ruedas=2, tipo_bicicleta='Deportiva', motor='2T', cuadro='Doble Viga', nro_radios=21)
]

# Guardar vehículos con manejo de excepciones
nombre_archivo = 'vehiculos.csv'
guardar_datos_csv(vehiculos, nombre_archivo)

# Leer datos con manejo de excepciones
leer_datos_csv('vehiculos.csv')
