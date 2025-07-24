import pandas as pd
import matplotlib.pyplot as plt

pedidos = pd.read_excel(r'D:\Docs\Cursos\Bcn Activa\Ciencia de Datos con Python\Prácticas\Practica-41\Datos Pedidos.xlsx', 
                        sheet_name='Datos')
pedidos2 = pedidos.groupby('Pais').Importe.sum()
# Convertimos la Serie a DataFrame
pedidos2 = pd.DataFrame(pedidos2).reset_index()
# 5 primeros países que más importe tienen
print(pedidos2.nlargest(5, 'Importe'))
# 5 primeros países que menos importe tienen, ordenado por Importe ascendente
print(pedidos2.nsmallest(5, 'Importe').sort_values(by='Importe', ascending=True))


