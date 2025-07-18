import pandas as pd

pedidos = pd.read_excel(r'D:\Docs\Cursos\Bcn Activa\Ciencia de Datos con Python\Prácticas\Practica-31\Pedidos.xlsx', sheet_name='Pedidos')
detalles_pedidos = pd.read_excel(r'D:\Docs\Cursos\Bcn Activa\Ciencia de Datos con Python\Prácticas\Practica-31\Detalles Pedidos.xlsx', sheet_name='Detalles Pedidos')

pedidos_completo = pd.merge(pedidos, detalles_pedidos, on='Id. de pedido', how='inner')
print(pedidos_completo)