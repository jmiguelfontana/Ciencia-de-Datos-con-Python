def comparar(a,b):
    if a > b:
        return str(a) +" es mayor que " + str(b)
    elif a < b:
        return str(a) + " es menor que " + str(b)
    else:
        return str(a) + " y " + str(b) + " son iguales"
    

print(comparar(2,2))