#Idem anterior pero solicitando los datos por pantalla

p1nombre= (input("Ingrese su nombre:"))
p1apellido=(input("Ingrese su apellido:"))
p1telefono=int(input("Ingrese tu telefono:"))

p2nombre= (input("Ingrese su nombre:"))
p2apellido=(input("Ingrese su apellido:"))
p2telefono=int(input("Ingrese tu telefono:"))

p3nombre= (input("Ingrese su nombre:"))
p3apellido=(input("Ingrese su apellido:"))
p3telefono=int(input("Ingrese tu telefono:"))

p1={'nombre':p1nombre, 'apellido':p1apellido, 'teléfono':p1telefono}
p2={'nombre':p2nombre, 'apellido':p2apellido, 'teléfono':p2telefono}
p3={'nombre':p3nombre, 'apellido':p3apellido, 'teléfono':p3telefono}

lista_diccionario = [p1,p2,p3]

print(lista_diccionario)