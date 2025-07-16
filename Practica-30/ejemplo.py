import pandas as pd

agosto2014 = pd.read_excel(r'D:\Docs\Cursos\Bcn Activa\Ciencia de Datos con Python\Prácticas\Practica-30\VentasGroucery_Meses.xlsx', sheet_name='Ventas Agosto 2014')
print(agosto2014)

agosto2014['Amount'] = agosto2014['Unit Price'] * agosto2014['Quantity']
print(agosto2014)

print(agosto2014.groupby(['Ship Country']).Amount.sum())
# Suma amount por país y ciudad
print(agosto2014.groupby(['Ship Country','Ship City']).Amount.sum())
# Promedio por pais
print(agosto2014.groupby(['Ship Country'])['Unit Price'].mean())
# LA cantidad de pedidods por categoría
print(agosto2014.groupby(['Category'])['Order ID'].count())

# Guardar la agrupación en un objeto
importe_pais = agosto2014.groupby(['Ship Country']).Amount.sum()
dfImportePais  = pd.DataFrame(importe_pais).reset_index()
print(dfImportePais)

fichero = r'.\prueba.csv'
dfImportePais.to_csv(fichero,sep=';', index=True)
