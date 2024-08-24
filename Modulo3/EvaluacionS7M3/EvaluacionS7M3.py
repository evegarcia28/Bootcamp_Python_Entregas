"""Dada una lista de diccionarios que representan información de estudiantes, realiza las siguientes
tareas:
Se debe imprimir cada dato de las listas en pantalla con las siguientes excepciones:
• Filtra y muestra únicamente los estudiantes que tienen más de 18 años y cuyo promedio de
calificaciones sea superior a 85.
• Calcula el promedio de las calificaciones de los estudiantes que tienen más de 18 años y
cuya edad sea un número primo"""

estudiantes = [
 {'nombre': 'Juan', 'edad': 17, 'calificaciones': [85, 90, 88]},
 {'nombre': 'María', 'edad': 19, 'calificaciones': [92, 89, 90]},
 {'nombre': 'Pedro', 'edad': 21, 'calificaciones': [85, 95, 80]},
 {'nombre': 'Ana', 'edad': 18, 'calificaciones': [90, 92, 87]},
 {'nombre': 'Luis', 'edad': 20, 'calificaciones': [88, 85, 92]},
]
#filtra y muestra los estudiantes > de 18 años y con promedio > a 85.
i = 0
while i < 5:
    notas = (estudiantes[i]['calificaciones'])
    promedio= sum(notas)/len(notas)
    if int((estudiantes[i]['edad'])) > 18 and promedio > 85:
        print(f"El estudiante de nombre: {(estudiantes[i]['nombre'])}, que tiene {(estudiantes[i]['edad'])} años, tiene un promedio de: {promedio:.1f}")
        i = i + 1
    else:
        i = i + 1    
        
#calcula promedio de notas de estudiantes >18 años y con edad = a número primo.
i = 0
while i < 5:
    notas = (estudiantes[i]['calificaciones'])
    promedio= sum(notas)/len(notas)
    if int((estudiantes[i]['edad'])) > 18:
        edad_n = int((estudiantes[i]['edad']))
        contador_divisores = 0
        for val in range(1, edad_n + 1):
            if (edad_n/val).is_integer():
                contador_divisores = contador_divisores + 1
            else:
                contador_divisores = contador_divisores
        if contador_divisores == 2:
            print(f"El estudiante de nombre: {(estudiantes[i]['nombre'])}, su edad es {edad_n} y corresponde a un número primo. Su promedio de notas es: {promedio:.1f} ")
            i = i + 1
    else:
        i = i + 1