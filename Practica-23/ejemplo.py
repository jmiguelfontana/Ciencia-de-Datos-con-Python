import pandas as pd

def lafuncion(x):
    return x + 10

def main():
    pedidos = pd.DataFrame([
        {"Cliente": "Comercial Suministros", "Cantidad": 10, "Precio": 100.0},
        {"Cliente": "Distribuciones Alimentarias", "Cantidad": 5, "Precio": 50.0},
        {"Cliente": "Servicios Informáticos", "Cantidad": 20, "Precio": 200.0},
        {"Cliente": "Comercial Suministros", "Cantidad": 15, "Precio": 150.0},
        {"Cliente": "Servicios Informáticos", "Cantidad": 10, "Precio": 100.0}
    ])
    print(pedidos)

    print(pedidos.head(2))

    print(pedidos.tail(2))

    print(pedidos[['Cliente','Cantidad']])

    pedidos2 = pedidos[['Cliente','Precio']]
    print(pedidos2)

    pedidos['Comercial'] = 'Manolo García'
    print(pedidos)

    pedidos['Cantidad2'] = pedidos['Cantidad'].apply(lafuncion)
    print(pedidos)

    pedidos['Precio2'] = pedidos['Precio'] * 1.1  # +10%
    print(pedidos)

    pedidos['Importe'] = pedidos['Cantidad'] * pedidos['Precio']

main()