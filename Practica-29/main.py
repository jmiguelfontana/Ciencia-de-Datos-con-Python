import pandas as pd

january2019 = pd.read_csv(r'D:\Docs\Cursos\Bcn Activa\Ciencia de Datos con Python\Prácticas\Practica-29\January 2019.csv')
february2019 = pd.read_csv(r'D:\Docs\Cursos\Bcn Activa\Ciencia de Datos con Python\Prácticas\Practica-29\February 2019.csv')
march2019 = pd.read_csv(r'D:\Docs\Cursos\Bcn Activa\Ciencia de Datos con Python\Prácticas\Practica-29\March 2019.csv')

tresmeses = pd.concat([january2019,february2019,march2019], ignore_index=True)
filtro = tresmeses['Country'].str.contains('Colombia')
resultado = tresmeses[filtro]
total = resultado['Revenue'].sum()

print("Suma de Revenue", round(total * 0.63,2))


