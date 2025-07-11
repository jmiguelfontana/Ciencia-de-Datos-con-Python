import pandas as pd

def restar(x):
    if x < 50:
        return x - 3
    else:
        return x
    
vip = [18,35,78,44,63,24,88,125,7,53]
srVip = pd.Series(vip)
srVip2 = srVip.apply(restar)
print("Suma antes",srVip.sum(),"->", "Suma después",srVip2.sum())
print("Diferencia",srVip.sum() - srVip2.sum())





