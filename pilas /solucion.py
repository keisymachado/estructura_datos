from typing import Optional, Tuple

class Pila:
    def __init__(self) -> None:
        self.datos: list[tuple[str, int]] = []

    def is_empty(self) -> bool:
        return len(self.datos) == 0  # true si la lista esta vacia 

    def push(self, elemento: tuple[str, int]) -> None:
        self.datos.append(elemento)

    def pop(self) ->str:
        if not self.is_empty():
            return self.datos.pop()
        return None

    def peek(self) -> str:
        if not self.is_empty():
            return self.datos[-1]
        return None

def verificar_balanceo(expresion: str) -> bool:
                
  
    pila = Pila()
    simbolos_abiertos = {'(', '{', '['}
    simbolos_cerrados = {')', '}', ']'}
    parejas = {'(': ')', '{': '}', '[': ']'}

    for indice, caracter in enumerate(expresion):
                        #Devuelve pares
        if caracter in simbolos_abiertos:
            pila.push((caracter, indice))
            #Si el caracter es de apertura, lo agrega a la pila con su posición.<
        elif caracter in simbolos_cerrados:
            if pila.is_empty() or parejas.get(pila.peek()[0]) != caracter:
                 #miramos el ultimo simbolo de apertura y buscamos en parejas cual es su cierre
                 #El método .get() busca una clave en el diccionario y devuelve su valor asociado
                return False, indice
            pila.pop()

    return (True, -1) if pila.is_empty() else (False, pila.peek()[1])
    #si se cerraron bien retorna true y si no pus false

#prueba
expresion = "{[a + b] * (c - d)}"
balanceado, posicion = verificar_balanceo(expresion)

if balanceado:
    print("La expresión está balanceada.")
else:
    print(f"Error: Expresión desbalanceada en la posición {posicion}.")
