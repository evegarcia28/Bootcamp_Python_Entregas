"""Crear una función que sume dos números, otra que reste dos números, otra que multiplique dos
números, y otra que divida dos números. Adicionalmente, crear una función que acepte dos
números como parámetros y regrese el resultado en forma de tupla de su suma, resta,
multiplicación y división.
Los resultados se deben almacenar en un diccionario, cuyas claves serán: Suma, Resta,
Multiplicación y División, y los valores de cada clave serán los resultados obtenidos con la función
creada anteriormente."""


def sumar(a,b):
    suma=(a+b)
    return suma

def restar(a,b):
    resta=(a-b)
    return resta

def multiplicar(a,b):
    multiplica=(a*b)
    return multiplica

def dividir(a,b):
    if b == 0:
        return "Error: División por cero no valida"
    divide=f"{a/b:.1f}" #para que me entregue un resultado de división con solo 1 decimal
    return divide

def tupla_operaciones(a,b):
    return (sumar(a,b), restar(a,b), multiplicar(a,b), dividir(a,b))
    
def diccionario_operaciones(a,b):
    resultados= tupla_operaciones(a,b)
    diccionario_resultados = {
        'suma': resultados[0],
        'resta': resultados[1],
        'multiplicacion': resultados[2],
        'division': resultados[3]
    }
    return diccionario_resultados

a= int(input("Ingrese el primer número:"))
b= int(input("Ingrese el segundo número:"))
resultado= diccionario_operaciones(a,b)
print(resultado)

