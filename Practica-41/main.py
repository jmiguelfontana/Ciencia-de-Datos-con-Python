import pandas as pd
import matplotlib.pyplot as plt

# Queremos ver en un gráfico circular el % que representa el importe 
# de las 5 primeras ciudades.
pedidos_ciudad = pd.read_excel(r'D:\Docs\Cursos\Bcn Activa\Ciencia de Datos con Python\Prácticas\Practica-41\Datos Pedidos.xlsx', 
                        sheet_name='Datos')
# Group by 'Comercial' and sum 'Importe'
pedidos_ciudad = pedidos_ciudad.groupby('Ciudad').Importe.sum()
pedidos_ciudad = pd.DataFrame(pedidos_ciudad).reset_index()

# Get the top 5 cities by 'Importe'
top_5_cities = pedidos_ciudad.nlargest(5, 'Importe').sort_values(by='Importe').sort_values(by='Importe', ascending=False)
top_rest_cities = pedidos_ciudad.nsmallest(len(pedidos_ciudad) - 5, 'Importe').sort_values(by='Importe', ascending=False)
importe_resto = top_rest_cities.Importe.sum()
resto_ciudades = pd.DataFrame([{'Ciudad': 'Resto ciudades', 'Importe': importe_resto}])
resultado = pd.concat([top_5_cities, resto_ciudades], ignore_index=True)

# Plotting the pie chart
resultado.plot(kind='pie', y='Importe', labels=resultado['Ciudad'], autopct='%1.2f%%', legend=False, figsize=(8, 8))
plt.title('Importe de pedidos por las 5 primeras ciudades')
plt.ylabel('')  # Hide the y-label for better aesthetics
plt.show()
