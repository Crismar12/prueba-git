"""
1️⃣ Comparación ➔ Estático ➔ 1 Variable
📌 Ejemplo: Ventas de café en una cafetería
📊 Gráfico de barras para mostrar las ventas de diferentes bebidas
"""
import numpy as np
import matplotlib.pyplot as plt


# Datos: bebidas y su cantidad de ventas
bebidas = ['Espresso', 'Latte', 'Cappuccino', 'Americano', 'Mocha']
ventas = [120, 200, 150, 180, 100]

# Crear la figura y los ejes del gráfico
fig, ax = plt.subplots()

# Crear un gráfico de barras
ax.bar(bebidas, ventas, color='skyblue', edgecolor='k', linewidth=2)

# Etiquetas y título
ax.set_ylabel('Cantidad de Ventas')
ax.set_title('Ventas de café en una cafetería')

# Mostrar el gráfico
plt.show()

"""
2️⃣ Comparación ➔ Estático ➔ 2 Variables
📌 Ejemplo: Ingresos por grupo y género
📊 Gráfico de barras agrupadas
"""
# Etiquetas de los grupos
labels = ['Grupo 1', 'Grupo 2', 'Grupo 3', 'Grupo 4']

# Ingresos por género
hombres = [20, 34, 30, 35]
mujeres = [25, 32, 34, 20]

# Posiciones en el eje X
x = np.arange(len(labels))  # Crea un array con las posiciones [0, 1, 2, 3]
width = 0.35  # Ancho de las barras

# Crear la figura y los ejes
fig, ax = plt.subplots()

# Dibujar las barras para cada género
rects1 = ax.bar(x - width/2, hombres, width, label='Hombres', edgecolor='k', linewidth=2)
rects2 = ax.bar(x + width/2, mujeres, width, label='Mujeres', edgecolor='k', linewidth=2)

# Etiquetas y título
ax.set_ylabel('Ingresos')
ax.set_title('Ingresos por grupo y género')
ax.set_xticks(x)  # Define la posición de las etiquetas en el eje X
ax.set_xticklabels(labels)  # Coloca las etiquetas en el eje X
ax.legend()  # Muestra la leyenda

# Mostrar el gráfico
plt.show()

# Explicación: 
#np.arange(len(labels)): Genera posiciones [0, 1, 2, 3] para los grupos.
#ax.bar(x - width/2, hombres, width): Desplaza las barras de hombres a la izquierda.
#ax.bar(x + width/2, mujeres, width): Desplaza las barras de mujeres a la derecha.
#set_xticks() y set_xticklabels(): Configuran las etiquetas en el eje X.

"""
📌 Algunos colores comunes en Matplotlib:

'b' → Azul (blue)
'g' → Verde (green)
'r' → Rojo (red)
'c' → Cyan
'm' → Magenta
'y' → Amarillo (yellow)
'k' → Negro (black)
'w' → Blanco (white)
""" 