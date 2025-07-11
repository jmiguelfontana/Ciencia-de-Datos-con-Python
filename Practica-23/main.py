import pandas as pd

def main():
    pedidos = pd.DataFrame([
        {"Cliente": "Comercial Suministros", "Cantidad": 10, "Precio": 100.0},
        {"Cliente": "Distribuciones Alimentarias", "Cantidad": 5, "Precio": 50.0},
        {"Cliente": "Servicios Informáticos", "Cantidad": 20, "Precio": 200.0},
        {"Cliente": "Comercial Suministros", "Cantidad": 15, "Precio": 150.0},
        {"Cliente": "Servicios Informáticos", "Cantidad": 10, "Precio": 100.0}
    ])
    print(pedidos)
    pedidos['Precio Unidad'] = pedidos['Precio'] * 1.15
    print(pedidos)

main()