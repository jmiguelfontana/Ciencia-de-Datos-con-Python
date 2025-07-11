import pandas as pd

srNumerosVip = pd.Series([34,124,81,9,27,81,34,63,75,44,18,67,22,63,25,63])
srNumerosVip40 = srNumerosVip[srNumerosVip > 40].sort_values(ascending=False, ignore_index=True)

#print(srNumerosVip40)

def restar2(x):
    if x > 70:
        return x - 2
    else:
        return x + 2

srNumerosVip40 = srNumerosVip40.apply(restar2)
print("Varianza",srNumerosVip40.var())
print("Desviación",round(srNumerosVip40.std(),2))
print("Suma acumulada",srNumerosVip40.cumsum())