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
dfPedidos = fetch_data(conexion, "select * from Pedidos")
conexion.close()

print(dfPedidos.iloc[0,0])

print(dfPedidos.iloc[20:30])

print(dfPedidos.info() )
print(dfPedidos.iloc[20:30, [2,4,8]])

# Clon de todos los registros pero solo de las columnas 2, 4 y 8
dfPedidos2 = dfPedidos.iloc[:, [2,4,8]]
print(dfPedidos2)

dfPedidos.iloc[0,1] = 'Hola'
print(dfPedidos.iloc[0,1])

numeroFilas = len(dfPedidos)
numeroColumnas = len(dfPedidos.columns)
print(numeroFilas, numeroColumnas)
for i in range(numeroFilas):
    print(dfPedidos.iloc[i,0], dfPedidos.iloc[i, 1], dfPedidos.iloc[i, 2])




