import ydata_profiling as yd
import pandas as pd
import yfinance as yf
import pandas_datareader as pda

# Crear DataFrame a partir de un diccionario
bmi_dict = {
    'EMPID': ['E001', 'E002', 'E003', 'E004', 'E005'],
    'Gender': ['M', 'F', 'F', 'M', 'F'],
    'Age': [34, 40, 37, 30, 44],
    'Sales': [123, 114, 135, 139, 117],
    'BMI': ['Normal', 'Overweight', 'Obesity', 'Underweight', 'Underweight']
}
df = pd.DataFrame(bmi_dict)
print (df)

"""
Cuando usas Pandas para crear un DataFrame a partir de un diccionario, lo que haces es 
tomar ese diccionario y convertirlo en una estructura de datos bidimensional, 
organizada en filas y columnas.
-Las claves del diccionario ('EMPID', 'Gender', 'Age', 'Sales', 'BMI') se convierten en los nombres de las columnas del DataFrame.
-Los valores asociados a cada clave son listas. Cada lista representa los datos para esa columna específica.
-Los elementos dentro de cada lista se alinean para formar las filas del DataFrame.
"""


