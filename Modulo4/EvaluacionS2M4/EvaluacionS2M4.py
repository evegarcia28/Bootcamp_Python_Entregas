"""
EJERCICIO:
Implementar en Python la clase Persona, que tenga como atributos: nombre, apellidos, sexo, edad,
estatura y peso. Adicionalmente, se deben implementar los métodos get y set que modifiquen todos
los atributos antes mencionados de la clase persona, recordando que los métodos get son los
métodos que permiten acceder al estado del objeto persona, y los métodos set permiten modificar
el estado de dicho objeto.
Cree dos objetos de la instancia persona con los siguientes datos:
Persona_ 1: Pedro, Vivas, Masculino, 20 años, 1.78 mts, 68 Kg.
Persona_ 2: Juan, Camargo, Masculino. 18, 1.8 mts, 75 Kg.
Modifique en la Persona_1 su edad a 21 años, y a la Persona_2 el apellido a Santiago, y que se
muestre por pantalla las actualizaciones respectivas. 
"""

class Persona:
    def __init__(self,nombre, apellidos, sexo, edad, estatura, peso):
        self.nombre=nombre
        self.apellidos=apellidos
        self.sexo=sexo
        self.edad=edad
        self.estatura=estatura
        self.peso=peso
    
    #método get:
    def get_nombre(self):
        return self.nombre
    
    def get_apellidos(self):
        return self.apellidos
    
    def get_sexo(self):
        return self.sexo
    
    def get_edad(self):
        return self.edad
    
    def get_estatura(self):
        return self.estatura
    
    def get_peso(self):
        return self.peso
    
    #método set:
    def set_nombre(self, nombre):
        self.nombre = nombre
    
    def set_apellidos(self, apellidos):
        self.apellidos = apellidos
    
    def set_sexo(self, sexo):
        self.sexo = sexo
    
    def set_edad(self, edad):
        self.edad = edad
    
    def set_estatura(self, estatura):
        self.estatura = estatura
    
    def set_peso(self, peso):
        self.peso = peso
        
Persona1= Persona('Pedro', 'Vivas', 'masculino', 20, 1.78, 68)
Persona2= Persona('Juan', 'Camargo', 'masculino', 18, 1.8, 75)

print(f"La persona 1 se llama: {Persona1.nombre} {Persona1.apellidos}, su género es {Persona1.sexo}, tiene {Persona1.edad} años, mide {Persona1.estatura} mts y pesa {Persona1.peso} kilos.")

print(f"La persona 2 se llama: {Persona2.nombre} {Persona2.apellidos}, su género es {Persona2.sexo}, tiene {Persona2.edad} años, mide {Persona2.estatura} mts y pesa {Persona2.peso} kilos.")

#modificaciones con set:

Persona1.set_edad(21)
Persona2.set_apellidos('Santiago')

print(f"Actualizacion: La persona 1 se llama: {Persona1.nombre} {Persona1.apellidos}, su género es {Persona1.sexo}, tiene {Persona1.edad} años, mide {Persona1.estatura} mts y pesa {Persona1.peso} kilos.")

print(f"Actualización: La persona 2 se llama: {Persona2.nombre} {Persona2.apellidos}, su género es {Persona2.sexo}, tiene {Persona2.edad} años, mide {Persona2.estatura} mts y pesa {Persona2.peso} kilos.")
