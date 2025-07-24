import numpy as np
from scipy.stats import linregress
import pandas as pd

# Creación de un modelo predictivo, con la librería scipy.
habitantes = pd.read_csv(r'D:\Docs\Cursos\Bcn Activa\Ciencia de Datos con Python\Prácticas\Practica-43\Datos Accidentes localidad.csv')
print(habitantes)
# Asignar a la variable y (la variable dependiente) la columna 'Num. Accidentes'
y = habitantes['Num. Accidentes']
# Asignar a la variable x (la variable independiente) la columna 'Habitantes'
x = habitantes['Habitantes']
# Calcular la regresión lineal
slope, intercept, r_value, p_value, std_err = linregress(x, y)
# Mostrar los resultados
print(f"Pendiente: {slope}")
print(f"Intersección: {intercept}")
print(f"Valor R: {r_value}")    
print(f"Valor P: {p_value}")
print(f"Error estándar: {std_err}")
# Calcular la predicción para un valor de x
x_pred = 114000  # Por ejemplo, 100,000 habitantes
y_pred = slope * x_pred + intercept
print(f"Predicción para {x_pred} habitantes: {round(y_pred,2)} accidentes")
