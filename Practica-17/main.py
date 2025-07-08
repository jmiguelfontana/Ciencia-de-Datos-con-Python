from rectangulo import Rectangulo

nuevo_rectangulo = Rectangulo(5, 10)
print(f"Área del rectángulo: {nuevo_rectangulo.area()}")
print(f"Perímetro del rectángulo: {nuevo_rectangulo.perimetro()}")

nuevo_rectangulo2 = Rectangulo(15, 30)
print(f"Área del rectángulo: {nuevo_rectangulo2.area()}")
print(f"Perímetro del rectángulo: {nuevo_rectangulo2.perimetro()}")

nuevo_rectangulo3 = Rectangulo(23, 74)
nuevo_rectangulo3.__setattr__('base', 50)
nuevo_rectangulo3.__setattr__('altura', 100)
print(f"Área del rectángulo: {nuevo_rectangulo3.area()}")
print(f"Perímetro del rectángulo: {nuevo_rectangulo3.perimetro()}")