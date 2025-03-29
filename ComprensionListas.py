#ejercicio 1: elevar al cuadrado

cuadrados = [i**2 for i in range(1,11)]
print(cuadrados) 

#ejercicio 2: filtrar cadenas
palabras = ["perro", "sol", "luna", "estrella", "mar"]

palabras_largas = [palabra for palabra in palabras if len(palabra) > 4]
print(palabras_largas) 

#ejercicio 3: Números impares al cubo

cuadrados_impares = [i**3 for i in range(1,16) if i % 2 != 0]

print(cuadrados_impares)

#ejercicio 4: clasificación par/impar ######

clasificacion = [(i, "par") if i % 2 == 0 else (i, "impar") for i in range(1,11)]
print(clasificacion)

#ejercicio 5: comprension de diccionarios #####
claves = ["nombre", "edad", "ciudad"]
valores =  ["Ana", 28, "Lima"]

diccionario = {clave: valor for clave, valor in zip(claves, valores)}
print(diccionario)

#ejercicio 6: Filtrar múltiplos de 3 y 5
multiplos = [i for i in range(1, 51) if i % 3 == 0 or i % 5 == 0]
print(multiplos)

#ejercicio 7: Comprension de tuplas ######
#convierte una lista de números en una tupla de sus dobles
tupla_dobles = tuple(i * 2 for i in [1,2,3,4,5])
print(tupla_dobles)

#ejercicio 8: Crear lista de booleanos 
mayores_que_cinco = [i > 5 for i in range (1,11)]
print(mayores_que_cinco)

#ejercicio 9: Convertir celsius a fahrenheit #####

temperaturas_celcius = [0, 20, 30, 40, 100]
temperaturas_fahrenheit = [((temp * 9/5) + 32) for temp in temperaturas_celcius]
print(temperaturas_fahrenheit)

#ejercicio 10: comprensión de lista anidado #######
#Crea una lista con los productos de todos los pares de números del 1 al 3 y del 4 al 6.

productos = [i * j for i in range (1,4) for j in range(4, 7)]
print(productos)

"""Cuando usas dos for en comprensión de listas, 
el primer valor del primer for se combina con 
todos los valores del segundo for, antes de que 
el primer for pase al siguiente valor.
Lo mismo pasaría si tuvieras tres for, el
tercer for cambiaría más rápido que el segundo, 
y el segundo más rápido que el primero."""

"""Paso a paso:
1 * 4 = 4
1 * 5 = 5
1 * 6 = 6
2 * 4 = 8
2 * 5 = 10
2 * 6 = 12
3 * 4 = 12
3 * 5 = 15
3 * 6 = 18"""

