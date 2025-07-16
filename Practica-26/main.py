import pandas as pd

january2019 = pd.read_csv(r'D:\Docs\Cursos\Bcn Activa\Ciencia de Datos con Python\Prácticas\Practica-26\January 2019.csv')
filtro = january2019['Customer'].str.contains('Systems')
clonado = january2019[filtro].sort_values(ascending=True,by='Customer')

print(clonado)