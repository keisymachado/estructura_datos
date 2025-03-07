class Rectangulo:
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)


rectangulo1 = Rectangulo(5, 10)
print(f"Área del rectángulo: {rectangulo1.calcular_area()}")
print(f"Perímetro del rectángulo: {rectangulo1.calcular_perimetro()}")