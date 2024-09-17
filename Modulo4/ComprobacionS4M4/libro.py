"""
Herencia y Polimorfismo.
EJERCICIOS:
Realice los pasos que se detallan a continuación:
1. La clase Libro está definida. Cree dos instancias de la clase Libro denominadas libro_1 y libro_2. Luego, asigne atributos de instancia a estos objetos (usando la notación de puntos) de la siguiente manera:
● libro_1:
○ autor = 'Dan Brown'
○ titulo = 'Infierno'
● libro_2:
○ autor = 'Dan Brown'
○ titulo = 'El Código Da Vinci'
○ ann_de_publicacion = 2003
2. En respuesta, imprima el valor del atributo __dict__ de libro_1 y libro_2.

3. Resultado al ejecutar: 

1 print(libro_1.__dict__) 
2 print(libro_2.__dict__)

Salida: 
1 {'author': 'Dan Brown', 'title': 'Inferno'} 
2 {'author': 'Dan Brown', 'title': 'The Da Vinci Code', 'year_of_publishment': 2003}
"""
class Libro():
    def __init__(self, autor, titulo, ann_de_publicacion=None):
        self.autor=autor
        self.titulo=titulo
        if ann_de_publicacion is not None:
            self.ann_de_publicacion=ann_de_publicacion 

libro1= Libro('Dan Brown', 'Inferno')
libro2= Libro('Dan Brown', 'El Código Da Vinci', 2003)

print(libro1.__dict__)
print(libro2.__dict__)