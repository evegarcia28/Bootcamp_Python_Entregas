class Persona:
    def __init__(self, nombre, apellido, anno):
        self.nombre=nombre
        self.apellido=apellido
        self.anno=anno


class Departamento:
    def __init__(self, nombre_dpto, nombre_corto_dpto):
        self.nombre_depto=nombre_dpto
        self.nombre_corto_depto=nombre_corto_dpto
        
        
class Trabajador(Persona, Departamento):
    def __init__(self, nombre, apellido, anno, nombre_dpto, nombre_corto_dpto, salario):
        Persona.__init__(self, nombre, apellido, anno)
        Departamento.__init__(self, nombre_dpto, nombre_corto_dpto)
        self.salario=salario

obj_trabajador= Trabajador('Juan', 'Perez', 2005,'Ingeniería de software','IS',20000)
print(obj_trabajador.__dict__)

print("Es trabajador instancia de Persona: ", isinstance(obj_trabajador, Persona))
print("Es trabajador instancia de Departamento: ", isinstance(obj_trabajador,Departamento))
print("Es trabajador instancia de Trabajador: ", isinstance(obj_trabajador, Trabajador))