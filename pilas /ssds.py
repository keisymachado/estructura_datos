from typing import Optional, Tuple, Union

class NodoCamino:
    """Nodo para representar cada posición en el camino"""
    def __init__(self, posicion: Tuple[int, int], anterior: Optional['NodoCamino'] = None):
        self.posicion = posicion  # Tupla (fila, columna)
        self.anterior = anterior  # Referencia al nodo anterior

class NodoPila:
    """Nodo para la pila que almacena los nodos de camino"""
    def __init__(self, valor: NodoCamino, siguiente: Optional['NodoPila'] = None):
        self.valor = valor
        self.siguiente = siguiente

class Pila:
    """Implementación de pila usando nodos"""
    def __init__(self):
        self.tope: Optional[NodoPila] = None
        self.contador = 0

    def esta_vacia(self) -> bool:
        return self.tope is None

    def apilar(self, elemento: NodoCamino) -> None:
        nuevo_nodo = NodoPila(elemento, self.tope)
        self.tope = nuevo_nodo
        self.contador += 1

    def desapilar(self) -> Optional[NodoCamino]:
        if not self.esta_vacia():
            valor = self.tope.valor
            self.tope = self.tope.siguiente
            self.contador -= 1
            return valor
        return None

def encontrar_inicio(laberinto: list[list[str]]) -> Optional[Tuple[int, int]]:
    """Encuentra la posición inicial 'S' en el laberinto"""
    for fila in range(len(laberinto)):
        for columna in range(len(laberinto[fila])):
            if laberinto[fila][columna] == 'S':
                return (fila, columna)
    return None

def resolver_laberinto(laberinto: list[list[str]]) -> Union[str, NodoCamino]:
    """Resuelve el laberinto usando una estructura de nodos"""
    inicio = encontrar_inicio(laberinto)
    if not inicio:
        return "No hay punto de inicio (S)"

    filas = len(laberinto)
    columnas = len(laberinto[0])
    pila = Pila()
    visitados = set()

    # Movimientos posibles: abajo, izquierda, derecha, arriba
    desplazamientos = [(1, 0), (0, -1), (0, 1), (-1, 0)]

    nodo_inicio = NodoCamino(inicio)
    pila.apilar(nodo_inicio)
    visitados.add(inicio)

    while not pila.esta_vacia():
        nodo_actual = pila.desapilar()
        fila, columna = nodo_actual.posicion

        if laberinto[fila][columna] == 'E':
            return nodo_actual  # Devuelve el nodo final (que contiene la referencia al camino completo)

        for df, dc in desplazamientos:
            nueva_fila = fila + df
            nueva_columna = columna + dc

            if (0 <= nueva_fila < filas and 
                0 <= nueva_columna < columnas and 
                (nueva_fila, nueva_columna) not in visitados and 
                laberinto[nueva_fila][nueva_columna] != 'X'):
                
                nuevo_nodo = NodoCamino((nueva_fila, nueva_columna), nodo_actual)
                pila.apilar(nuevo_nodo)
                visitados.add((nueva_fila, nueva_columna))

    return "No hay camino posible"

def imprimir_camino(nodo_final: Optional[NodoCamino]) -> None:
    """Imprime el camino desde el nodo final"""
    if isinstance(nodo_final, str):
        print(nodo_final)
        return
    
    camino = []
    actual = nodo_final
    while actual is not None:
        camino.append(actual.posicion)
        actual = actual.anterior
    
    # Invertimos para mostrar de inicio a fin
    camino_str = " → ".join([f"({f},{c})" for f, c in reversed(camino)])
    print("¡Camino encontrado! Coordenadas:", camino_str)

# Laberinto de ejemplo
laberinto = [
    ['S', 'O', 'X', 'X', 'O'],
    ['X', 'O', 'O', 'X', 'O'],
    ['X', 'X', 'O', 'O', 'X'],
    ['O', 'O', 'X', 'O', 'E'],
    ['X', 'O', 'O', 'O', 'X']
]

# Resolver e imprimir
solucion = resolver_laberinto(laberinto)
imprimir_camino(solucion)