import pandas as pd

january2019 = pd.read_csv(r'D:\Docs\Cursos\Bcn Activa\Ciencia de Datos con Python\Prácticas\Practica-29\January 2019.csv')
print(january2019['IdOrder'].count())
february2019 = pd.read_csv(r'D:\Docs\Cursos\Bcn Activa\Ciencia de Datos con Python\Prácticas\Practica-29\February 2019.csv')
print(february2019['IdOrder'].count())
march2019 = pd.read_csv(r'D:\Docs\Cursos\Bcn Activa\Ciencia de Datos con Python\Prácticas\Practica-29\March 2019.csv')
print(march2019['IdOrder'].count())

tresmeses = pd.concat([january2019,february2019,march2019], ignore_index=True)
tresmesesC = tresmeses[tresmeses['Country'] == 'Colombia'].copy()
tresmesesNC = tresmeses[tresmeses['Country'] != 'Colombia'].copy()

tresmesesC['Revenue'] = tresmesesC['Revenue'] * (1-0.0563)
resultado = pd.concat([tresmesesC,tresmesesNC], ignore_index=True)
print(round(resultado['Revenue'].sum(),2))