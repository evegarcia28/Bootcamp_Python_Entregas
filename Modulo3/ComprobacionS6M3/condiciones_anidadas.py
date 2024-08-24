"""Escribir un programa que analice un número, e indique si es positivo o negativo, y si es par o impar.
En caso de ser cero, también indicarlo. Se debe usar la expresión if-elif-else, y no usar
subcondiciones; en su lugar, usar condiciones anidadas."""

numero = int(input("Ingrese un número:"))

if numero > 0:
    if numero % 2 == 0:
        print("El número es positivo y par")
    else:
        print("El número es positivo e impar")
elif numero < 0:
    if numero % 2 == 0:
        print("El número es negativo y par")
    else:
        print("El número es negativo e impar")
else:
    print("El número es cero.")