import pandas as pd

pedidos = pd.read_excel(r'D:\Docs\Cursos\Bcn Activa\Ciencia de Datos con Python\Prácticas\Practica-32\Pedidos.xlsx', sheet_name='Pedidos')
comerciales = pd.read_excel(r'D:\Docs\Cursos\Bcn Activa\Ciencia de Datos con Python\Prácticas\Practica-32\Comerciales.xlsx', sheet_name='Comerciales')

pedidos_completo = pd.merge(pedidos, comerciales, on='Id. de Comercial', how='inner')