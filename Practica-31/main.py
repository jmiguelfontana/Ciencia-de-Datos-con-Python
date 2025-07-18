import pandas as pd

pedidos = pd.read_excel(r'D:\Docs\Cursos\Bcn Activa\Ciencia de Datos con Python\Prácticas\Practica-31\Pedidos.xlsx', sheet_name='Pedidos')
detalles_pedidos = pd.read_excel(r'D:\Docs\Cursos\Bcn Activa\Ciencia de Datos con Python\Prácticas\Practica-31\Detalles Pedidos.xlsx', sheet_name='Detalles Pedidos')
productos = pd.read_excel(r'D:\Docs\Cursos\Bcn Activa\Ciencia de Datos con Python\Prácticas\Practica-31\Productos.xlsx', sheet_name='Productos')
categorias = pd.read_excel(r'D:\Docs\Cursos\Bcn Activa\Ciencia de Datos con Python\Prácticas\Practica-31\Categorías.xlsx', sheet_name='Categorías')
comerciales = pd.read_excel(r'D:\Docs\Cursos\Bcn Activa\Ciencia de Datos con Python\Prácticas\Practica-31\Comerciales.xlsx', sheet_name='Comerciales')

pedidos_completo = pd.merge(pedidos, detalles_pedidos, on='Id. de pedido', how='inner')
pedidos_completo = pedidos_completo.merge(productos, left_on='Producto', right_on='Nombre de producto', how='inner')
pedidos_completo = pedidos_completo.merge(categorias, left_on='Categoría', right_on='Nombre de categoría', how='inner')
pedidos_completo['Importe'] = pedidos_completo['Precio por unidad'] * pedidos_completo['Cantidad']

importe_categoria = pedidos_completo.groupby('Nombre de categoría')['Importe'].sum()
importe_categoria = pd.DataFrame(importe_categoria).reset_index()

pedidos_categoria = pedidos_completo.groupby('Nombre de categoría')['Importe'].count()
pedidos_categoria = pd.DataFrame(pedidos_categoria).reset_index()

promedio_categoria = pedidos_completo.groupby('Nombre de categoría')['Cantidad'].mean()
promedio_categoria = pd.DataFrame(promedio_categoria).reset_index()

agrupado = pd.merge(importe_categoria, pedidos_categoria, on="Nombre de categoría")
agrupado = pd.merge(agrupado, promedio_categoria, on="Nombre de categoría")

print(agrupado)
agrupado.to_excel(r'.\practica-31.xlsx',sheet_name='Hoja 1',header=True,index=False)