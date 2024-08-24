#Se solicita recorrer los datos numéricos que se encuentran dentro de la siguiente lista de listas:
"""Hay que imprimir cada dato de las listas en pantalla con las siguientes excepciones:
• Si el primer número de la sublista es cero, omitir la impresión de toda la sublista,
• Si existe un cero en cualquier otra posición, omitir solo la impresión del cero.
• Adicionalmente, crear un diccionario donde asignaremos la primera sublista a la clave A, la
segunda a la clave B, la tercera a la clave C, y la cuarta a la clave D.
• Finalmente, imprimiremos en pantalla el diccionario resultante."""

lista_de_listas= [[1,2,3], [0,4,5], [4,0,1], [6,5,4]]

#Crear diccionario a partir de lista_de_listas con claves A,B,C y D respectivamente:
claves = ['A','B','C','D']

diccionario = dict(zip(claves,lista_de_listas)) #la función 'zip()' toma 2 o + variables y las combina en pares.

#Se obtiene el sgte diccionario:
# diccionario = {'A': [1, 2, 3], 'B': [0, 4, 5], 'C': [4, 0, 1], 'D': [6, 5, 4]}


#Crea el diccionario final con claves y sin valores aún:
diccionario_final = { 'A':[], 'B': [], 'C': [], 'D': []}

for i in diccionario: # este for itera sobre las claves del diccionario, en c/iteración toma el valor de una clave.
    for val in diccionario[i]: #este otro for itera sobre los elementos de la lista q está asociada a la clave i iterada.
        if val == (diccionario[i][1]) and val == 0:  #si encuentra un 0 en el índice 1 lo salta y no lo agrega a la lista correspondiente en el diccionario final.
            continue
        (diccionario_final[i]).append(val)
    
    if (diccionario_final[i][0]) == 0: #si en el diccionario final encuentra una lista/valor que empieza por 0 (indice 0 es 0), elimina la clave y su lista asociada.
        diccionario_final.pop(i)

print(diccionario_final)
