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

print(pyodbc.drivers())
conexion = connect_to_database()
dfFrancia = fetch_data(conexion, "SELECT IdPedido FROM Pedidos WHERE PaísDestinatario = 'Francia'")
dfPedidos = fetch_data(conexion, "SELECT IdPedido, Cantidad * PrecioUnidad as Importe FROM Detalles_de_pedidos dp")
df = dfFrancia.merge(dfPedidos, on='IdPedido', how='inner')
print(df.Importe.sum())
conexion.close()