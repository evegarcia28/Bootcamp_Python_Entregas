#Parte 2:

class Vehiculo:
    def __init__(self, marca, modelo, nro_ruedas):
        self.marca = marca
        self.modelo = modelo
        self.nro_ruedas = nro_ruedas
        
#Hereda de Vehículo:
class Automovil(Vehiculo):
    def __init__(self, marca, modelo, nro_ruedas, velocidad, cilindrada):
        super().__init__(marca, modelo, nro_ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return f"Marca {self.marca}, Modelo {self.modelo}, {self.nro_ruedas} ruedas {self.velocidad} Km/h, {self.cilindrada} cc"

#Heredan de Automóvil:
class Particular(Automovil):
    def __init__(self, marca, modelo, nro_ruedas, velocidad, cilindrada, nro_puestos):
        super().__init__(marca, modelo, nro_ruedas, velocidad, cilindrada)
        self.nro_puestos = nro_puestos

    def __str__(self):
        return f"{super().__str__()} Puestos: {self.nro_puestos}"

class Carga(Automovil):
    def __init__(self, marca, modelo, nro_ruedas, velocidad, cilindrada, peso_carga):
        super().__init__(marca, modelo, nro_ruedas, velocidad, cilindrada)
        self.peso_carga = peso_carga

    def __str__(self):
        return f"{super().__str__()} Carga: {self.peso_carga} Kg"

#Hereda de Vehículo:
class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, nro_ruedas, tipo_bicicleta):
        super().__init__(marca, modelo, nro_ruedas)
        self.tipo_bicicleta = tipo_bicicleta

    def __str__(self):
        return f"Marca {self.marca}, Modelo {self.modelo}, {self.nro_ruedas} ruedas Tipo: {self.tipo_bicicleta}"

#Hereda de Bicicleta:
class Motocicleta(Bicicleta):
    def __init__(self, marca, modelo, nro_ruedas, tipo_bicicleta, motor, cuadro, nro_radios):
        super().__init__(marca, modelo, nro_ruedas, tipo_bicicleta)
        self.motor = motor
        self.cuadro = cuadro
        self.nro_radios = nro_radios

    def __str__(self):
        return f"{super().__str__()} Motor: {self.motor}, Cuadro: {self.cuadro}, Nro Radios: {self.nro_radios}"

print("---------------------------------------------------------------------------------------------")
# Ejemplo de uso
particular = Particular("Ford", "Fiesta", 4, 180, 500, 5)
carga = Carga("Daft Trucks", "G 38", 10, 120, 1000, 20000)
bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
motocicleta = Motocicleta("BMW", "F800s", 2, "Deportiva", "2T", "Doble Viga", 21)

vehiculos = [particular, carga, bicicleta, motocicleta]

for vehiculo in vehiculos:
    print(vehiculo)
print("---------------------------------------------------------------------------------------------")

# Crear una instancia de Motocicleta
motocicleta = Motocicleta("BMW", "F800s", 2, "Deportiva", "2T", "Doble Viga", 21)

# Verificar relaciones de instancia
print(f"Motocicleta es instancia con relación a Vehículo: {isinstance(motocicleta, Vehiculo)}")
print(f"Motocicleta es instancia con relación a Automóvil: {isinstance(motocicleta, Automovil)}")
print(f"Motocicleta es instancia con relación a Vehículo particular: {isinstance(motocicleta, Particular)}")
print(f"Motocicleta es instancia con relación a Vehículo de Carga: {isinstance(motocicleta, Carga)}")
print(f"Motocicleta es instancia con relación a Bicicleta: {isinstance(motocicleta, Bicicleta)}")
print(f"Motocicleta es instancia con relación a Motocicleta: {isinstance(motocicleta, Motocicleta)}")
print("---------------------------------------------------------------------------------------------")