class Producto:
    def __init__(self, nombre: str, precio: float, cantidad_disponible: int):
        self.nombre = nombre
        self.precio = precio
        self.cantidad_disponible = cantidad_disponible

    def calcular_total(self, cantidad: int):
        if cantidad <= self.cantidad_disponible:
            return cantidad * self.precio
        else:
            return "No hay suficiente stock."


producto1 = Producto("Laptop", 1200.0, 10)
print(f"Costo total de 3 laptops: {producto1.calcular_total(3)}")