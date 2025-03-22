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
    
    def mostrar(self):
        print("Camino:", self.dato[:self.tope])

      
    def __init__(self, size, laberinto, inicio, salida):
        self.dato = [None] * size
        self.size = size
        self.tope = 0
        self.laberinto = laberinto  
        self.inicio = inicio        
        self.salida = salida

    def mostrar(self) -> None:
        
        for i in range(len(self.laberinto)):
            for j in range(len(self.laberinto[0])):
                if (i, j) == self.inicio:
                    print('S', end=' ')  # Muestra el inicio
                elif (i, j) == self.salida:
                    print('E', end=' ')
laberinto = [
    ['O', 'O', 'X', 'O', 'X'],
    ['X', 'O', 'X', 'O', 'X'],
    ['O', 'O', 'O', 'X', 'O'],
    ['X', 'O', 'O', 'O', 'O'],
    ['X', 'O', 'O', 'O', 'X']
]

desplazamiento_fila = [1, 0, 0, -1]  
desplazamiento_columna = [0, -1, 1, 0] 

inicio = (0, 0)
salida = (3, 4)

pila = Pila(6)
pila.mostrar(laberinto, inicio, salida)

   