from typing import Optional

# Clase Node  Representa cada elemento individual en el árbol binario
# Cada nodo contiene un valor y referencias a sus nodos hijos izquierdo y derecho
class Node:
    data: int
    left: Optional['Node']  # Subárbol izquierdo (valores menores)
    right: Optional['Node'] # Subárbol derecho (valores mayores)
    
    def __init__(self, data: int, left=None, right=None):
        # Constructor del nodo:
        # - data: valor numérico a almacenar
        # - left: nodo hijo izquierdo (opcional)
        # - right: nodo hijo derecho (opcional)
        self.data = data
        self.left = left
        self.right = right

# Clase BinaryTree - Implementa un Árbol Binario de Búsqueda (BST ose  Binary Search Tree))
# Los BST mantienen los valores ordenados donde:
# - Todos los valores izquierdos son menores que el padre
# - Todos los valores derechos son mayores o iguales que el padre
class BinaryTree:
    root: Optional[Node]  # El nodo raíz del árbol (puede ser None si está vacío)
    
    def __init__(self, root=None):
        # Inicializa un árbol binario, opcionalmente con un nodo raíz existente
        self.root = root

    def insert(self, data: int) -> None:
        
        #Inserta un nuevo valor en el árbol manteniendo el orden BST
        
    
        if self.root is None:
            # Si el árbol está vacío, creamos el nodo raíz
            self.root = Node(data)
        else:
            # Si hay raíz, buscamos la posición correcta recursivamente
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, node: Node, data: int) -> None:
        """
        recursivo para encontrar la posición de inserción
        - Si el valor es menor, va al subárbol izquierdo
        - Si es mayor o igual, va al subárbol derecho
        """
        if data < node.data:
            if node.left is None:
                # Insertamos en la izquierda si está vacío
                node.left = Node(data)
            else:
                # Continuamos buscando en el subárbol izquierdo
                self._insert_recursive(node.left, data)
        else:
            if node.right is None:
                # Insertamos en la derecha si está vacío
                node.right = Node(data)
            else:
                # Continuamos buscando en el subárbol derecho
                self._insert_recursive(node.right, data)

    def preorder_traversal(self, node: Optional[Node]) -> None:
        """
        Recorrido preorden (Raíz-Izquierda-Derecha)
        Útil para mostrar la estructura del árbol
        
        """
        if node is not None:
            print(node.data, end=' ')  # Primero procesamos la raíz
            self.preorder_traversal(node.left)  # Luego subárbol izquierdo
            self.preorder_traversal(node.right)  # Finalmente subárbol derecho

    def search(self, node: Optional[Node], data: int) -> bool:
        """
        Busca un valor en el árbol
        Retorna:
        - True si el valor existe
        - False si no se encuentra

        """
        if node is None:
            # llegamos a un nodo vacío
            return False
        if data == node.data:
            # Encontramos el valor
            return True
        elif data < node.data:
            # Buscamos en el subárbol izquierdo
            return self.search(node.left, data)
        else:
            # Buscamos en el subárbol derecho
            return self.search(node.right, data)


# Ejemplo de uso del árbol binario
if __name__ == "__main__":
    # Creamos una instancia del árbol
    tree = BinaryTree()
    
    # Valores iniciales para insertar
    initial_values = [4, 8, 24, 5, 14, 28, 48]
    
    # Insertamos todos los valores
    for value in initial_values:
        tree.insert(value)

    # Mostramos el árbol usando recorrido preorden
    print("Pre-order traversal of the tree:")
    tree.preorder_traversal(tree.root)

    # Menú para probar el árbol
    while True:
        print("Options ")
        print("1. Search for a value")
        print("2. Exit program")
        choice = input("Select an option (1-2): ")

        if choice == "1":
            try:
                # Solicitamos el valor a buscar
                search_value = int(input("Enter value to search: "))
                # Realizamos la búsqueda
                if tree.search(tree.root, search_value):
                    print(f"Value {search_value} found in the tree")
                else:
                    print(f"Value {search_value} not found")
            except ValueError:
                print("Error: Please enter a valid integer")
        elif choice == "2":
            print("Exiting the program... Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1 or 2")