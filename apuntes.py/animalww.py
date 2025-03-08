from typing import Optional

class Animal:
    def __init__(self, nombre: str, edad: int, tipo: str) -> None:
        self.nombre = nombre
        self.edad = edad
        self.tipo = tipo
        

class Node:
    def __init__(self,animal:Animal):
        self.animal= animal
        self.next: Optional["Node"] = None

class ListaEnlazada:
    def __init__(self) -> None:
        self.cabeza: Optional[Node] = None

    def agregar_animal(self, nombre: str, edad: int, tipo: str) -> None:
        nuevo_animal = Animal(nombre, edad, tipo)
        nodeAnimal=Node(nuevo_animal)
        
        if self.cabeza is None:
            self.cabeza = nuevo_animal
            return
        
        node_actual = self.cabeza
        while node_actual.next is not None:
            if node_actual.nombre == nombre and node_actual.tipo == tipo:
                print(f"El animal {nombre} de tipo {tipo} ya está registrado.")
                return
            node_actual = node_actual.next
        
        if node_actual.nombre == nombre and actual.tipo == tipo:
            print(f"El animal {self.nombre} con {self.edad} de tipo {self.tipo} ya está registrado.")
            return
        
        node_actual.next = nuevo_animal

    
zoologico = ListaEnlazada()

zoologico.agregar_animal("Leo", 5, "León")
zoologico.agregar_animal("Paco", 3, "Pavo")
zoologico.agregar_animal("Mimi", 2, "Gato")
zoologico.agregar_animal("Leo", 5, "León") 

