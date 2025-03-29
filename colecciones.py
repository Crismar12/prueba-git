#crear una lista y acceder a sus elementos
cosmeticos = ["pintura labial", "crema facial", "tónico", "gel"]

print(cosmeticos[0:])
print(cosmeticos[2])

#modificar
cosmeticos[-1] = "base"
print(cosmeticos[0:])

#eliminar 

del cosmeticos[2]
print(cosmeticos[0:])

cosmeticos.remove("base")
print(cosmeticos[0:])

cosmeticos.pop(0)
print(cosmeticos[0:])

#añadir elementos
cosmeticos.insert(0, "retinol")
cosmeticos = cosmeticos + ["esmalte", "labial"]
cosmeticos.append("mango")

print(cosmeticos, "jeje")

#desempacar elementos de una lista 
comestico1, cosmetico2, cosmeticos3, cosmeticos4, cosmeticos5 = cosmeticos
print("Cosmetico 1: ", comestico1)

#ejer 1

estudiantes = ["raul", "jose", "paola", "maria", "ale"]

estudiantes[2]= "richard"

estudiantes.remove("raul")

estudiantes.append("tracy")

estudiantes.pop(1)

estudiantes.insert(0, "antonio")

print(estudiantes)

#tuplas ejer 2

contactos = ("Pedro", "juan@correo.com", "123-456-7890")
print(contactos[0:2])

#conjuntos ejer 3
frutas = ["manzana", "pera", "plátano", "manzana", "naranja", "plátano"]

frutas_conjunto = set(frutas)

print(frutas_conjunto)

frutas_conjunto.remove("pera")
print(frutas_conjunto)

frutas_lista = list(frutas_conjunto)

print(frutas_lista)

inventario = {"laptop": 5, "teclado": 10, "ratón": 7}
#acceder a elementos de diccionario
print(inventario['teclado'])
print(inventario.get('ratón'))

#añadir elemento a diccionario
inventario["pantalla"] = 20
print(inventario)
#borrar elemento
del inventario["pantalla"]
print(inventario)

inventario.pop("laptop")
print(inventario)
#verificar si un producto esta en el inventario
print("tablet" in inventario)

#ejer 5 funcion zip
nombres = ["Ana", "Juan", "Carlos", "Luis"]
edades = [28, 34, 45, 25]

personas = zip(nombres, edades)
print(next(personas))
print(next(personas))
print(next(personas))
print(next(personas))

#ejer 6:comprension de listas-numeros pares

numeros_pares = [num for num in range(2, 41 ,2)]
print(numeros_pares)
print(max(numeros_pares))

#otra forma
numeros_pares = []
for num in range(2,41,2):
    numeros_pares.append(num)
    
    print(numeros_pares)
#ejer 7: Lista-Películas favoritas

pelis = ["rey leon", "miraculos", "matrix", "100 metros", "escape"]

del pelis[1]

pelis.append("wicked")

pelis.insert(1, "dora")

print(pelis)

