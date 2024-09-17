class Vehiculo:
    def __init__(self, marca, modelo, nro_ruedas):
        self.marca = marca
        self.modelo = modelo
        self.nro_ruedas = nro_ruedas

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, nro_ruedas, velocidad, cilindrada):
        super().__init__(marca, modelo, nro_ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return f"Marca {self.marca}, Modelo {self.modelo}, {self.nro_ruedas} ruedas {self.velocidad} Km/h, {self.cilindrada} cc"


# Ingreso de datos parte 1
automovil1 = Automovil("Toyota", "Yaris", 4, 120, 800)
automovil2 = Automovil("Fiat", "Palio", 4, 95, 1200)
automovil3 = Automovil("Ford", "Fiesta", 4, 125, 1500)

vehiculos = [automovil1, automovil2, automovil3]

# Si se desea ingresar los datos por pantalla descomentar la sgte porción de código y comentar la anterior (L18 a L22)
"""

vehiculos = []
cantidad = int(input("¿Cuántos Vehículos desea insertar?:"))
    
    for i in range(cantidad):
        print(f"\nDatos del automóvil {i+1}")
        marca = input("Inserte la marca del automóvil: ")
        modelo = input("Inserte el modelo: ")
        nro_ruedas = int(input("Inserte el número de ruedas: "))
        velocidad = int(input("Inserte la velocidad en km/h: "))
        cilindrada = int(input("Inserte el cilindraje en cc: "))
        
auto = Automovil(marca, modelo, nro_ruedas, velocidad, cilindrada)
vehiculos.append(auto)
"""
print("\nImprimiendo por pantalla los Vehículos:")
for id, auto in enumerate(vehiculos, 1):
    print(f"Datos del automóvil {id} : {auto}")

    
    


