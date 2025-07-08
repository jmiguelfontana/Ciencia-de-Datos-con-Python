class Vehiculo:
    def __init__(self, marca, modelo, anno, velocidad):
        self.marca = marca
        self.modelo = modelo
        self.anno = anno
        self.velocidad = velocidad

    def descripcion(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.anno}, Velocidad: {self.velocidad}")

    def velocidad_maxima(self):
        print("Velocidad máxima:", self.velocidad - 14)

