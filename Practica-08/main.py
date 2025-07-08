lista = [5,-8,145,36,75,62,-20,41,25,19]
lista.sort()
for numero in lista:
    if numero >= 0 and numero <= 120:
        if numero >=0 and numero <= 30:
            print("El", numero, "está comprendido entre 0 y 30")
        elif numero > 30 and numero <= 60:
            print("El", numero, "está comprendido entre 31 y 60") 
        elif numero > 60 and numero <= 90:
            print("El", numero, "está comprendido entre 61 y 90") 
        elif numero > 90 and numero <= 120:
            print("El", numero, "está comprendido entre 91 y 120") 
    else:
       print("El", numero, "está fuera de rango")            
