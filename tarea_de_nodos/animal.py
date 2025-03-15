from typing import Optional

class Animal:
    def __init__(self, nombre: str, edad: int, tipo: str) -> None:
        self.nombre = nombre
        self.edad = edad
        self.tipo = tipo

    def __str__(self) -> str:
        return f"{self.nombre} ({self.tipo}), {self.edad} años"



class Node:
    def __init__(self, animal: Animal):
        self.animal = animal
        self.next: Optional["Node"] = None


class ListaEnlazada:
    def __init__(self) -> None:
        self.cabeza: Optional[Node] = None

    def agregar_animal(self, nombre: str, edad: int, tipo: str) -> None:
        nuevo_animal = Animal(nombre, edad, tipo)
        nuevo_nodo = Node(nuevo_animal)

        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return

        nodo_actual = self.cabeza
        while nodo_actual.next is not None:
            if nodo_actual.animal.nombre == nombre and nodo_actual.animal.tipo == tipo:
                print(f"El animal {nombre} de tipo {tipo} ya está registrado.")
                return
            nodo_actual = nodo_actual.next

        if nodo_actual.animal.nombre == nombre and nodo_actual.animal.tipo == tipo:
            print(f"El animal {nombre} de tipo {tipo} ya está registrado.")
            return

        nodo_actual.next = nuevo_nodo

    def mostrar_animales_iterativo(self) -> None:
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            print(nodo_actual.animal)
            nodo_actual = nodo_actual.next

    def mostrar_animales_recursivo(self, nodo: Optional[Node] = None) -> None:
        if nodo is None:
            nodo = self.cabeza
        if nodo is not None:
            print(nodo.animal)
            if nodo.next is not None:  
                self.mostrar_animales_recursivo(nodo.next)



zoologico = ListaEnlazada()

zoologico.agregar_animal("key", 5, "León")
zoologico.agregar_animal("davi", 3, "Pavo")
zoologico.agregar_animal("karla", 2, "Gato")


print(" animales de manera iterativa:")
zoologico.mostrar_animales_iterativo()

print(" animales de manera recursiva:")
zoologico.mostrar_animales_recursivo()