"""Crear una lista con 10 números enteros, recorrerla haciendo uso de la sentencia for, e imprimir en
pantalla el valor de cada elemento indicando si es par, impar o cero"""
numeros=[5,8,21,-15,68,7,48,90,0,3]

#Si se necesita, también se puede pedir al usuario que ingrese los número por pantalla con el siguiente código:
'''numeros =[]
numeros.append(int(input("Ingrese el primer número: ")))
numeros.append(int(input("Ingrese el segundo número: ")))
numeros.append(int(input("Ingrese el tercer número: ")))
numeros.append(int(input("Ingrese el cuarto número: ")))
numeros.append(int(input("Ingrese el quinto número: ")))
numeros.append(int(input("Ingrese el sexto número: ")))
numeros.append(int(input("Ingrese el séptimo número: ")))
numeros.append(int(input("Ingrese el octavo número: ")))
numeros.append(int(input("Ingrese el noveno número: ")))
numeros.append(int(input("Ingrese el décimo número: ")))'''

for val in numeros:
    if val % 2==0 and val!=0:
        print(f" El número {val} es par")
    elif val == 0:
        print(f" El número {val} es cero")
    else:
        print(f" El número {val} es impar")