import pandas as pd

def incrementar(x):
    if x > 40:
        return x * 1.25
    else:
        return x
   
def main():
    pedidos = pd.DataFrame([
        {"Cliente": "Comercial Suministros", "Cantidad": 45, "Precio": 100.0},
        {"Cliente": "Distribuciones Alimentarias", "Cantidad": 5, "Precio": 50.0},
        {"Cliente": "Servicios Informáticos", "Cantidad": 20, "Precio": 200.0},
        {"Cliente": "Comercial Suministros", "Cantidad": 55, "Precio": 150.0},
        {"Cliente": "Servicios Informáticos", "Cantidad": 10, "Precio": 100.0}
    ])
    print(pedidos)
    pedidos['Diferencia Cantidad'] = pedidos['Cantidad'].max() - pedidos['Cantidad']
    print(pedidos)

main()