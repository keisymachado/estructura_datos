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
        self.en_marcha = False

    def __str__(self)-> str:
        return f"la marca del vehiculo es {self.marca} y el nivel de combustible es de {self.combustible} su tipo de vehiculo es {self.tipo}"
        

    def encender(self):
       if self.combustible <=10:
             return("no puede prender")
       else:
             self.en_marcha= True 
             return("puede prender ")
        
    def acelerar(self):
      if not self.en_marcha:
            return ("El vehículo no está encendido.")
      else:
            self.consumir_combustible()
            return ("El vehículo está acelerando.")

        
    def frenar(self):
        if self.en_marcha:
            return ("El vehículo está frenando.")
        else:
            return ("El vehículo no está encendido.")
        
    def apagar(self):
        self.en_marcha = False
        return ("El vehículo ha sido apagado.")
    
    def consumir_combustible(self):
        if self.en_marcha:
            self.combustible -= 1
            if self.combustible <= 10:
                print(f"Advertencia: Nivel de combustible bajo ({self.combustible} litros).")
            if self.combustible <= 0:
                self.combustible = 0
                self.en_marcha = False
                print("El vehículo se ha quedado sin combustible y se ha detenido.")

class moto(Vehiculo):
    pass
class carro(Vehiculo):
    pass

def simular_marcha(vehiculo, iteraciones):
    for _ in range(iteraciones):
        if vehiculo.en_marcha:  
            print(vehiculo.acelerar())
        else:
            break  

Vehiculo1 = Vehiculo ("mazda",10,"carro")
print(Vehiculo1)    
print(Vehiculo1.encender())


print(Vehiculo1.apagar())

moto1 = moto ("honda", 50,"moto")
print(moto1)    
print(moto1.encender())

print(moto1.apagar())
carro1 = carro ("renault", 70,"helicoptero")
print(carro1)
print(carro1.encender())


print(carro1.apagar())
