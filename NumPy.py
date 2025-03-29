
import numpy as np

"""
1: Crea un arreglo de NumPy con los números del 1 al 5 e imprime:
El tipo de datos del arreglo
La forma (shape) del arreglo
La cantidad de dimensiones (ndim)
"""
ar = np.arange(1,6)
print(ar.dtype)
print(ar.shape)
print(ar.ndim)

"""
2: Crea un arreglo de NumPy con los números del 1 al 10 y luego:
Multiplica todos sus elementos por 2
Suma 5 a todos los elementos
Calcula la media y la suma total del arreglo
"""
ar2 = np.arange(1,11)
print(ar2*2)
print(ar2+5)
print(ar2.mean())
print(ar2.sum())

"""
3: Ejercicio:
Crea una matriz de 3x3 con valores del 1 al 9 y:
Imprime la matriz
Obtén la forma (shape) y el número de dimensiones (ndim)
"""
ar3 = np.arange(1,10).reshape(3, 3)
print(ar3)
print(ar3.shape)
print(ar3.ndim)

"""
4: Ejercicio:
Crea un arreglo de NumPy con valores del 1 al 10 y 
obtén solo los valores que sean mayores a 5.
"""
ar4 = np.arange(1,11)
filtro = ar4 > 5
print(ar2[filtro])

"""
5: Ejercicio:
Crea los siguientes arreglos usando NumPy:
Un arreglo de ceros con forma (3,2)
Un arreglo de unos con forma (2,4)
Un arreglo lleno de sietes con forma (3,3)
"""
ar5 = np.zeros((3,2))
ar6 = np.ones((2,4))
ar7 = np.full((3,3),7)

print(ar5)
print(ar6)
print(ar7)

"""
6: Ejercicio:
Dada la siguiente matriz:
Realiza las siguientes acciones:

Imprime el elemento en la posición (1,1)
Imprime la segunda fila completa
Imprime la última columna completa
"""
arr = np.array([[10,20,30], [40,50,60], [70,80,90]])
print(arr)
print(arr[1,1])
print(arr[1, : ]) 
print(arr[ : , -1])

"""
7: Ejercicio: 
Ejercicio:
Usa NumPy para generar:
Un número aleatorio entre 0 y 1
Una matriz 2x3 de números enteros aleatorios entre 1 y 50
"""
arra = np.random.rand()
print(arra)
arra2 = np.random.randint(1, 51, (2,3))
print(arra2)

"""
8: Ejercicio:
Dado el siguiente arreglo:
Calcula e imprime:
El valor mínimo
El valor máximo
La suma total
La media
"""
arra3 = np.array([5,10,15,20,25,30])

print(arra3.min())
print(arra3.max())
print(arra3.sum())
print(arra3.mean())

"""
9: Ejercicio:
Crea un array con valores del 10 al 50 y muestra sus propiedades
Crea un array de NumPy con valores del 10 al 50 (incluidos).
Muestra su forma (shape), tamaño (size), número de dimensiones (ndim) y tipo de datos (dtype).
"""

arr = np.arange(10,51)
print(arr.shape)
print(arr.size)
print(arr.ndim)
print(arr.dtype)

"""
10: Ejercicio:
Genera una matriz de 3x3 con valores aleatorios entre 1 y 100.
Muestra la matriz generada.
Calcula la media y la varianza de la matriz.
"""
arra = np.random.randint(1, 101, (3, 3))
print(arra)
print("Media: ", arra.mean())
print("Varianza: ", arra.var())

"""
11: Ejercicio:
Crea dos matrices de 2x3 con valores aleatorios entre 1 y 20.
Suma ambas matrices.
Multiplica sus elementos.
Calcula el producto punto entre ellas (trasponiendo una de las matrices si es necesario).
"""
a = np.random.randint(1, 21, (2, 3))
b = np.random.randint(1, 21, (2, 3))
print(a)
print(b)
print(a + b)
print(np.add(a, b)) #hace lo mismo que (a + b)
print(np.multiply(a, b))

"""
12: Ejercicio:
Crea un array de 12 elementos secuenciales.
Reshapea el array en una matriz de 3x4.
Aplana la matriz en un array unidimensional nuevamente.
"""
arra = np.arange(1,13) 
print(arra)
print(arra.reshape(3,4))
print("array aplanado", arra.ravel()) #salida igual al arra sin reshape