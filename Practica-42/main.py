import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos
pedidos_comercial = pd.read_excel(
    r'D:\Docs\Cursos\Bcn Activa\Ciencia de Datos con Python\Prácticas\Practica-42\Datos Pedidos.xlsx', 
    sheet_name='Datos'
)

# Agrupar por Comercial y País, sumar el Importe
pedidos_comercial = pedidos_comercial.groupby(['Comercial', 'Pais']).Importe.sum().reset_index()

# Filtrar por Alemania y seleccionar los 4 comerciales con menor importe
pedidos_comercial_alemania = pedidos_comercial[pedidos_comercial['Pais'] == 'Alemania']
pedidos_comercial_alemania = pedidos_comercial_alemania.nsmallest(4, 'Importe')
print(pedidos_comercial_alemania)

# Gráfica
pedidos_comercial_alemania.plot(kind='bar', x='Comercial', y='Importe', color=['green', 'blue', 'purple', 'black'], legend=False, figsize=(10, 6))
plt.title('4 Comerciales con menos importe en Alemania')
plt.xlabel('Comercial')
plt.ylabel('Importe')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
