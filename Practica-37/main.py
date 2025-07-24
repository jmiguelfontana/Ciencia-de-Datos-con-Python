import pyodbc
import pandas as pd

def connect_to_database():
    try:
        connection = pyodbc.connect(
            'Driver={SQL Server};'
            'Server=localhost;'
            'Database=Neptuno;'
            'UID=sa;'
            'PWD=AH64Sqlserver@!;'
        )
        print("Connection successful")
        return connection
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None

def fetch_data(connection, sql_query):
    try:
        df = pd.read_sql(sql_query, connection)
        print("Data fetched successfully")
        return df
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

conexion = connect_to_database() 
dfPedidos = fetch_data(conexion, "SELECT * " \
"FROM Pedidos p, Detalles_de_pedidos dp, Productos pr, Categorías ca " \
"WHERE p.IdPedido = dp.IdPedido and dp.IdProducto = pr.IdProducto and pr.IdCategoría = ca.IdCategoría")
conexion.close()

numeroFilas = len(dfPedidos)
for i in range(numeroFilas):
    if dfPedidos.iloc[i,31] == 'Bebidas':
        dfPedidos.iloc[i,31] = 'Beverages'
    elif dfPedidos.iloc[i,31] == 'Pescado/Marisco':
        dfPedidos.iloc[i,31] = 'Seafood'

print(dfPedidos)
dfPedidos50 = dfPedidos[100:150]  
dfPedidos50.to_excel(r'.\practica-37.xlsx', sheet_name='Datos', index=False) 


