import pandas as pd
from ydata_profiling import ProfileReport

# Crear un DataFrame de prueba
data = pd.DataFrame({
    "A": [1, 2, 3, 4, 5],
    "B": [3, 3, 3, 3, 3],
    "C": [5, 4, 3, 2, 1]
})

# Generar el reporte
profile = ProfileReport(data, title="Reporte de Datos", explorative=True)

# Guardar el reporte en un archivo HTML
profile.to_file("reporte.html")
