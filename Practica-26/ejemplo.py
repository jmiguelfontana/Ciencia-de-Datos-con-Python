import pandas as pd

january2019 = pd.read_csv(r'D:\Docs\Cursos\Bcn Activa\Ciencia de Datos con Python\Prácticas\Practica-26\January 2019.csv')
print(january2019)

print(january2019.info())

print(january2019.head(5))

print(january2019.tail(3))

print(january2019['Country'].sort_values(ascending=True).head(5))

january2019['AEliminar'] = "A eliminar"
january2019 = january2019.drop(['AEliminar'], axis=1)
print(january2019)

january2019['AEliminar'] = "A eliminar"
january2019.drop(['AEliminar'], axis=1, inplace=True)
print(january2019)

january2019.sort_values(ascending=True, by='Units')

print(january2019[january2019['Units'] > 100].sort_values(ascending=True,by='IdOrder').head(3))

filtro = january2019['Customer'].str.contains('Industries')
print(january2019[filtro])

filtro = january2019['Customer'].str.contains('C.*')
print(january2019[filtro])

filtro = january2019['Customer'].str.startswith('C')
print(january2019[filtro])

filtro = january2019['Customer'].str.endswith('s')
print(january2019[filtro])

