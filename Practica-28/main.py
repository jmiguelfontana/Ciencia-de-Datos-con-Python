import pandas as pd

january2019 = pd.read_csv(r'D:\Docs\Cursos\Bcn Activa\Ciencia de Datos con Python\Prácticas\Practica-28\January 2019.csv')
february2019 = pd.read_csv(r'D:\Docs\Cursos\Bcn Activa\Ciencia de Datos con Python\Prácticas\Practica-28\February 2019.csv')

dosmeses = pd.concat([january2019,february2019], ignore_index=True)
filtro = dosmeses['Country'].str.contains('Canada')

print(dosmeses[filtro].head(10))