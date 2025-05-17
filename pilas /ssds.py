class Pila:
    def __init__(self, size:int)->None:
        self.dato = [None] * size
        self.size = size
        self.tope = 0

    def isEmpty(self)->bool:
        return self.tope == 0
 
    def push(self, elemento)->None:
        if self.tope < self.size:
            #indicador y apuntador
            self.dato[self.tope] = elemento
            self.tope += 1
        else:
            print(" Pila llena")

    def pop(self)->tuple:
        if not self.isEmpty():
            self.tope -= 1
            return self.dato[self.tope]
        else:
            print(" Pila vacía")
            return None

    def peek(self)->tuple:
        return self.dato[self.tope - 1] if not self.isEmpty() else None

laberinto = [
    ['S', 'O', 'X', 'X', 'O'],
    ['X', 'O', 'O', 'X', 'O'],
    ['X', 'X', 'O', 'O', 'X'],
    ['O', 'O', 'X', 'O', 'E'],
    ['X', 'O', 'O', 'O', 'X']
]

def encontrar_inicio(laberinto:list)->tuple:
    for fila in range(len(laberinto)):
        for columna in range(len(laberinto[fila])):
            if laberinto[fila][columna] == 'S':
                return (fila, columna)
    return None


def resolver_laberinto(laberinto: list)->str:
    inicio = encontrar_inicio(laberinto)
    if not inicio:
        return "No hay punto de inicio (S)"

    filas = len(laberinto)
    columnas = len(laberinto[0])
    pila = Pila(filas * columnas)
    visitados = set()
                #conjunto 

    desplazamiento_fila = [1, 0, 0, -1]  
    desplazamiento_columna = [0, -1, 1, 0]

    pila.push((inicio[0], inicio[1], []))  
    #corrdenadas de inicip
    while not pila.isEmpty():
        fila, columna, camino = pila.pop()
        nuevo_camino = camino + [(fila, columna)]
        #nuevo camino con la posicion actual
        if laberinto[fila][columna] == 'E':
            return nuevo_camino  

        visitados.add((fila, columna))
        #marrca la celda como visitada 

        for i in range(4):
            nueva_fila = fila + desplazamiento_fila[i]
            nueva_columna = columna + desplazamiento_columna[i]

            if (0 <= nueva_fila < filas and 
                0 <= nueva_columna < columnas and 
                (nueva_fila, nueva_columna) not in visitados and 
                laberinto[nueva_fila][nueva_columna] != 'X'):
                
                pila.push((nueva_fila, nueva_columna, nuevo_camino))

    return "No hay camino posible"



solucion = resolver_laberinto(laberinto)
if isinstance(solucion, list):
    print("¡Camino encontrado! Coordenadas:", " → ".join([f"({f},{c})" for f, c in solucion]))
else:
    print(solucion)