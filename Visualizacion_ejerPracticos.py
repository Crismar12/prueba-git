#1
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

bebidas = ['Espresso', 'Latte', 'Cappuccino', 'Americano', 'Mocha']
ventas = [120, 200, 150, 180, 100]

#crear la figura y los ejes del gráfico
fig, ax = plt.subplots()
#crear un grágico de barras
ax.bar(bebidas,ventas,color="skyblue",edgecolor="black",linewidth=2)
#etiquetas y titulos
ax.set_ylabel("Cantidad de ventas")
ax.set_title("Ventas de café en una cafetería")
#mostrar el gráfico
plt.show()

#2  #####
# Etiquetas de los grupos
labels = ['Grupo 1', 'Grupo 2', 'Grupo 3', 'Grupo 4']

# Ingresos por género
hombres = [20, 34, 30, 35]
mujeres = [25, 32, 34, 20]

# Posiciones en el eje X
x= np.arange(len(labels))  # Crea un array con las posiciones [0, 1, 2, 3]
width=0.35  # Ancho de las barras

# Crear la figura y los ejes
fig, ax = plt.subplots()

# Dibujar las barras para cada género
rects1 = ax.bar(x - width/2, hombres, width, label= "Hombres", edgecolor= "k", linewidth = 2)
rects2 = ax.bar(x + width/2, mujeres, width, label="Mujeres", edgecolor= "k", linewidth = 2)

# Etiquetas y título
ax.set_ylabel("Ingresos")
ax.set_title("Ingresos por género y grupo")
ax.set_xticks(x) # Define la posición de las etiquetas en el eje X
ax.set_xticklabels(labels) # Coloca las etiquetas en el eje X
ax.legend() # Muestra la leyenda

# Mostrar el gráfico
plt.show()

#3 ##############
# Datos de ventas, marketing y clientes
meses = ["Ene", "Feb", "Mar", "Abr", "May", "Jun"]
ventas = [200, 220, 210, 250, 270, 300] #esto es plata (ingresos)
marketing = [50, 60, 55, 70, 65, 80] #esto es plata (gastos)
clientes = [20, 25, 20, 30, 35, 40] #esto es cantidad de clientes
productos = {'Producto A': 120, 'Producto B': 80, 'Producto C': 100} #cantidad de productos vendidos

# Gráfica de Comparación - Ventas vs Marketing a lo largo del tiempo (meses)
# Esta gráfica de línea muestra la tendencia entre dos variables (marketing y clientes)

plt.subplot(2,2,1)# 2 filas, 2 columnas, posición 1
plt.plot(meses, ventas, label = "Ventas", color = "blue")# Gráfica de línea para ventas, el eje x son los meses y el eje y son las ventas
plt.plot(meses, marketing, label ="Marketing", color = "green")# Gráfica de línea para marketing, el eje x son los meses y el eje y son los gastos de marketing
plt.title("Ventas vs Gastos de Marketing") #title
#etiquetas eje x e y
plt.ylabel("Dólares")
plt.xlabel("Mes")
#legenda
plt.legend()

# Gráfica de Relación - Gasto en Marketing vs Clientes
# Esta gráfica de dispersión muestra la relación entre dos variables (marketing y clientes)
plt.subplot(2,2,2) # 2 filas, 2 columnas, posición 2
sns.scatterplot(x = marketing, y = clientes) # Gráfica de dispersión para marketing y clientes
plt.title("Marketing vs Clientes")
plt.xlabel("Gastos en marketing")
plt.ylabel("Clientes")

# Gráfica de Distribución - Distribución de Clientes
# Esta gráfica de histograma muestra la distribución de una variable (clientes)
plt.subplot(2,2,3) # 2 filas, 2 columnas, posición 3
sns.histplot(clientes, kde =True) # Gráfica de histograma para clientes, kde=True muestra la distribución de la variable
plt.title("Distribución de clientes") #title
#labels
plt.xlabel("Clientes")
plt.ylabel("Frecuencia")

# Gráfica de Composición - Ventas por Producto
# Esta gráfica de pastel muestra la composición de una variable (ventas por producto)
plt.subplot(2,2,4) # 2 filas, 2 columnas, posición 4
plt.pie(productos.values(), labels= productos.keys(), autopct="%1.1f%%")# Gráfica de pastel para ventas por producto, autopct muestra el porcentaje de cada producto
plt.title("Composición de ventas por producto")#title
# Ajustar el layout y mostrar las gráficas
plt.tight_layout()# Ajustar el layout para evitar superposición de gráficas

plt.show()# Mostrar todas las gráficas



