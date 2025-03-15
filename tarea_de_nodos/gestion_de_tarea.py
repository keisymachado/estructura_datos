from typing import Optional
from datetime import datetime


class Tarea:
    def __init__(self, descripcion: str, prioridad: int, fecha_vencimiento: str) -> None:
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.fecha_vencimiento = fecha_vencimiento
        self.completada = False

    def __str__(self) -> str:
        estado = "Completada" if self.completada else "Pendiente"
        return (
            f"Descripción: {self.descripcion}, "
            f"Prioridad: {self.prioridad}, "
            f"Vencimiento: {self.fecha_vencimiento}, "
            f"Estado: {estado}"
        )


class Node:
    def __init__(self, tarea: Tarea):
        self.tarea = tarea
        self.next: Optional["Node"] = None


class ListaEnlazadaTareas:
    def __init__(self) -> None:
        self.cabeza: Optional[Node] = None

    def agregar_tarea(self, descripcion: str, prioridad: int, fecha_vencimiento: str) -> None:
        nueva_tarea = Tarea(descripcion, prioridad, fecha_vencimiento)
        nuevo_nodo = Node(nueva_tarea)

        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
          
            nodo_actual = self.cabeza
            nodo_anterior = None

            while nodo_actual is not None and (
                nodo_actual.tarea.prioridad < prioridad
                or (
                    nodo_actual.tarea.prioridad == prioridad
                    and nodo_actual.tarea.fecha_vencimiento <= nueva_tarea.fecha_vencimiento
                )
            ):
                nodo_anterior = nodo_actual
                nodo_actual = nodo_actual.next

            if nodo_anterior is None:
                nuevo_nodo.next = self.cabeza
                self.cabeza = nuevo_nodo
            else:
                nuevo_nodo.next = nodo_actual
                nodo_anterior.next = nuevo_nodo

    def eliminar_tarea(self, descripcion: str) -> None:
        nodo_actual = self.cabeza
        nodo_anterior = None

        while nodo_actual is not None:
            if nodo_actual.tarea.descripcion == descripcion:
                if nodo_anterior is None:
                    self.cabeza = nodo_actual.next
                else:
                    nodo_anterior.next = nodo_actual.next
                print(f"Tarea '{descripcion}' eliminada.")
                return
            nodo_anterior = nodo_actual
            nodo_actual = nodo_actual.next

        print(f"Tarea '{descripcion}' no encontrada.")

    def mostrar_tareas(self) -> None:
        if self.cabeza is None:
            print("No hay tareas registradas.")
            return

        nodo_actual = self.cabeza
        while nodo_actual is not None:
            print(nodo_actual.tarea)
            nodo_actual = nodo_actual.next

    def buscar_tarea(self, descripcion: str) -> None:
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            if nodo_actual.tarea.descripcion == descripcion:
                print("Tarea encontrada:")
                print(nodo_actual.tarea)
                return
            nodo_actual = nodo_actual.next
        print(f"Tarea '{descripcion}' no encontrada.")

    def marcar_completada(self, descripcion: str) -> None:
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            if nodo_actual.tarea.descripcion == descripcion:
                nodo_actual.tarea.completada = True
                print(f"Tarea '{descripcion}' marcada como completada.")
                self.eliminar_tarea(descripcion)  
                return
            nodo_actual = nodo_actual.next
        print(f"Tarea '{descripcion}' no encontrada.")



sistema_tareas = ListaEnlazadaTareas()

sistema_tareas.agregar_tarea("Hacer la compra", 1, "2025-03-15")
sistema_tareas.agregar_tarea("Enviar tarea de estructura de datos",1,"2025-03-14")
sistema_tareas.agregar_tarea("Llamar al médico", 3, "2025-03-20")
sistema_tareas.agregar_tarea("Enviar informe", 2, "2025-03-05")


print("\nTodas las tareas ")
sistema_tareas.mostrar_tareas()


print("\n Marcar tarea 'Enviar informe' como completada ")
sistema_tareas.marcar_completada("Enviar informe")


print("\n Todas las tareas después de completar 'Enviar informe'")
sistema_tareas.mostrar_tareas()

print("\n Eliminar tarea 'Llamar al médico' ")
sistema_tareas.eliminar_tarea("Llamar al médico")


print("\n Todas las tareas después de eliminar 'Llamar al médico'")
sistema_tareas.mostrar_tareas()