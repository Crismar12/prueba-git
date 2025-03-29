

#control de flujo IF..ELSE...ELIF: Ejercicio 1:
"""Pide al usuario que ingrese la temperatura actual en grados Celsius.
Si la temperatura es menor o igual a 0, imprime "Hace mucho frío ❄️".
Si está entre 1 y 20 grados, imprime "Está fresco 🌤️". 
Si está entre 21 y 30 grados, imprime "El clima está agradable ☀️". 
Si es mayor de 30, imprime "Hace calor 🔥"""

temperatura = int(input("Ingrese la temperatura actual en grados celcius: "))

if temperatura <= 0:
    print("hace mucho frio")
elif temperatura>=1 and temperatura <=20:
    print("está fresco")
elif temperatura>=21 and temperatura <=30:
    print("el clima está agradable")
else: 
    print("hace calor")
    
#con match
"""Uso de match ... case (requiere Python 3.10 o superior)
Ejercicio 2:
Pide al usuario que ingrese el día de la semana (como texto). Dependiendo del día, muestra un mensaje:
Lunes a Viernes: "Es un día laboral."
Sábado: "¡Es fin de semana! 🎉"
Domingo: "Día de descanso. 😴"
Si el día no es válido, imprime "Día no reconocido."""

dia = input("Ingrese el dia de la semana: ").strip().lower() #se convierte a minúscula para evitar errores

match dia:
 case "lunes" | "martes" | "miércoles" | "miercoles" | "jueves" | "viernes":
  print("Es un día laboral")
 case "sábado" | "sabado": 
     print("¡Es fin de semana!")
 case "domingo":
     print("Día de descanso")
 case _:
     print("Día no reconocido")
     
#ejercicio 3: BUCLES WHILE
import random
numero_secreto = random.randint(0,10)
numero= int(input("¡Adivina el número entre 0 y 10!"))

while (numero != numero_secreto):
    
    numero= int(input("¡Adivina el número entre 0 y 10!"))
    
print("¡Felicidades! Adivinaste el número")

#ejercicio 5:

clave = "marciano1"

while True: 
    clave_ing = input("Ingrese la contraseña (o escriba 'salir' para abandonar): ").strip().lower()
    
    if clave_ing == "salir":
      print ("Sesión finalizada.")
      break #termina el bucle while
    
    if clave_ing == clave:
        print("¡Ingreso exitoso!")
        break
    else:
        print("Contraseña incorrecta. Intenta de nuevo: ")
        
#BLUCES FOR ejer6:

lista_precios = [100,200,300,400,500]

for precio in lista_precios:
    descuento = precio * 0.1 #precio representa cada precio directamente por el bucle for
    precio_final = precio - descuento
    print(f"El precio original era {precio}, con un 10% de descuento es {precio_final}")
    
#ejer 7: 
nombres = ["Ana", "Luis", "Pedro", "María", "José"]

for i in nombres:
    print( f"{i} tiene {len(i)} letras.")
    
#ejer 8: ALTERAR BUCLES

i = 0

while (i<=10):
    i +=1 
    if (i == 5):
        continue
    if (i == 8):
        break
    print(i)
    
#ejer 9: 
   
tareas = ["Lavar los platos", "Hacer la cama", "Estudiar Python", "Sacar la basura"]

for tarea in tareas:
    if (tarea == "Estudiar Python"):
        print("¡Hora de aprender!🚀")
        pass
    print(tarea)  
    
#EJERCICIO INTEGRADOR:

while True:
    
    pregunta1 = input("¿Prefieres actividades en equipo o individuales? (Escribe 'equipo' o 'individual')").strip().lower()
    pregunta2 = input("¿Te gusta más estar al aire libre o en espacios cerrados? (Escribe 'aire libre' o 'espacios cerrados')").strip().lower()
    pregunta3 = input("¿Te gustaría un deporte que requiera mucho esfuerzo físico? (Responde 'si' o 'no')").strip().lower()
    
    if pregunta1 not in ["equipo", "individual"]:
        print("Respuesta no válida en la primera pregunta, por favor intenta de nuevo.")
        
        """Usamos los corchetes [] porque estamos comparando 
        contra un conjunto de palabras exactas, 
        no verificando si la entrada está "incluida dentro de un texto largo"."""
        
        continue
    if pregunta2 not in ["aire libre", "espacios cerrados"]:
        print("Respuesta no válida en la segunda pregunta, por favor intenta de nuevo.")
        continue
    if pregunta3 not in ["si" , "no"]:
        print("Respuesta no válida en la tercera pregunta, por favor intenta de nuevo.")
        continue
    
    if pregunta3 == "si":
        if pregunta1 == "equipo" and pregunta2 == "aire libre":
            print("Recomendación: Fútbol ⚽")
        elif pregunta1 == "equipo" and pregunta2 == "espacios cerrados":
            print("Recomendación: Básquetbol 🏀")
        elif pregunta1 == "individual" and pregunta2 == "aire libre":
            print("Recomendación: Ciclismo 🚴")
        elif pregunta1 == "individual" and pregunta2 == "espacios cerrados":
            print("Recomendación: Natación 🏊")
            
    else: #pregunta3 == "no"
        if pregunta1 == "equipo":
            print("Recomendación: Bolos 🎳")
        else: #pregunta1 == "individual"
            print("Recomendación: Ajedrez ♟️")
            
    break #sale del bucle tras una recomendacion valida
            


