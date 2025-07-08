from datetime import date

fecha1 = date(2024,10,11)
fecha2 = date.today()

dias = (fecha2 - fecha1).days

if dias > 180:
    print("Distancia superior a 6 meses")
else:
    print("Distancia inferior o igual a 6 meses")    
