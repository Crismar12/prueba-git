#Ejercicio 1: Clase Vehiculo y Herencia

class Vehiculo:
    
    def __init__(self, marca, modelo, año):
        
        self.marca = marca
        self.modelo = modelo
        self.año = año
        
    def descripcion(self):
        
        return f"el vehículo es de la marca {self.marca}, modelo {self.modelo} y el año {self.año}"
    
class Auto(Vehiculo): #esta clase hereda de la clase vehiculo
    def __init__(self, marca, modelo, año, numero_puertas):
        super().__init__(marca, modelo, año)
        self.numero_puertas = numero_puertas
        
    def tipo_auto(self):
        if self.numero_puertas >= 4:
            return f"{self.marca} {self.modelo} es un auto familiar"
        elif self.numero_puertas <=0:
            return f"número de puertas del auto {self.marca} {self.modelo} es inválido"
        else:
            return f"el {self.marca} {self.modelo} es un auto deportivo"  
            
auto1 = Auto("Toyota", "Corolla", 2022, 4)
auto2 =Auto("Audi", "A3 Sedán",2019, 3)
auto3 = Auto("Mercedes", "Genial", 2023, -1)
 
print(auto1.descripcion()) 
print(auto3.descripcion())   
print(auto3.tipo_auto())         
print(auto2.tipo_auto())  
print(auto1.tipo_auto())
print(auto2.descripcion())
                
"""Se usa super() cuando en la clase hija se necesita sobrescribir el 
constructor (__init__) pero sin perder la inicialización de la clase base.
En cambio, si solo se heredan métodos y atributos sin modificar el constructor, 
no es necesario usar super()."""

#EJERCICIO 2: Clase Estudiante con Métodos Estáticos y de Clase

class Estudiante:
    
    politica_aprobacion = 13
    
    def __init__(self, nombre, apellido, promedio):
        self.nombre = nombre
        self.apellido = apellido
        self.promedio = promedio
        
    @staticmethod
    
    def mensaje_motivador():
        return f"¡Sé perseverante!"
    
    @classmethod
    
    def mostrar_politica_aprobacion(cls):
        return f"La política de aprobación es tener un promedio mayor o igual a {cls.politica_aprobacion}"
    
    def aprobo(self):
        
        if self.promedio >= self.politica_aprobacion:
            return f"el estudiante {self.nombre} {self.apellido} está aprobado"
        else:
            return f"el estudiante {self.nombre} {self.apellido} está desaaprobado"
        
estudiante01 = Estudiante("Maria", "López", 13)
estudiante02= Estudiante("Paula", "Perez", 7)

print(Estudiante.mensaje_motivador())
print(Estudiante.mostrar_politica_aprobacion())
print(estudiante01.aprobo())
print(estudiante01.nombre)
print(estudiante02.aprobo())
print(estudiante02.nombre)
    
#EJER 3: INVENTARIO DE TIENDA (libreta)

#EJER 4: Mascotas y Dueños

class Mascota:
    
    def __init__(self, nombre, tipo, edad):
        self.nombre = nombre
        self.tipo = tipo
        self.edad = edad
        
class Dueño:
    
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono
        self.mascotas = []
        
    def agregar_mascotas(self,mascota):
        self.mascotas.append(mascota)
        
    def listar_mascotas(self):
        
        if not self.mascotas:
            return f"{self.nombre} no tiene mascotas"
        
        nombres_mascotas = [m.nombre for m in self.mascotas]   #m es un objeto de nombre (atributo) de la clase Mascota que fue instanciada y guardada en mascotas[]
        return f"Mascotas de {self.nombre}: {",".join(nombres_mascotas)}" 
        
mascota1 = Mascota("sandy", "perro", 4)
mascota2 = Mascota("pepino", "gato", 7)
mascota3 = Mascota("luchuga", "pajaro", 3)
mascota4 = Mascota("paulo", "gato", 5)

dueño1 = Dueño("Maria", 123456)
dueño2 = Dueño("Roberto", 2344756)

dueño1.agregar_mascotas(mascota1)
dueño1.agregar_mascotas(mascota2)

dueño2.agregar_mascotas(mascota3)
dueño2.agregar_mascotas(mascota4)

print(dueño1.listar_mascotas())
print(dueño2.listar_mascotas())

#Herencia Multiple: Piloto Comercial

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
class Empleado:
    def __init__(self,id_empleado, departamento):
        self.id_empleado = id_empleado
        self.departamento = departamento
class PilotoComercial(Persona,Empleado):
    def __init__(self, nombre, edad, id_empleado, departamento, horas_vuelo):
        Persona.__init__(self,nombre,edad)
        Empleado.__init__(self,id_empleado,departamento)
        self.horas_vuelo = horas_vuelo
        
    def vuelos(self):
        if not self.horas_vuelo:
            return f"No hay horas de vuelo ingresadas"
        elif self.horas_vuelo > 1500:
            
            return f" {self.nombre} puede realizar vuelos internacionales"
            
        else:
            
            return f" {self.nombre} no puede realizar vuelos internacionales"
            
piloto1 = PilotoComercial("Mario", 23, 55678, "cuzco",1800)
piloto2 = PilotoComercial("Luisa", 24, 23456, "arequipa",1200)

print(piloto1.vuelos())
print(piloto2.vuelos())
        
            
    


