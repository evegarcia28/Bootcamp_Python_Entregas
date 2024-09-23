"""
Codifique en Python una clase que represente a un animal. Un animal tiene las siguientes
características comunes:
• Nombre.
• Raza.
• Edad.
• Peso.
Debe crear dos instancias u objetos de la clase Animal, cuyos objetos son un caballo y un león, con
las siguientes características particulares:
Caballo             León
Nombre Zeus         Nombre Boulder
Edad 5 años         Edad 10 años
Raza Pura sangre    Raza Atlas
Peso 450 kg         Peso 130 kg
"""

class Animal:
    def __init__(self,nombre,raza,edad,peso):
        self.nombre=nombre
        self.raza=raza
        self.edad=edad
        self.peso=peso
    
obj_caballo= Animal('Zeus','Pura sangre', 5, 450)
obj_leon= Animal('Boulder', 'Atlas', 10, 130)

print(f"El caballo se llama: {obj_caballo.nombre}, es de raza {obj_caballo.raza}, tiene {obj_caballo.edad} años y pesa {obj_caballo.peso} kilos.")

print(f"El león se llama: {obj_leon.nombre}, es de raza {obj_leon.raza}, tiene {obj_leon.edad} años y pesa {obj_leon.peso} kilos.")