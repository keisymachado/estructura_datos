class Persona:
    def __init__(self, nombre: str, edad: int, genero: str):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero

    def presentarse(self):
        print(f"Hola, soy {self.nombre}, tengo {self.edad} años y soy {self.genero}.")

    def __str__(self):
        return f"{self.nombre}, {self.edad} años, {self.genero}"


class CuentaBan:
    def __init__(self, titular: Persona, saldo: float, numero_cuenta: str):
        self.titular = titular
        self.saldo = saldo
        self.numero_cuenta = numero_cuenta

    def depositar(self, cantidad: float):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Depósito de {cantidad} realizado. Saldo actual: {self.saldo}")
        else:
            print("La cantidad a depositar debe ser mayor que 0.")

    def retirar(self, cantidad: float):
        if cantidad > 0:
            if self.saldo >= cantidad:
                self.saldo -= cantidad
                print(f"Retiro de {cantidad} realizado. Saldo actual: {self.saldo}")
            else:
                print("Fondos insuficientes.")
        else:
            print("La cantidad a retirar debe ser mayor que 0.")

    def consultar_saldo(self):
        print(f"Saldo actual: {self.saldo}")

 
if __name__ == "__main__":
    persona1 = Persona("keisy ", 18, "ingeniera")
    cuenta1 = CuentaBan(persona1, 1000.0, "123456789")
    cuenta1.depositar(500)
    cuenta1.retirar(200)
    cuenta1.consultar_saldo()