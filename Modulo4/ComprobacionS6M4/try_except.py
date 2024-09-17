"""
Manejo de errores y excepciones.
EJERCICIO:
Una de las excepciones más comunes es la división por cero. Esto puede provocar las caídas de softwares completos, por lo que se vuelve fundamental su control; por este motivo se plantea como uno de los controles de excepción básicos. A continuación, se dan dos variables definidas como: 1 2 suma = 3000 contador = 0
Queremos dividir la variable suma por la variable contador.
El uso de la cláusula try... except... maneja el ZeroDivisionError. Si la división se realiza correctamente, imprima el resultado en la consola; de lo contrario, imprima en la consola el siguiente mensaje: 'División por cero.'
"""

# Variables dadas
suma = 3000
contador = 0

# Manejo de la división por cero
try:
    resultado = suma / contador
    print(f"El resultado de la división es: {resultado}")
except ZeroDivisionError:
    print("División por cero.")
