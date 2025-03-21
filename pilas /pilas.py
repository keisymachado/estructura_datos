class Pila:
    def __init__(self, size)->int:
        self.dato = [None]* size 
        self.size = size 
        self.tope = 0  

    def isEmpty(self)-> bool:
        if self.tope == 0:
            return True
        else:
         return False 
    

    
    def push(self, dato)->int:
       if self.tope < self.size:
         self.dato[self.tope]= dato 
         self.tope += 1
       else:
           print("ya alcanzo el tope")
           #profe un compa me dijo que las pilas son infinitas pero yo le puse un tope de 6, y tambien que lo hiciera con append pero si no es correcto asi yo lo cambio pipipipi
 
    def pop(self)->int:
        if self.isEmpty():  
            print("La pila está vacía")
            return None
        else:
            self.tope -= 1
            dato_eliminado = self.dato[self.tope] 
            self.dato[self.tope] = None 
            return dato_eliminado

    def peek(self)->int:
        if self.isEmpty==0:
            print("La pila está vacía")
            return None
        else:
            return self.dato[self.tope - 1]  

    def mostrar(self)->int:
        print("Pila:", self.dato [:self.tope])


pila = Pila(6)
pila.push (25)
pila.push(2)
pila.push(3)
pila.push (5)
pila.push(1)
pila.push(26)
pila.push (44)

print("si se supero el tope se autoeliminara el ultimo numero puesto ")

pila.mostrar()  

print("Elemento en la cima:", pila.peek())

print("si sacamos el primer  elemento puesto en la pila ")
pila.pop()  
pila.mostrar()  