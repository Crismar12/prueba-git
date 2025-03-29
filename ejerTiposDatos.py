print("hola mundo")

#EJER 1 IDENTIFICAR TIPOS DE DATOS

cadena = "Hola Python"

numeros = 12345

decimal = 3.1416

lista = [1, 2, 3, 4]

valor = True

variable = {"clave" : "valor"}

print(cadena, type(cadena), "\n" 
, numeros, type(numeros), "\n", decimal, type(decimal), 
"\n", lista, type(lista), "\n",  valor, type(valor), "\n", variable, type(variable))

#ejercicio 2
numeros = float(numeros)

print(numeros)

decimal = int(decimal)

print(decimal)

#ejer 3
complejo = 4 + 3j
print(complejo, type(complejo))

#ejer 4
saludo = "Buenos días"

print(len(saludo))

print(saludo[0])

print(saludo[-1])

print(saludo[0:6]) #para rangos

texto = "mi nombre es"

print(texto.upper())
texto = "   mi nombre es   "
print(texto.strip()) # strip para quitar espacios

#ejer 5
import random 
print(random.randrange(1,100))

#ejer 6
x ="hola"
y= "mundo"
print(x + " " + y)

#ejer 7
saludo_2= "hola mundo"
print(saludo_2.count("o")) #para contar
print(saludo_2.replace("mundo", "python")) #para reemplazar

texto_2 = "python es divertido"
print(texto_2.split()) #divide la cadena en palabras

precio = 49
mensaje = "El precio es ${:.2f}".format(precio)
print(mensaje)

txt = "12345"
print("¿Es numérica?", txt.isnumeric())
print("¿Está en minúsculas?", txt.islower())

print(saludo_2.ljust(20, "*")) #para justificar a la izquierda rellenando los espacios
print(saludo_2.rjust(24, "$")) #para justificar a la derecha rellenando los espacios
print(saludo_2.center(40, "/")) #para centrar

txt = "Hola Mundo"
print(txt.swapcase()) #para intercambiar mayusculas por minusculas

#operadores aritmeticos

x = 10 #valor inicial de x

x+= 5 #suma
print("x + 5: ", x)
x-=3 #resta
print("x-3: ", x)
x %= 3
print("modulo de x entre 3:", x)

#operadores de comparacion

a=10
b= 3

print(f"\n¿Es {a} igual a {b}?", a==b)
print(f"¿Es {a} diferente de {b}?", a!=b)
print(f"¿Es {a} menor que {b}?", a<b)
print(f"Es {a} menor que {b}?", a<b)
print(f"Es {a} menor o igual que {b}?", a<=b)
print(f"Es {a} mayor o igual que {b}?", a>=b)

palabra1 = "manzana"
palabra2= "pera"

print(f"\n¿'{palabra1}' es menor que '{palabra2}'", palabra1<palabra2)

#operadores logicos

edad = 25
licencia = True

print(f"\n¿Es mayor de 18 y tiene licencia?: ", edad>18 and licencia)
print(f"\n¿Es menor de 18 o tiene licencia?: ", edad<18 or licencia)
print(f"\n¿No tiene licencia?", not licencia)

temperatura = 30
es_verano= True

print("\n¿La temperatura es menor a 15 o no es verano?", temperatura<15 or not es_verano)

#operadores de membresia

texto ="Python es divertido"

print("\n¿La palabra 'Python' está en el texto?", "Python" in texto)
print("\n¿La palabra 'Java' no está en el texto?", "Java" not in texto)

#operadores de identidad
x = [1,2,3]
y = [1,2,3]
z = x
j= [1,3,5]

print("\n¿x es igual a y en contenido:", x ==y )
print("\n¿x es y (mismo objeto en memoria)?", x is y)# es false porque las listas son objetos mutables 
print("\n¿x es z (mismo objeto en memoria)?", x is z)
print("\n¿x no es y?", x is not y)

a = 10
b = 10
c = 20

print("\n¿a es b (mismo objeto)? →", a is b) #es true porque los numeros enteros son objetos inmutables
print("¿a es c? →", a is c)
print("¿a no es c? →", a is not c)

#caso mas complejo

numeros = [10,20,30,40]
suma = sum(numeros)
promedio = suma / len(numeros)

print("\nSuma total mayor que promedio * cantidad:", suma > (promedio*len(numeros)))
print("Suma total menor que promedio * cantidad", suma < (promedio * len(numeros)))
print("Suma total igual a promedio * cantidad", suma == (promedio * len(numeros)))

