import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

# Cargar CSV
motos = pd.read_csv(r'D:\Docs\Cursos\Bcn Activa\Ciencia de Datos con Python\Prácticas\Practica-43\Motocicletas gasolina.csv')

# Extraer variables
X = motos[['Año']] # Asegúrate de usar doble corchete para obtener un DataFrame
y = motos['Unidades']

# Crear y entrenar el modelo
modelo = LinearRegression()
modelo.fit(X, y)

# Predecir para 2030
x_pred = [[2030]]
y_pred = modelo.predict(x_pred)
print(f"Predicción para el año 2030: {int(y_pred[0])} motos")
# Mostrar coeficientes
print(f"Pendiente: {modelo.coef_[0]}")
print(f"Intersección: {modelo.intercept_}")
print(f"R^2: {modelo.score(X, y)}")


# Gráfico
plt.figure(figsize=(8,5))
plt.scatter(X, y, color='blue', label='Datos reales')
plt.plot(X, modelo.predict(X), color='red', label='Regresión lineal')
plt.scatter(2030, y_pred, color='green', marker='x', s=100, label='Predicción 2030')
plt.text(2030 + 0.3, y_pred[0], f'{int(y_pred[0])}', color='green')

plt.xlabel('Año')
plt.ylabel('Unidades')
plt.title('Predicción de Motocicletas (Regresión Lineal)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
