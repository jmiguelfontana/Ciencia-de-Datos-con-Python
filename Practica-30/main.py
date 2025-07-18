import pandas as pd

agosto = pd.read_excel(r'D:\Docs\Cursos\Bcn Activa\Ciencia de Datos con Python\Prácticas\Practica-30\VentasGroucery_Meses.xlsx', sheet_name='Ventas Agosto 2014')
septiembre = pd.read_excel(r'D:\Docs\Cursos\Bcn Activa\Ciencia de Datos con Python\Prácticas\Practica-30\VentasGroucery_Meses.xlsx', sheet_name='Ventas Septiembre 2014')
octubre = pd.read_excel(r'D:\Docs\Cursos\Bcn Activa\Ciencia de Datos con Python\Prácticas\Practica-30\VentasGroucery_Meses.xlsx', sheet_name='Ventas Octubre 2014')

trimestre = pd.concat([agosto,septiembre,octubre], ignore_index=True)
trimestre_fichero = trimestre[trimestre['Quantity']>10]
trimestre_fichero['Amount'] = trimestre_fichero['Unit Price'] * trimestre_fichero['Quantity']
resultado = trimestre_fichero.groupby(['Ship Country','Category']).Amount.sum()

resultado = pd.DataFrame(resultado).reset_index()
#resultado.to_csv(r'.\prueba2.csv',sep=';')
resultado.to_excel(r'.\prueba2.xlsx',sheet_name='Hoja 1',header=True,index=False)
print(resultado)