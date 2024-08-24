#Requerimos crear un registro de datos personales de tres personas. Los datos que se necesitan son: su nombre, apellido y teléfono. Para ello, generaremos un diccionario para cada una de las personas con los datos mencionados, y luego los almacenaremos dentro de una lista. Finalmente, imprimiremos en pantalla la lista.

persona1 = {'Nombre': 'Pedro',
            'Apellido': 'Torres',
            'Telefono': '12345678'}
persona2 = {'Nombre': 'Andres',
            'Apellido': 'Lopez',
            'Telefono': '23456789'}
persona3 = {'Nombre': 'Maria',
            'Apellido': 'Andrade',
            'Telefono': '98765432'}

listaPersonas = [persona1, persona2, persona3]
print(listaPersonas)