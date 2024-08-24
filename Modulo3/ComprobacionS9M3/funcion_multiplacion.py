"""Crear una función que acepte dos parámetros (base y altura) y calcule el área de un rectángulo.
Validar que ambos sean números positivos."""


def area_rectangulo(base,altura):
    if base>0 and altura>0:
        area=(base*altura)
        return area
    else:
        return "Error: La base y la altura deben ser números positivos"
    

base= float(input("Ingrese la medida de la base de su rectángulo:"))
altura= float(input("Ingrese la altura de su rectángulo:"))

print(f"El área de un rectángulo de base: {base} y altura: {altura} es: {area_rectangulo(base,altura)}")
