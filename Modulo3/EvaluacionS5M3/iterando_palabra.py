"""Requerimos eliminar todas las vocales de la palabra “paralelepípedo”, e imprimir en pantalla las consonantes restantes y su posición dentro de dicha palabra."""

i = 0
for val in ("paralelepipedo"):
    i = i + 1
    if val in ["a","e","i","o","u"]:
        continue
    print(f"Letra {val} y su posición es {i}" )

print("fin")