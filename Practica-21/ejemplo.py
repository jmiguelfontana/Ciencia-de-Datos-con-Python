import pandas as pd

semana = pd.Series(['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo'])
semana.info()

valores = pd.Series([True, False, True, False, True, False, True])
valores.info()

numeros = pd.Series([1, 2, 3, 4, 5, 6, 7])
numeros.info()
print("La suma es:",numeros.sum())
print("El promedio es:",numeros.mean())
print("El máximo es:",numeros.max())
print("El mínimo es:",numeros.min())
print("La desviación estándar es:",numeros.std())
print("La desviación estándar es:",round(numeros.std(),3))
print("El número de elementos es:",numeros.count())
print("La suma acumulada es:",numeros.cumsum())
print("La varianza es:",numeros.var())

print(numeros * 2)

def suma10(x):
    return x + 10
numeros2 = numeros.apply(suma10)
print(numeros2)

numeros3=pd.Series([9, 2, 5, 8, 5, 6, 7])
numeros3 = numeros3.sort_values(ascending=True, ignore_index=True)
print(numeros3)

numeros4 = pd.Series([9, 2, 5, 8, 5, 6, 7])
print(numeros4[numeros4 > 5].sort_values(ascending=True, ignore_index=True))

