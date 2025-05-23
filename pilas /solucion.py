from typing import Optional, Tuple

class Nodo:
    def __init__(self, valor: tuple[str, int], siguiente: Optional['Nodo'] = None):
        self.valor = valor
        self.siguiente = siguiente

class Pila:
    def __init__(self) -> None:
        self.tope: Optional[Nodo] = None

    def is_empty(self) -> bool:
        return self.tope is None

    def push(self, elemento: tuple[str, int]) -> None:
        nuevo_nodo = Nodo(elemento, self.tope)
        self.tope = nuevo_nodo

    def pop(self) -> Optional[tuple[str, int]]:
        if not self.is_empty():
            valor = self.tope.valor
            self.tope = self.tope.siguiente
            return valor
        return None

    def peek(self) -> Optional[tuple[str, int]]:
        if not self.is_empty():
            return self.tope.valor
        return None

def verificar_balanceo(expresion: str) -> Tuple[bool, int]:
    pila = Pila()
    simbolos_abiertos = {'(', '{', '['}
    simbolos_cerrados = {')', '}', ']'}
    parejas = {'(': ')', '{': '}', '[': ']'}

    for indice, caracter in enumerate(expresion):
        if caracter in simbolos_abiertos:
            pila.push((caracter, indice))
        elif caracter in simbolos_cerrados:
            if pila.is_empty():
                return False, indice
            tope = pila.peek()
            if tope is None or parejas.get(tope[0]) != caracter:
                return False, indice
            pila.pop()

    if pila.is_empty():
        return True, -1
    else:
        tope = pila.peek()
        return False, tope[1] if tope is not None else -1

expresion = "{[a + b] * (c - d)}"
balanceado, posicion = verificar_balanceo(expresion)

if balanceado:
    print("La expresión está balanceada.")
else:
    print(f"Error: Expresión desbalanceada en la posición {posicion}.")