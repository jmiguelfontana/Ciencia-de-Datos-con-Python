import pandas as pd
import matplotlib.pyplot as plt

# Queremos ver en un gráfico circular el % que representa las 3 categorías que 
# menos importe tienen con respecto al total.
pedidos_categoria = pd.read_excel(r'D:\Docs\Cursos\Bcn Activa\Ciencia de Datos con Python\Prácticas\Practica-41\Datos Pedidos.xlsx', 
                        sheet_name='Datos')
# Group by 'Comercial' and sum 'Importe'
pedidos_categoria = pedidos_categoria.groupby('Categoria').Importe.sum()
pedidos_categoria = pd.DataFrame(pedidos_categoria).reset_index()

# Get the top 5 cities by 'Importe'
low_3_categories = pedidos_categoria.nsmallest(3, 'Importe').sort_values(by='Importe').sort_values(by='Importe', ascending=False)
top_rest_categories = pedidos_categoria.nlargest(len(pedidos_categoria) - 3, 'Importe').sort_values(by='Importe', ascending=False)
importe_resto = top_rest_categories.Importe.sum()
resto_categorias = pd.DataFrame([{'Categoria': 'Resto categorias', 'Importe': importe_resto}])
resultado = pd.concat([low_3_categories, resto_categorias], ignore_index=True)

# Plotting the pie chart
resultado.plot(kind='pie', y='Importe', labels=resultado['Categoria'], autopct='%1.2f%%', legend=False, figsize=(8, 8))
plt.title('Importe de pedidos por las 3 últimas categorías')
plt.ylabel('')  # Hide the y-label for better aesthetics
plt.show()
