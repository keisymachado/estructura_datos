from typing import Optional, Tuple, List, Union

class NodoPila:
    def __init__(self, valor: Tuple[int, int, List[Tuple[int, int]]], siguiente: Optional['NodoPila'] = None):
        self.valor = valor
        self.siguiente = siguiente

class Pila:
    def __init__(self) -> None:
        self.tope: Optional[NodoPila] = None
        self.contador = 0

    def isEmpty(self) -> bool:
        return self.tope is None
 
    def push(self, elemento: Tuple[int, int, List[Tuple[int, int]]]) -> None:
        nuevo_nodo = NodoPila(elemento, self.tope)
        self.tope = nuevo_nodo
        self.contador += 1

    def pop(self) -> Optional[Tuple[int, int, List[Tuple[int, int]]]]:
        if not self.isEmpty():
            valor = self.tope.valor
            self.tope = self.tope.siguiente
            self.contador -= 1
            return valor
        print("Pila vacía")
        return None

    def peek(self) -> Optional[Tuple[int, int, List[Tuple[int, int]]]]:
        return self.tope.valor if not self.isEmpty() else None

laberinto = [
    ['S', 'O', 'X', 'X', 'O'],
    ['X', 'O', 'O', 'X', 'O'],
    ['X', 'X', 'O', 'O', 'X'],
    ['O', 'O', 'X', 'O', 'E'],
    ['X', 'O', 'O', 'O', 'X']
]

def encontrar_inicio(laberinto: List[List[str]]) -> Optional[Tuple[int, int]]:
    for fila in range(len(laberinto)):
        for columna in range(len(laberinto[fila])):
            if laberinto[fila][columna] == 'S':
                return (fila, columna)
    return None

def resolver_laberinto(laberinto: List[List[str]]) -> Union[str, List[Tuple[int, int]]]:
    inicio = encontrar_inicio(laberinto)
    if not inicio:
        return "No hay punto de inicio (S)"

    filas = len(laberinto)
    columnas = len(laberinto[0])
    pila = Pila()
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

solucion = resolver_laberinto(laberinto)
if isinstance(solucion, list):
    print("¡Camino encontrado! Coordenadas:", " → ".join([f"({f},{c})" for f, c in solucion]))
else:
    print(solucion)