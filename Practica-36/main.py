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
dfPedidos = fetch_data(conexion, "SELECT ca.NombreCategoría, SUM(dp.PrecioUnidad * dp.Cantidad) as Importe " \
"FROM Pedidos p, Detalles_de_pedidos dp, Productos pr, Categorías ca " \
"WHERE p.IdPedido = dp.IdPedido and dp.IdProducto = pr.IdProducto and pr.IdCategoría = ca.IdCategoría " \
"GROUP BY ca.NombreCategoría")
print(dfPedidos)
print(dfPedidos.Importe.sum())
conexion.close()