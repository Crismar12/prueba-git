#nota: si quieres guardar en una nueva variable el valor de una función, necesitas usar un return
#sino lo haces, cuando llames a la variable, devolvera none

"""def producto(a,b):
  print(f"La multiplicacion es {a*b}")
  producto(4,4)

resul = producto(5,5)

print(resul)

---> La multiplicacion es 16
     La multiplicacion es 25
     None"""

#EJERCICIO 1: CÁLCULO DE PROPINA
"""
def propina(cuenta, porcen=10):
    total_cuenta = cuenta + (cuenta * porcen / 100)
    return total_cuenta

cuenta = float(input("Ingrese el total de la cuenta: "))

while True:
    porcentaje_input = input("Escriba solo el número del porcentaje de propina que desea dar (por defecto es 10%): ").strip()

    # Si el usuario no ingresa nada, se usa el valor por defecto (10%)
    if porcentaje_input == "":
        total_pagar = propina(cuenta)
        break
    else:
        try:
            porcen = float(porcentaje_input)
            if 10 <= porcen <= 100:
                total_pagar = propina(cuenta, porcen)
                break
            else:
                print("Cantidad ingresada incorrectamente. Recuerde escribir solo números en un rango de 10 a 100.")
        except ValueError:
            print("Entrada no válida. Por favor, escriba un número válido.")

print(f"El total a pagar, incluyendo propina, es: {total_pagar:.2f}") """


#EJERCICIO 3: DECORADOR SALUDO

def saludar_usuario(nombre):
    print(f"Hola, {nombre}")
    
def decorador_saludo(funcion_original):
    def envoltura(nombre):
        print("Inicio del proceso...")
        funcion_original(nombre)
        print("Fin del saludo")
    return envoltura
    
@decorador_saludo
def saludar_usuario(nombre):
    print(f"Hola, {nombre}")
    
saludar_usuario("Francis")

#EJERCICIO 4: RETIRO DE MONTO Y CONSULTA DE SALDO
saldo = 1000

def monstrar_saldo():
    global saldo
    print(f"Tu saldo actual es {saldo:.2f}")
    
    
def retirar_dinero(monto):
    global saldo
    
    if monto <= 0:
        print("El monto debe ser mayor a 0")
        
    elif monto > saldo:
        print(f"Saldo insuficiente, tu saldo actual es {saldo:.2f}")
        
    else:
        saldo -=monto
        print(f"Ha retirado {monto:.2f} exitosamente")
        
monstrar_saldo()

retirar_dinero(200)

retirar_dinero(-8)

retirar_dinero(900)


        
        