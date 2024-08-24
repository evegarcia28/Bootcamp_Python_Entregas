#Se requiere contar con un programa que, dados 3 números diferentes, los evalúe y entregue el orden de mayor a menor.

n1 = int(input("Ingrese primer número:"))
n2 = int(input("Ingrese segundo número:"))
n3 = int(input("Ingrese tercer número:"))

if n1 > n2:
    if n1 > n3:
        mayor = n1
        if n2 > n3:
            medio = n2
            menor = n3
        else:
            medio = n3
            menor = n2
    else:
        mayor = n3
        medio = n1
        menor = n2
else:
    if n2 > n3:
        mayor = n2
        if n1 > n3:
            medio = n1
            menor = n3
        else:
            medio = n3
            menor = n1
    else:
        mayor = n3
        medio = n2
        menor = n1

print(f"Los números ordenados de mayor a menor son: {mayor} , {medio} , {menor}")

#Otra forma es usando el método 'sort' con el parámetro adicional 'reverse'

n1 = int(input("Ingrese primer número:"))
n2 = int(input("Ingrese segundo número:"))
n3 = int(input("Ingrese tercer número:"))

numeros= [n1,n2,n3]

numeros.sort(reverse=True)

print(f"Los números ordenados de mayor a menor son: {numeros}")