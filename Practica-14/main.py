def nombre(dia):
    dias = ['Lunes','Martes','Miércoles','Jueves','Viernes','Sábado','Domingo']
    if dia >= 1 and dia <= 7:
        return dias[dia-1]
    else:
        return "No válido"
    

entrada = input("Dame un número entre 1 y 7: ")
print(nombre(int(entrada)))