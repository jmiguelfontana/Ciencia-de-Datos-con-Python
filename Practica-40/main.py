import pandas as pd
import matplotlib.pyplot as plt

pedidos = pd.read_excel(r'D:\Docs\Cursos\Bcn Activa\Ciencia de Datos con Python\Prácticas\Practica-40\Datos Pedidos.xlsx', 
                        sheet_name='Datos')

pedidos_comercial = pedidos.groupby('Comercial').Importe.sum()
pedidos_comercial = pd.DataFrame(pedidos_comercial).reset_index()

#plt.figure(figsize=(9, 5))
#pedidos_comercial.plot(kind='bar', x='Comercial', y='Importe', color='orange')
#plt.title('Importe de pedidos por comercial')
#plt.xlabel('Comerciales')
#plt.ylabel('Importes')
#plt.xticks(rotation=45)
#plt.show()  

#plt.figure(figsize=(6, 6))
#plt.pie(pedidos_comercial['Importe'], labels=pedidos_comercial['Comercial'], autopct='%1.2f%%')
#plt.show()

pedidos["Fecha de Pedido"] = pd.to_datetime(pedidos["Fecha de Pedido"], format='%d/%m/%Y')
pedidos['Mes']  = pedidos['Fecha de Pedido'].dt.month
pedidos['Año']  = pedidos['Fecha de Pedido'].dt.year
pedidos['Día'] = pedidos['Fecha de Pedido'].dt.day
pedidos['Nombre Mes'] = pedidos['Fecha de Pedido'].dt.month_name()

meses_pedidos = pedidos.groupby('Nombre Mes').Importe.sum()
meses_pedidos = pd.DataFrame(meses_pedidos).reset_index()
orden_meses = ['January', 'February', 'March', 'April', 'May', 'June',
               'July', 'August', 'September', 'October', 'November', 'December']
meses_pedidos['Nombre Mes'] = pd.Categorical(meses_pedidos['Nombre Mes'], categories=orden_meses, ordered=True)
meses_pedidos = meses_pedidos.sort_values('Nombre Mes')
print(meses_pedidos)

#plt.figure(figsize=(12, 5))
meses_pedidos.plot(kind='line', x='Nombre Mes', y='Importe', marker='o', markerfacecolor='red', markeredgecolor='black', color='blue')
plt.title('Importe de pedidos por mes')
plt.show()