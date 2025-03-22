class Pila:
    def __init__(self, size):
        self.dato = [None] * size
        self.size = size
        self.tope = 0

    def isEmpty(self):
        return self.tope == 0

    def push(self, elemento):
        if self.tope < self.size:
            self.dato[self.tope] = elemento
            self.tope += 1
        else:
            print(" Pila llena")

    def pop(self):
        if not self.isEmpty():
            self.tope -= 1
            return self.dato[self.tope]
        else:
            print(" Pila vacía")
            return None

    def peek(self):
        return self.dato[self.tope - 1] if not self.isEmpty() else None


def encontrar_inicio(laberinto):
    for fila in range(len(laberinto)):
        for columna in range(len(laberinto[fila])):
            if laberinto[fila][columna] == 'S':
                return (fila, columna)
    return None


def resolver_laberinto(laberinto):
    inicio = encontrar_inicio(laberinto)
    if not inicio:
        return "No hay punto de inicio (S)"

    filas = len(laberinto)
    columnas = len(laberinto[0])
    pila = Pila(filas * columnas)
    visitados = set()

    desplazamiento_fila = [1, 0, 0, -1]  
    desplazamiento_columna = [0, -1, 1, 0]

    pila.push((inicio[0], inicio[1], []))  

    while not pila.isEmpty():
        fila, columna, camino = pila.pop()
        nuevo_camino = camino + [(fila, columna)]

        if laberinto[fila][columna] == 'E':
            return nuevo_camino  

        visitados.add((fila, columna))

        for i in range(4):
            nueva_fila = fila + desplazamiento_fila[i]
            nueva_columna = columna + desplazamiento_columna[i]

            if (0 <= nueva_fila < filas and 
                0 <= nueva_columna < columnas and 
                (nueva_fila, nueva_columna) not in visitados and 
                laberinto[nueva_fila][nueva_columna] != 'X'):
                
                pila.push((nueva_fila, nueva_columna, nuevo_camino))

    return "No hay camino posible"


laberinto = [
    ['S', 'O', 'X', 'X', 'O'],
    ['X', 'O', 'O', 'X', 'O'],
    ['X', 'X', 'O', 'O', 'X'],
    ['O', 'O', 'X', 'O', 'E'],
    ['X', 'O', 'O', 'O', 'X']
]

solucion = resolver_laberinto(laberinto)
if isinstance(solucion, list):
    print("¡Camino encontrado! Coordenadas:", " → ".join([f"({f},{c})" for f, c in solucion]))
else:
    print(solucion)