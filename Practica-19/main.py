from datetime import date

def transformar(fecha):
    try:
        dia, mes, anno = fecha.split('@')
        return date(int(anno),int(mes),int(dia))
    except ValueError:
        raise ValueError("Formato de fecha incorrecto. Debe ser dd@mm@yyyy")
    
    
entrada = input("Introduce una fecha en formato dd@mm@yyyy: ")  
print(transformar(entrada))