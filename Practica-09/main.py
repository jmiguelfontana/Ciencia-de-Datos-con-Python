numeros = [28,15,32,7,44,35,62,76]
numeros.sort()
total=0
for numero in numeros:
    total+=numero
    if total <= 180:
        print(numero)
    else:
        break