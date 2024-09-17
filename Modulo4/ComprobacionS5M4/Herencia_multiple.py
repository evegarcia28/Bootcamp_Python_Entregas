"""
Herencia en Python.
EJERCICIOS:
Para llevar a cabo esta actividad, comenzaremos con la base del siguiente código en Python: (ver más abajo)
1. Construya una nueva clase C que tenga herencia múltiple de B y A respectivamente, y que contenga el metodo_c que imprima por pantalla “Método de clase C”. 
2. Cree un nuevo objeto C, y al instanciarlo y acceder a cada método: metodo_a, metodo_b y metodo_c tenga como resultado lo siguiente:
1 Clase B 
2 Método heredado de A 
3 Método heredado de B 
4 Método de clase C
"""
#código base
class A: 
    def __init__(self): 
        print("Pertenezco a la clase A") 
    
    def metodo_a(self): 
        print("Método heredado de A") 
        
class B: 
    def __init__(self): 
        print("Clase B") 
    
    def metodo_b(self): 
        print("Método heredado de B")

#1. creación clase C
        
class C(B,A):
    def __init__(self):
        super().__init__()
        
    def metodo_c(self):
        print("Método de clase C")
        
#2. Creación objeto C
objetoC= C()
objetoC.metodo_a()
objetoC.metodo_b()
objetoC.metodo_c()
        