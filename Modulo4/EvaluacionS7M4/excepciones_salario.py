"""
Diseñe una nueva clase de excepción definida por el usuario, que gestione la entrada del valor de una variable salario, y la misma se encuentre entre los valores de 1000 y 2000; de lo contrario, se lanza una excepción que refleja que el salario no se encuentra en el rango de 1000 y 2000.
"""
class RangoSalarioError(Exception):
    def __init__(self, salario):
        super().__init__(f"El monto '{salario}' asignado a Salario no está definido en el rango (1000 a 2000)")

def validar_salario(salario):
    if salario<1000 or salario>2000:
        raise RangoSalarioError(salario)
    return salario

try:
    salario= int(input("Ingrese el salario: "))
    validar_salario(salario)
except RangoSalarioError as e:
    print(f"Error: {e}")
else:
    print("Valor ingresado dentro del rango permitido.")