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
dfFinlandia = fetch_data(conexion, "SELECT TOP 50 * FROM Pedidos WHERE PaísDestinatario IN('Finlandia','Suiza')")
print(dfFinlandia.IdPedido.count())
conexion.close()