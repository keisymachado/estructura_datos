from typing import Optional
class Node:
    def __init__(self, numero:int)-> None:
         self.dato = numero
         self.next : Optional ["Node"] = None

class listaEnlazada:
     def __init__(self)-> None:
          self.cabeza: Optional["Node"] = None
          if self.cabeza is None:
               self.cabeza= Node
          else: 
               Node.actual = self.cabeza
               while Node_actual.next is not None:
                  Node_actual = Node_actual.next
                  Node.next = self.cabeza
               self.cabeza= Node 

lista = listaEnlazada()
lista.agregar(26)
lista.agregar(30)
lista.agregar(7)
lista.agregar(6)
lista.agregar(2)
lista.agregar(4)