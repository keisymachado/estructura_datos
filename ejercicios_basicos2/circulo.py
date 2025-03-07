import math

class Circulo:
    def __init__(self, radio: float):
        self.radio = radio

    def calcular_area(self):
        return math.pi * (self.radio ** 2)

    def calcular_circunferencia(self):
        return 2 * math.pi * self.radio


circulo1 = Circulo(7)
print(f"Área del círculo: {circulo1.calcular_area()}")
print(f"Circunferencia del círculo: {circulo1.calcular_circunferencia()}")