"""Dada la siguiente lista de nombres:
• Harry Houdini
• Newton
• David Blaine
• Hawking
• Messi
• Teller
• Einstein
• Pele
• Juanes
Y sabiendo que Harry Houdini, David Blaine y Teller son magos. Y también que Newton, Hawking y
Einstein son científicos. Debemos separar los nombres en tres grupos: magos, científicos y otros; y
escribir una función llamada hacer_grandioso(), que modifique la lista de magos añadiendo la
frase ‘El gran‘ antes del nombre de cada mago.
Crear una función llamada imprimir_nombres(), que imprime el nombre de cada persona de la
lista.
Finalmente, imprimir en pantalla la lista completa de nombres antes de ser modificados; luego
imprimir los nombres de los magos grandiosos, los nombres de los científicos, y los restantes."""


# Lista original de nombres
nombres = ["Harry Houdini", "Newton", "David Blaine", "Hawking", "Messi", "Teller", "Einstein", "Pele", "Juanes"]

# Grupos de nombres
magos = []
cientificos = []
otros = []

# Separar los nombres en sus respectivos grupos
for nombre in nombres:
    if nombre in ["Harry Houdini", "David Blaine", "Teller"]:
        magos.append(nombre)
        
for nombre in nombres:
    if nombre in ["Newton", "Hawking", "Einstein"]:
        cientificos.append(nombre)

for nombre in nombres:
    if nombre not in magos and nombre not in cientificos:
        otros.append(nombre)
        

# Función para hacer grandiosos a los magos
def hacer_grandioso(magos):
    for i in range(len(magos)):
        magos[i] = "El gran " + magos[i]
    return magos

# Función para imprimir nombres
def imprimir_nombres(nombres):
    resultado=[]
    for nombre in nombres:
        resultado.append(nombre)
    return (", ".join(resultado)) #se usó .join() para unir los elementos de la lista

# Imprimir lista completa antes de ser modificada
print(f"Lista original de nombres: {imprimir_nombres(nombres)}")

# Imprimir los nombres de los magos grandiosos, científicos y otros:

hacer_grandioso(magos)
print(f"Magos grandiosos: {imprimir_nombres(magos)}")

print(f"Científicos: {imprimir_nombres(cientificos)}")

print(f"Otros: {imprimir_nombres(otros)}")


