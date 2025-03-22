class Pila:
    def __init__(self):
        self.dato = []

    def isEmpty(self):
        return len(self.dato) == 0

    def push(self, elemento):
        self.dato.append(elemento)

    def pop(self):
        if not self.isEmpty():
            return self.dato.pop()
        else:
            return None

    def peek(self):
        if not self.isEmpty():
            return self.dato[-1]
        else:
            return None


def verificar_balanceo(expresion: str) -> tuple:
    """Verifica el balanceo de símbolos en una expresión."""
    pila = Pila()
    simbolos_abiertos = {'(', '{', '['}
    simbolos_cerrados = {')', '}', ']'}
    parejas = {'(': ')', '{': '}', '[': ']'}

    for i, caracter in enumerate(expresion):
        if caracter in simbolos_abiertos:
            pila.push((caracter, i)) 
        elif caracter in simbolos_cerrados:
            if pila.isEmpty() or parejas[pila.peek()[0]] != caracter:
                return False, i  
            pila.pop()

    if pila.isEmpty():
        return True, -1 
    else:
        return False, pila.peek()[1] 


expresion = "{[a + b] * (c - d)}"
balanceado, posicion = verificar_balanceo(expresion)

if balanceado:
    print("La expresión está balanceada.")
else:
    print(f"Error: Expresión desbalanceada en la posición {posicion}.")