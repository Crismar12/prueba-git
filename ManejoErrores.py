#1:Divide y vencerás 
while True:
    try:
        num1 = int(input("Ingresa el primer número: "))
        num2 = int(input("Ingresa el segundo número: "))
        print(num1 / num2)
    except Exception as e:
        print("Hubo un error al dividir los números.")
        print(f"Detalles del error: {e}")
    else:
        print("¡División exitosa!")
        break  # Sale del bucle si no hay errores
    finally:
        print("Gracias por usar el programa\n")

#2 Acceso seguro al diccionario

pelicula = {'nombre': 'Blancanieves', 'año': 1960, 'director': 'Desconocido'}

while True:
    try:
        clave = input("Escribe una de las siguientes opciones: nombre, año o director. Para saber la información de la película").strip().lower()
        if clave in pelicula:
            print(f"El {clave} de la película es {pelicula[clave]}")
            break
        else:
            print("La clave ingresada no es válida.")
    except Exception as e:
        print(f"Detalle del error: {repr(e)}")
    else: 
        print("proceso exitoso")
    finally:
        print("gracias por usar el programa")
     
#3 Validación de lista:

lista = ["a", "b", "c", "d", "e"]

while True:
    try:
        indice = int(input("Ingresa un número, entre 0-4, para acceder al elemento de la lista"))
        if 0 <= indice <= len(lista):
            print(f"El elemento en la posicion {indice} es {lista[indice]}")
            break
        else:
            print("el número no está en el rango")
    except Exception as e:
        print(f"Detalles del error{repr(e)}")
    finally:
        print("Gracias por usar el programa")
        
#4 Conversión segura:

while True:
    try:
        mensaje = input("Ingresa un número: ")
        
        numero_entero = int(mensaje)
        print(f"la conversión a entero de la cadena es: {numero_entero}")
        
        numero_decimal = float(mensaje)
        print(f"la conversión a decimal de la cadena es: {numero_decimal}")
        break
    except ValueError:
        print("Error: ingresa un número válido")
    except Exception as e:
        print(f"Detalles del error {repr(e)}")
    finally:
        print("Gracias por usar el programa")
        
#5 Try-Except anidado

while True:
    try:
        num_1 = input("Ingresa un número: ")
        num_2 = input("Ingresa otro número: ")
        
        try:
            #intentamos convertir a entero y sumar
            suma = int(num_1) + int(num_2)
        except ValueError:
            #intentamos convertir a flotante y sumar
            suma = float(num_1) + float(num_2)
            
        print(f"La suma de los números es {suma}")
        break
        
    except Exception as e:
        
        print(f"Detalles del error {repr(e)}")
        
    finally:
        print("Gracias por usar el programa")
        

