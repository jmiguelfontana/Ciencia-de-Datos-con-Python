from datetime import datetime, timedelta

fechas = ['30/06/2024','15/7/2023','22/08/2025']
dias = [10,20,16]
horas = [7,12,8]
minutos = [20,12,50]

intAux = 0
for intAux in range(3):
   dia, mes, anno = fechas[intAux].split('/')
   
   dtFecha1 = datetime(int(anno), int(mes), int(dia))
   dlDiferencia = timedelta(days=dias[intAux], hours=horas[intAux], minutes=minutos[intAux])
   dtFecha2 = dtFecha1 + dlDiferencia
   
   print("Fecha", dtFecha1.strftime("%d/%m/%Y %H:%M"), ">", dtFecha2.strftime("%d/%m/%Y %H:%M"))

