
import matplotlib.pyplot as plt
import matplotlib as mpl 
import numpy as np

mpl.rcParams.update(mpl.rcParamsDefault) #restablece los valores de mplpara que sns no interfiera en las funciones de matplotlib

"""
1. Gráfico de Barras 📊
Crea un gráfico de barras que muestre la cantidad de frutas vendidas en una tienda:

Frutas: Manzana, Plátano, Uva, Naranja, Sandía
Ventas: 120, 90, 50, 75, 40
📌 Extra: Agrega etiquetas a los ejes y un título.
"""

frutas = ["manzana", "plátano", "uva", "naranja", "sandía"]
ventas = [120, 90, 50, 75, 40]

plt.bar(frutas, ventas)

plt.title("Ventas de frutas", fontsize= 18, fontweight = "bold")
plt.xlabel("Frutas", fontsize = 13)
plt.ylabel("Ventas", fontsize=13)
plt.xticks(rotation = 90, fontsize = 11) #rotation rota los valores del eje indicado
plt.yticks(fontsize=11) 
plt.savefig("ventas-frutas.png", dpi = 200, bbox_inches = "tight")
plt.show()

"""
2. Gráfico de Líneas 📈
Dibuja un gráfico de líneas con los siguientes datos:

X: números del 0 al 10
Y: el triple de cada número en X
📌 Extra: Usa un color diferente y agrega marcadores en cada punto.
"""
X = np.arange(0,11)
Y = X *3

plt.plot(X, Y, color="red", linewidth=2, marker="*", linestyle="-")
plt.xlabel("X", fontsize=13, fontweight = "bold")
plt.ylabel("Y", fontsize = 13, fontweight = "bold")
plt.xticks(fontsize=11)
plt.yticks(fontsize=11)
plt.grid(True) #cuadricula para visualizar mejor
plt.show()

"""
3. Gráfico de Dispersión 🔵
Genera un diagrama de dispersión con datos aleatorios:

X: números del 1 al 50 (de 5 en 5)
Y: valores aleatorios con una media de 30 y una desviación estándar de 5
📌 Extra: Cambia el color y tamaño de los puntos.
"""
arr1 = np.arange(1, 51, 5)
arr2= np.random.normal(30, 5, len(arr1))

plt.scatter(arr1, arr2, color = "pink", s = 100, edgecolors= "black") # s controla el tamaño de los puntos
#edgecolors define el color del borde de los puntos en plt.scatter()
plt.title("diagrama de dispersion", fontsize= 18, fontweight="bold")
plt.xlabel("x", fontsize= 13, fontweight="bold")
plt.ylabel("y", fontsize= 13, fontweight="bold")
plt.xticks(fontsize=11)
plt.yticks(fontsize= 11)
plt.show()

"""
4. Histograma 📊
Genera un histograma con 500 valores distribuidos normalmente con:
Media = 5
Desviación estándar = 2
📌 Extra: Usa 15 bins y cambia el color del histograma
"""
arr3 = np.random.normal(5,2, 500)

plt.hist(arr3, bins = 15, color = "green")
plt.title("histograma", fontsize= 18, fontweight = "bold")
plt.xlabel("x", fontsize =13)
plt.ylabel("conteo", fontsize = 13)
plt.xticks(fontsize=11)
plt.yticks(fontsize=11)
plt.show()

"""
5. Gráfico de Pastel 🍰
Crea un gráfico de pastel con la siguiente distribución de calificaciones:

Aprobados: 60
Reprobados: 25
Retirados: 15
📌 Extra: Usa porcentajes y cambia los colores.
"""
# Datos de la distribución de calificaciones
estado = ["Aprobados", "Reprobados", "Retirados"]
cantidad = [60, 25, 15]
colores = ["#4CAF50", "#FF9800", "#F44336"]  # Verde, Naranja, Rojo

# Crear una figura de tamaño 6x6 pulgadas para mantener el gráfico circular
plt.figure(figsize=(6, 6))  

# Crear el gráfico de pastel con etiquetas, colores y porcentajes
plt.pie(
    x=cantidad,                # Datos numéricos (valores de cada categoría)
    labels=estado,             # Etiquetas de cada sector
    colors=colores,            # Colores personalizados para cada categoría
    textprops={'size': 13, 'color': 'white'},  # Tamaño y color del texto dentro del gráfico
    autopct='%1.1f%%',         # Mostrar porcentajes con 1 decimal
    startangle=90,             # Girar el gráfico para que empiece desde arriba
    wedgeprops={"edgecolor": "black"}  # Borde negro para mejor visibilidad
)

# Agregar una leyenda fuera del gráfico (esquina superior izquierda)
plt.legend(title="Estado", bbox_to_anchor=(1, 1), loc="upper left")

# Título del gráfico, centrado y con formato en negrita
plt.title("Distribución de Alumnos", fontsize=18, fontweight="bold", loc="center")

# Mostrar el gráfico
plt.show()
