import numpy as np
from scipy.stats import linregress
import pandas as pd

#Calcular cuantas motocicletas tendré en el año 2030

# Creación de un modelo predictivo, con la librería scipy.
motos = pd.read_csv(r'D:\Docs\Cursos\Bcn Activa\Ciencia de Datos con Python\Prácticas\Practica-43\Motocicletas gasolina.csv')
print(motos)
# Asignar a la variable x (la variable dependiente) la columna 'Año'
x = motos['Año']
# Asignar a la variable y (la variable independiente) la columna 'Unidades'
y = motos['Unidades']
# Calcular la regresión lineal
slope, intercept, r_value, p_value, std_err = linregress(x, y)
# Mostrar los resultados
print(f"Pendiente: {slope}")
print(f"Intersección: {intercept}")
print(f"Valor R: {r_value}")    
print(f"Valor P: {p_value}")
print(f"Error estándar: {std_err}")
# Calcular la predicción para un valor de x
x_pred = 2030  # Año 2030
y_pred = slope * x_pred + intercept
print(f"Predicción para el año {x_pred}: {round(y_pred,2)} motos")

# Gráfico de la regresión lineal
import matplotlib.pyplot as plt
plt.scatter(x, y, color='blue', label='Datos')
plt.plot(x, slope * x + intercept, color='red', label='Regresión lineal')
plt.xlabel('Año')
plt.ylabel('Unidades')
plt.title('Regresión Lineal de Motocicletas')
plt.legend()
plt.show()