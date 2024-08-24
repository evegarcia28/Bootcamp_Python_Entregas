"""En esta actividad trabajaremos con listas. Tomando la lista que se entrega a continuación, se
solicita realizar las siguientes acciones en el orden indicado:
1. Eliminar los elementos duplicados.
2. Ordenar la lista resultante en orden ascendente.
"""

mi_lista = [5, 20, 15, 20, 25, 50, 20, 5, 18, 15]
print(f"Mi lista inical: {mi_lista}")

mi_lista_sin_repetidos= list(set(mi_lista))     #set transforma la lista en conjunto ({}) y elimina duplicados pero agrego 'list' porque necesito que me devuelva una nueva lista para seguir trabajando en ella.
print(f"Mi lista sin repetidos: {mi_lista_sin_repetidos}")

mi_lista_sin_repetidos.sort()   #el método .sort() ordena los elementos de la lista de forma ascendente (no funciona con conjuntos ni diccionarios)
print(f"Mi lista sin repetidos y con orden ascendente: {mi_lista_sin_repetidos}")