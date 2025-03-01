#clase
class Vehiculo :
#atributos 
    color: str
    modelo:int
    cilindraje:int
    numero_ruedas: int  
    combustible : int
    tipo: str
    combustible :int

    def __init__(self, marca:str, combustible:int, tipo:str)-> None:
        self.marca = marca
        self.combustible = combustible
        self.tipo = tipo 
    def __str__(self)-> str:
        return f"la marca del vehiculo es {self.marca}y el nivel de combustible es de {self.combustible} su tipo de vehiculo es {self.tipo}"
        pass

    def encender(self):
       if self.combustible <=10:
             return("no puede prender")
       else:
             return("puede prender ")
        
    def acelerar(self):
        pass
    def frenar(self):
        pass
    def apagar(self):
        pass

class moto(Vehiculo):
    pass
class carro(Vehiculo):
    pass

Vehiculo1 = Vehiculo ("mazda",80,"carro")
print(Vehiculo1)    
print(Vehiculo1.encender())
moto1 = moto ("honda", 50,"moto")
print(moto1)    
print(moto1.encender())
carro1 = carro ("renault", 70,"helicoptero")
print(carro1)
print(carro1.encender())

def marchar(self, consumo_por_km: int, distancia: int):
        if self.combustible <= 0:
            return "El vehículo no tiene combustible."

        for km in range(1, distancia + 1):
            self.combustible = consumo_por_km
            if self.combustible <= 0:
                self.combustible = 0
                print(f"Combustible agotado después de {km} km. El vehículo se detiene.")
                return
            elif self.combustible <= 10:
                print(f" Advertencia: Bajo nivel de combustible ({self.combustible} litros) después de {km} km.")

        print(f"El vehículo ha recorrido {distancia} km. Nivel de combustible actual: {self.combustible} litros.")

def frenar(self):
        return "El vehículo se ha detenido."

def apagar(self):
        return "El vehículo se ha apagado."
