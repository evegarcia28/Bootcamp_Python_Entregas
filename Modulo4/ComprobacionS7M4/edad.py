"""
Diseñe un programa en Python que pida la edad al usuario por consola. El usuario debe ingresar un número entero; en caso contrario, el programa arrojará una excepción y le solicitará que ingrese su edad nuevamente.
Seguidamente, el programa debe imprimir que es Adulto si es mayor o igual a 18; y en caso contrario, no es un adulto.
"""

def validar_edad(edad):
    if not isinstance(edad, int):
        raise ValueError("La edad debe ser un número entero.") #aquí se lanza la excepción para una edad no entero pero nunca se ejecutará pues en el try al solicitar la edad y definirla como int, cualquier ingreso "no entero" será capturado por ese ValueError.
    if edad<0:
        raise ValueError("La edad no puede ser negativa.")
    if edad >=18:
        print("Usted es un adulto")
    else:
        print("Usted es menor de edad")
    return edad

while True:
    try:
        edad=int(input("Introduce edad (debe ser un número entero): "))
        validar_edad(edad)
        break
    except ValueError as e:
        print(f"Error: {e} Por favor ingrese un valor válido para la edad.")
